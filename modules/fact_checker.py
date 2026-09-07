import requests
import re

def check_reference_crossref(reference_text):
    if len(reference_text.strip()) < 10:
        return None
    
    url = 'https://api.crossref.org/works'
    params = {
        'query.bibliographic': reference_text,
        'rows': 1,
        'select': 'title,author,DOI,score'
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            items = data.get('message', {}).get('items', [])
            if items:
                return items[0]
    except Exception as e:
        print(f'Error calling Crossref: {e}')
    return None

import concurrent.futures

def process_single_reference(ref):
    if len(ref) > 20:
        match = check_reference_crossref(ref)
        if match:
            return {'reference': ref, 'found': True, 'crossref_data': match}
        else:
            return {'reference': ref, 'found': False, 'crossref_data': None}
    return None

def analyze_references(references_text):
    if not references_text:
        return []
    
    # Split references by looking for typical patterns (e.g. all caps name at start of line)
    # A naive split by newline first
    lines = references_text.split('\n')
    refs = []
    current_ref = ''
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if re.match(r'^[A-Z\u00C0-\u00DC\s]+,', line): # Starts with Last Name,
            if current_ref:
                refs.append(current_ref)
            current_ref = line
        else:
            current_ref += ' ' + line
    if current_ref:
        refs.append(current_ref)
        
    results = []
    # Paraleliza as requisições ao Crossref (super rápido)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_ref = {executor.submit(process_single_reference, ref): ref for ref in refs}
        for future in concurrent.futures.as_completed(future_to_ref):
            res = future.result()
            if res:
                results.append(res)
                
    return results
