import re

LLM_MARKERS = [
    'Em suma', 'É imperativo notar que', 'Vale destacar que', 
    'Em um mundo cada vez mais', 'É crucial ressaltar',
    'Podemos concluir que', 'Importante observar', 'Neste viés', 'Em síntese'
]

def count_llm_markers(text):
    count = 0
    found_markers = []
    for marker in LLM_MARKERS:
        # case insensitive search
        matches = re.findall(rf'(?i)\b{re.escape(marker)}\b', text)
        count += len(matches)
        if matches:
            found_markers.extend(matches)
    return count, found_markers

def calculate_perplexity(text):
    # Desativado hardcoded para evitar qualquer gargalo de memória/CPU
    return "Desativado (Foco em Desempenho)"

def analyze_style(text):
    marker_count, markers = count_llm_markers(text)
    # Skipping perplexity for very large texts to avoid freezing, or limit to first N words
    ppl = calculate_perplexity(text[:2000]) if len(text) > 0 else None
    
    return {
        'marker_count': marker_count,
        'markers_found': markers,
        'perplexity': ppl
    }
