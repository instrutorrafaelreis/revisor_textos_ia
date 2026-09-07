from fastapi import FastAPI, File, UploadFile, Form
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from modules.parser import parse_document
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

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
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
        # O Fact Checker (Crossref via internet) foi removido para focar na leitura do manual offline!
        fact_check_results = [] 
        t1 = time.time()
        
        style_results = analyze_style(parsed_data.get('full_text'))
        t2 = time.time()
        print(f"[DEBUG] Tempo de Estilometria: {t2 - t1:.2f}s")
        
        semantic_results = evaluate_text_semantics(parsed_data.get('full_text'), model_choice=model_choice)
        t3 = time.time()
        print(f"[DEBUG] Tempo do Juiz Semântico: {t3 - t2:.2f}s")
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

@app.post("/api/generate_prompt")
async def generate_prompt(text: str = Form(...)):
    try:
        import config
        from google import genai
        from google.genai import types
        
        client = genai.Client(api_key=config.GEMINI_API_KEY)
        prompt_instruction = f"""Com base neste texto acadêmico que possui erros, gere um PROMPT DE COMANDO para o usuário copiar e colar no ChatGPT/Claude.
        O prompt gerado deve instruir a IA externa a corrigir erros de ABNT e remover clichês.
        Responda APENAS com o texto do prompt, para ser facilmente copiado.
        
        Texto original:
        {text[:2500]}"""
        
        res = client.models.generate_content(
            model=config.GEMINI_MODEL,
            contents=prompt_instruction,
            config=types.GenerateContentConfig(temperature=0.3)
        )
        return {"prompt": res.text}
    except Exception as e:
        return {"error": str(e)}
