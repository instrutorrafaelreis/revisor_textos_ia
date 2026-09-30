import os
from dotenv import load_dotenv

# Carrega as chaves do arquivo .env (Oculto)
load_dotenv()

# Configuração Gemini (Nuvem)
USE_GEMINI = True
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
GEMINI_MODEL = 'gemini-3.5-flash'

# Configuração NVIDIA NIM (Nuvem)
USE_NVIDIA = True
NVIDIA_API_KEY = os.getenv('NVIDIA_API_KEY', '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')
NVIDIA_MODELS = [
    'meta/llama-3.2-11b-vision-instruct',
    'z-ai/glm-5.3-flash'
]

