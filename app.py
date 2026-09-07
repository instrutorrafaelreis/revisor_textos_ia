import streamlit as st
import os
import tempfile

from modules.parser import parse_document
from modules.fact_checker import analyze_references
from modules.stylometrics import analyze_style
from modules.semantic_judge import evaluate_text_semantics
from utils.report_generator import generate_report

st.set_page_config(page_title="Auditor Acadêmico", page_icon="🎓", layout="wide")

st.title("🎓 Auditor Acadêmico com IA")
st.markdown("Faça o upload do seu texto acadêmico (TCC, Artigo, etc) e a inteligência artificial auditará o conteúdo em busca de clichês, alucinações e erros de ABNT.")

uploaded_file = st.file_uploader("Selecione seu documento", type=["pdf", "docx", "md"])

if uploaded_file is not None:
    # Mostra um botão para iniciar a análise
    if st.button("Iniciar Auditoria"):
        with st.spinner("Analisando o documento... Isso pode levar alguns segundos."):
            
            # Salvar arquivo temporariamente para os módulos processarem
            # Criamos na pasta data
            os.makedirs("data", exist_ok=True)
            temp_path = os.path.join("data", uploaded_file.name)
            
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
                
            try:
                # 1. Parsing
                st.info("1/4 Extraindo texto do documento...")
                parsed_data = parse_document(temp_path)
                
                if not parsed_data:
                    st.error("Não foi possível extrair o texto do documento.")
                else:
                    # 2. Fact Checking
                    st.info("2/4 Verificando referências e citações...")
                    fact_check_results = analyze_references(parsed_data.get('references_section'))
                    
                    # 3. Stylometrics
                    st.info("3/4 Realizando análise estilométrica e buscando clichês de IA...")
                    style_results = analyze_style(parsed_data.get('full_text'))
                    
                    # 4. Semantic Judge
                    st.info("4/4 O Juiz Semântico está lendo o texto...")
                    semantic_results = evaluate_text_semantics(parsed_data.get('full_text'))
                    
                    # Concluindo
                    results = {
                        "fact_checking": fact_check_results,
                        "stylometrics": style_results,
                        "semantic_judge_analysis": semantic_results
                    }
                    
                    # A função generate_report salva json e md na pasta raiz
                    report = generate_report(results, output_path="analise_resultado.json")
                    
                    st.success("Auditoria concluída com sucesso!")
                    
                    # --- RENDERIZANDO DASHBOARD ---
                    st.markdown("---")
                    st.header("📊 Resumo das Métricas")
                    col1, col2, col3 = st.columns(3)
                    
                    col1.metric("Risco em Referências Falsas", report["risco_referencias_falsas"])
                    col2.metric("Marcadores de IA Detectados", report["marcadores_llm_encontrados"])
                    col3.metric("Perplexidade (Complexidade)", report["perplexidade_texto"])
                    
                    st.markdown("---")
                    st.header("🤖 Avaliação do Juiz Semântico")
                    # O retorno semântico já vem formatado em markdown pelo LLM
                    st.markdown(report["juiz_semantico"] if report["juiz_semantico"] else "Análise semântica falhou.")
                    
                    with st.expander("Ver logs técnicos e referências analisadas (JSON)"):
                        st.json(report["detalhes"])
                        
            finally:
                # Limpeza: Apagar arquivo temporário
                if os.path.exists(temp_path):
                    os.remove(temp_path)
