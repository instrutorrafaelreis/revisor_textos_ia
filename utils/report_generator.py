import json

def generate_report(results, output_path="report.json"):
    # Calcula um score ponderado (simplificado para este exemplo)
    
    # 1. Checa referencias
    refs = results.get('fact_checking', [])
    not_found_refs = sum(1 for r in refs if not r['found'])
    total_refs = len(refs) if refs else 1
    ref_hallucination_score = (not_found_refs / total_refs) * 10
    
    # 2. Estilometria
    style = results.get('stylometrics', {})
    markers = style.get('marker_count', 0)
    # Se perplexidade for muito baixa, maior risco (ex: < 15 pode ser IA, depende do modelo)
    ppl = style.get('perplexity')
    
    # Consolidação
    report = {
        "risco_referencias_falsas": f"{ref_hallucination_score:.1f}/10",
        "marcadores_llm_encontrados": markers,
        "perplexidade_texto": f"{ppl:.2f}" if ppl else "N/A",
        "juiz_semantico": results.get('semantic_judge_analysis'),
        "detalhes": results
    }
    
    # Salva JSON (útil para integração com outros sistemas)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
        
    # Salva MARKDOWN (útil para leitura humana)
    md_path = output_path.replace('.json', '.md')
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Relatório de Auditoria Acadêmica\n\n")
        f.write("## 1. Métricas Heurísticas e Estilometria\n")
        f.write(f"- **Risco de Referências Falsas/Alucinações**: {report['risco_referencias_falsas']}\n")
        f.write(f"- **Marcadores de Texto Gerado (Clichês)**: {report['marcadores_llm_encontrados']}\n")
        f.write(f"- **Perplexidade (Complexidade do Texto)**: {report['perplexidade_texto']}\n\n")
        f.write("---\n\n")
        f.write("## 2. Avaliação do Juiz Semântico (IA)\n\n")
        f.write(report['juiz_semantico'] if report['juiz_semantico'] else "Análise semântica não disponível.")
        f.write("\n")
    
    print(f"\n[OK] Relatório completo gerado em: {md_path}")
    
    return report
