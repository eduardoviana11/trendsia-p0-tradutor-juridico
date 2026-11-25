"""Versão básica do Tradutor de Juridiquês via CLI integrado ao Ollama."""

import os

import requests
import urllib3
from dotenv import load_dotenv

PROMPT_SISTEMA = (
    "Você é um assistente especializado em traduzir trechos jurídicos "
    "(\"juridiquês\") de contratos ou termos de uso para linguagem simples e "
    "acessível a uma pessoa comum, em português do Brasil.\n"
    "Regras obrigatórias:\n"
    "1. Resuma a explicação em no máximo 3 linhas curtas e diretas.\n"
    "2. Explique na prática direitos, deveres, cobranças, prazos, multas ou "
    "riscos presentes no texto.\n"
    "3. Não invente informações, valores ou cláusulas que não estejam no "
    "trecho fornecido.\n"
    "4. Responda sem jargão jurídico e sem formatação excessiva."
)

AVISO_LEGAL = (
    "Aviso: Esta tradução tem caráter meramente informacional e preliminar "
    "e não substitui orientação jurídica profissional."
)


def main() -> None:
    """Lê uma cláusula jurídica pelo terminal e exibe o resumo via Ollama."""
    load_dotenv()

    ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
    ollama_model = os.getenv("OLLAMA_MODEL", "qwen3.5:9b-q4_K_M")
    verify_ssl = os.getenv("LLM_VERIFY_SSL", "true").strip().lower() == "true"

    # Suprime avisos apenas quando o servidor usa certificado SSL autogerado.
    if not verify_ssl:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print("=== Tradutor de Juridiquês (Versão Básica) ===")
    print("Cole o trecho ou cláusula do contrato abaixo.")
    print("Pressione Enter em uma linha vazia para enviar:\n")

    linhas = []
    while True:
        try:
            linha = input()
        except EOFError:
            break
        if linha == "":
            break
        linhas.append(linha)

    texto_juridico = "\n".join(linhas)

    url = f"{ollama_host}/api/chat"
    payload = {
        "model": ollama_model,
        "messages": [
            {"role": "system", "content": PROMPT_SISTEMA},
            {"role": "user", "content": texto_juridico},
        ],
        "stream": False,
    }

    print("\nTraduzindo trecho...")
    resposta = requests.post(url, json=payload, verify=verify_ssl)
    resposta.raise_for_status()

    dados = resposta.json()
    traducao = dados["message"]["content"].strip()

    print("\n--- Tradução Simplificada ---")
    print(traducao)
    print(f"\n{AVISO_LEGAL}")


if __name__ == "__main__":
    main()
