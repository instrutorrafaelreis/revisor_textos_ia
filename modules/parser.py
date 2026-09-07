import pymupdf  # substituiu o antigo fitz
import re
import os
import docx

def extract_text_from_pdf(pdf_path):
    try:
        doc = pymupdf.open(pdf_path)
        text = ''
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f'Error reading PDF: {e}')
        return None

def extract_text_from_docx(docx_path):
    try:
        doc = docx.Document(docx_path)
        text = '\\n'.join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        print(f'Error reading DOCX: {e}')
        return None

def extract_text_from_md(md_path):
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f'Error reading MD: {e}')
        return None

def extract_references_section(text):
    # Regex to find 'Referências' or 'Referências Bibliográficas' until the end
    # Assuming standard academic formatting
    match = re.search(r'(?i)\\n\s*(?:REFER\u00CANCIAS(?:\s+BIBLIOGR\u00C1FICAS)?|REFERENCIAS(?:\s+BIBLIOGRAFICAS)?)\s*\\n(.*)', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ''

def extract_citations(text):
    # Captures standard ABNT citations like (SILVA, 2021) or (SILVA; SANTOS, 2021)
    citations = re.findall(r'\([A-Z\u00C0-\u00DCa-z\u00E0-\u00FC\s;]+,\s*\d{4}[a-z]?\)', text)
    return citations

def parse_document(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif ext == '.docx':
        text = extract_text_from_docx(file_path)
    elif ext == '.md':
        text = extract_text_from_md(file_path)
    else:
        print(f"Formato não suportado: {ext}")
        return None

    if not text:
        return None
    
    references = extract_references_section(text)
    citations = extract_citations(text)
    
    return {
        'full_text': text,
        'references_section': references,
        'citations': citations
    }
