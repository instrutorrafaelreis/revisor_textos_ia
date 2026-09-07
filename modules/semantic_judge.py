from google import genai
from google.genai import types
from openai import OpenAI
import requests
import sys
import os

# Adiciona o diretorio pai ao path para importar config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

import concurrent.futures

def fetch_gemini(client, prompt):
    try:
        response = client.models.generate_content(
            model=config.GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.3,
                system_instruction="Você é um assistente rigoroso de revisão acadêmica. IMPORTANTE: Sua resposta deve ser EXCLUSIVAMENTE em Português do Brasil (PT-BR)."
            )
        )
        return f"### ✨ Análise do Modelo Nuvem (Gemini - {config.GEMINI_MODEL})\n\n{response.text}"
    except Exception as e:
        return f"### ✨ Análise do Modelo Nuvem (Gemini)\n\n**Erro:** {e}"

def fetch_nvidia(client_nv, model_name, prompt):
    try:
        kwargs = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": "Você é um assistente rigoroso de revisão acadêmica. IMPORTANTE: Sua resposta deve ser EXCLUSIVAMENTE em Português do Brasil (PT-BR). NÃO VAZAR PROCESSO DE PENSAMENTO. NÃO mostre tags como <think> ou 'Here is a thinking process'. Retorne APENAS o relatório final formatado."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 2500,
            "stream": False
        }
        
        if "deepseek" in model_name.lower():
            kwargs["extra_body"] = {"chat_template_kwargs": {"thinking": False}}
            
        completion = client_nv.chat.completions.create(**kwargs)
        nv_text = completion.choices[0].message.content
        return f"### 🟢 Análise do Modelo Nuvem (NVIDIA - {model_name})\n\n{nv_text}"
    except Exception as e:
        return f"### 🟢 Análise do Modelo Nuvem (NVIDIA - {model_name})\n\n**Erro:** {e}"

def evaluate_text_semantics(text, model_choice="todos"):
    """
    Avalia a semântica do texto (clichês, coesão, estilo acadêmico) via LLM (Gemini e/ou NVIDIA).
    Paralelizado para ser extremamente rápido.
    """
    if not text or len(text.strip()) < 50:
        return "Texto insuficiente para análise semântica estrutural."
        
    if not getattr(config, 'USE_GEMINI', False) and not getattr(config, 'USE_NVIDIA', False):
        return 'Configuração de modelos desativada.'
        
    prompt = f"""Você é um auditor acadêmico rigoroso. Seu objetivo é analisar o texto e entregar instruções de melhoria.

Analise o texto quanto a:
1. Circularidade argumentativa e clichês de IA.
2. Superficialidade técnica.
3. Normas da ABNT (citações e referências).

SAÍDA OBRIGATÓRIA (Siga ESTRITAMENTE este formato):

**Análise Geral**: (Breve avaliação crítica do texto)

**O Que Corrigir**: (Liste os principais problemas encontrados no texto)

**Indícios de Plágio**: (Avalie se o texto possui trechos exatos muito comuns na internet, jargões copiados de enciclopédias ou artigos famosos. Atribua um nível de 'Risco de Plágio' de Baixo, Médio ou Alto e justifique).

**Prompt Sugerido para Correção (Copiar e Colar)**:
Crie um PROMPT PRONTO E OTIMIZADO que o usuário possa copiar e colar no ChatGPT, Claude ou qualquer outra IA externa para consertar o texto dele de forma automática.
O prompt que você gerar DEVE incluir comandos rigorosos para:
- Remover os clichês, marcas d'água e circularidades específicas que você encontrou.
- Ajustar a densidade do texto para um tom acadêmico sênior humano.
- Corrigir os erros de ABNT identificados.
*Nota: Coloque esse prompt dentro de um bloco de citação ou código para que o usuário saiba que é a área copiável.*

**Score de Risco Semântico**: (Nota de 0 a 10, onde 10 é altíssima probabilidade de IA)

Trecho a analisar:
{text[:3000]}
"""
    
    evaluations = []
    futures = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Prepara a chamada do Gemini
        if getattr(config, 'USE_GEMINI', False) and model_choice in ["todos", "gemini"]:
            client = genai.Client(api_key=config.GEMINI_API_KEY)
            futures.append(executor.submit(fetch_gemini, client, prompt))
            
        # Prepara as chamadas da NVIDIA
        if getattr(config, 'USE_NVIDIA', False) and model_choice in ["todos", "llama", "deepseek"]:
            try:
                client_nv = OpenAI(
                    base_url="https://integrate.api.nvidia.com/v1",
                    api_key=config.NVIDIA_API_KEY
                )
                
                models_to_run = []
                if model_choice == "todos":
                    models_to_run = getattr(config, 'NVIDIA_MODELS', [])
                elif model_choice == "llama":
                    models_to_run = ['meta/llama-3.2-11b-vision-instruct']
                elif model_choice == "deepseek":
                    models_to_run = ['deepseek-ai/deepseek-v4-pro-0813']
                    
                for model_name in models_to_run:
                    futures.append(executor.submit(fetch_nvidia, client_nv, model_name, prompt))
            except Exception as e:
                evaluations.append(f"### 🟢 Erro Geral na Conexão NVIDIA\n\n**Erro:** {e}")

        # Aguarda todos terminarem e pega o resultado
        for future in futures:
            evaluations.append(future.result())

    return "\n\n---\n\n".join(evaluations)
