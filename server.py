from fastapi import FastAPI, File, UploadFile, Form
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from modules.parser import parse_document
from modules.fact_checker import analyze_references
from modules.stylometrics import analyze_style
from modules.semantic_judge import evaluate_text_semantics
from utils.report_generator import generate_report

app = FastAPI(title="API Auditor Acadêmico")

# Permite acesso ao frontend se estiver rodando em portas diferentes (ex: React em dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cria a pasta estática se não existir
os.makedirs("static", exist_ok=True)

# Servindo os arquivos do Frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    # Rota raiz que entrega o nosso HTML (Interface Visual)
    index_path = os.path.join("static", "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>Frontend não encontrado. Crie o arquivo static/index.html</h1>")

@app.post("/api/analyze")
async def analyze_file(
    file: Optional[UploadFile] = File(None), 
    text: Optional[str] = Form(None),
    model_choice: str = Form("todos")
):
    if not file and not text:
        return {"error": "Por favor, envie um arquivo ou cole um texto."}
        
    try:
        if text:
            # Processa o texto puro colado pelo usuário
            parsed_data = {
                'full_text': text,
                'references_section': text
            }
        else:
            # 1. Salvar o arquivo
            os.makedirs("data", exist_ok=True)
            file_location = os.path.join("data", file.filename)
            
            with open(file_location, "wb+") as file_object:
                file_object.write(await file.read())
                
            # 2. Executar a extração (Parser)
            parsed_data = parse_document(file_location)
            
        if not parsed_data:
            return {"error": "Não foi possível extrair o texto."}
            
        # 3. Análises
        import time
        
        t0 = time.time()
        fact_check_results = analyze_references(parsed_data.get('references_section'))
        t1 = time.time()
        print(f"[DEBUG] Tempo do Fact Checker (Crossref): {t1 - t0:.2f}s")
        
        style_results = analyze_style(parsed_data.get('full_text'))
        t2 = time.time()
        print(f"[DEBUG] Tempo de Estilometria (PyTorch/Regex): {t2 - t1:.2f}s")
        
        semantic_results = evaluate_text_semantics(parsed_data.get('full_text'), model_choice=model_choice)
        t3 = time.time()
        print(f"[DEBUG] Tempo do Juiz Semântico (APIs de IA): {t3 - t2:.2f}s")
        print(f"[DEBUG] TEMPO TOTAL DE ANÁLISE: {t3 - t0:.2f}s")
        
        results = {
            "fact_checking": fact_check_results,
            "stylometrics": style_results,
            "semantic_judge_analysis": semantic_results
        }
        
        # 4. Gerar Relatório e Retornar
        report = generate_report(results, output_path="analise_resultado.json")
        return report
        
    finally:
        # Limpar arquivo temporário se quiser (opcional)
        pass
