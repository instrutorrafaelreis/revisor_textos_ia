import re

def clean_text(text):
    if not text:
        return ""
    # Remove excessive newlines
    text = re.sub(r'\n+', '\n', text)
    # Remove excessive spaces
    text = re.sub(r' +', ' ', text)
    return text.strip()
