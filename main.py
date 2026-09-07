import os
import argparse
import tkinter as tk
from tkinter import filedialog
from pprint import pprint

from modules.parser import parse_document
from modules.fact_checker import analyze_references
from modules.stylometrics import analyze_style
from modules.semantic_judge import evaluate_text_semantics
from utils.report_generator import generate_report

def get_file_path_interactively():
    # Cria uma janela oculta do Tkinter
    root = tk.Tk()
    root.withdraw()
    # Abre a janela de diálogo para o usuário escolher o arquivo
    print("Por favor, selecione o documento (PDF, DOCX ou MD) na janela que se abriu...")
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo para análise",
        filetypes=[
            ("Documentos", "*.pdf *.docx *.md"),
            ("Arquivos PDF", "*.pdf"),
            ("Arquivos Word", "*.docx"),
            ("Arquivos Markdown", "*.md"),
            ("Todos os Arquivos", "*.*")
        ]
    )
    return file_path

def main():
    parser = argparse.ArgumentParser(description="Agente Analisador de Textos Acadêmicos")
    parser.add_argument("file_path", nargs="?", help="Caminho para o arquivo (PDF, DOCX ou MD) a ser analisado")
    args = parser.parse_args()

    # Se o usuário não passar o caminho no comando, pedimos para selecionar
    file_path = args.file_path
    if not file_path:
        file_path = get_file_path_interactively()
        
    if not file_path or not os.path.exists(file_path):
        print("Erro: Nenhum arquivo válido foi selecionado ou encontrado.")
        return

    print(f"\nIniciando análise do arquivo: {file_path}")
    
    # Módulo 1
    print("1. Extraindo texto e metadados...")
    parsed_data = parse_document(file_path)
    if not parsed_data:
        print("Falha ao extrair texto.")
        return

    # Módulo 2
    print("2. Verificando integridade das referências...")
    fact_check_results = analyze_references(parsed_data.get('references_section'))

    # Módulo 3
    print("3. Analisando estilometria e marcadores...")
    style_results = analyze_style(parsed_data.get('full_text'))

    # Módulo 4
    print("4. Executando auditor semântico...")
    semantic_results = evaluate_text_semantics(parsed_data.get('full_text'))

    # Consolidação
    print("5. Gerando relatório...")
    results = {
        "fact_checking": fact_check_results,
        "stylometrics": style_results,
        "semantic_judge_analysis": semantic_results
    }
    
    report = generate_report(results, output_path="analise_resultado.json")
    print("\n--- Relatório Resumido ---")
    pprint(report)
    print("\nRelatório completo salvo em analise_resultado.json")

if __name__ == "__main__":
    main()
