import re
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

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
    # Only load model if called to save memory/time
    try:
        tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        model = GPT2LMHeadModel.from_pretrained('gpt2')
        
        encodings = tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
        max_length = model.config.n_positions
        stride = 512
        
        nlls = []
        for i in range(0, encodings.input_ids.size(1), stride):
            begin_loc = max(i + stride - max_length, 0)
            end_loc = min(i + stride, encodings.input_ids.size(1))
            trg_len = end_loc - i    # may be different from stride on last loop
            input_ids = encodings.input_ids[:, begin_loc:end_loc]
            target_ids = input_ids.clone()
            target_ids[:, :-trg_len] = -100
            
            with torch.no_grad():
                outputs = model(input_ids, labels=target_ids)
                neg_log_likelihood = outputs.loss * trg_len
            nlls.append(neg_log_likelihood)
            
        ppl = torch.exp(torch.stack(nlls).sum() / end_loc)
        return ppl.item()
    except Exception as e:
        print(f'Error calculating perplexity: {e}')
        return None

def analyze_style(text):
    marker_count, markers = count_llm_markers(text)
    # Skipping perplexity for very large texts to avoid freezing, or limit to first N words
    ppl = calculate_perplexity(text[:2000]) if len(text) > 0 else None
    
    return {
        'marker_count': marker_count,
        'markers_found': markers,
        'perplexity': ppl
    }
