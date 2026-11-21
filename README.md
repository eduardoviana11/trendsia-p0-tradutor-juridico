# Tradutor de Juridiquês — Versão Básica (`p0-basico`)

Aplicação de linha de comando (CLI) em Python para traduzir trechos complexos de contratos e termos de uso em resumos simples e acessíveis de até três linhas, utilizando um modelo de linguagem (LLM) via API REST do Ollama.

---

## 1. Problema, Público-Alvo e Justificativa do Uso de LLM

- **Problema:** Pessoas comuns frequentemente precisam aceitar contratos ou termos de uso sem compreender claramente os direitos, deveres, cobranças, prazos, multas ou riscos descritos em linguagem jurídica complexa ("juridiquês").
- **Público-alvo:** Consumidores e usuários leigos que desejam uma explicação preliminar e direta de cláusulas contratuais antes de tomar decisões ou buscar análise especializada.
- **Por que usar um LLM:** Textos jurídicos variam amplamente em vocabulário, estrutura frasal e contexto. Regras fixas ou expressões regulares não conseguem interpretar o sentido prático das cláusulas nem parafraseá-las em linguagem natural acessível.

---

## 2. Aviso Ético e de Escopo

> **Importante:** Por envolver direitos, obrigações e contratos, esta aplicação tem papel **exclusivamente informacional e preliminar**. A saída apresentada no terminal **não substitui orientação jurídica profissional** prestada por advogado ou defensoria.

---

## 3. Estrutura do Projeto e Tecnologias

Arquivos da versão básica:

```text
trendsia-p0-tradutor-juridico/
├── .env.example      # Modelo de variáveis de ambiente (sem dados sensíveis)
├── .gitignore        # Exclusões do Git (.env, .venv/, cache Python)
├── main.py           # Núcleo funcional da versão básica (CLI + chamada REST)
├── README.md         # Documentação de instalação, configuração e uso
└── requirements.txt  # Dependências Python com versões fixadas
```

Tecnologias utilizadas:

- **Python `3.12.7`**
- **Ollama API REST** (`POST /api/chat` sem streaming)
- **`requests==2.32.3`** para requisições HTTP/HTTPS
- **`python-dotenv==1.0.1`** para carregamento de configuração via `.env`

---

## 4. Instalação Passo a Passo

1. **Clonar o repositório e acessar a pasta do projeto:**

   ```bash
   git clone https://github.com/eduardoviana11/trendsia-p0-tradutor-juridico.git
   cd trendsia-p0-tradutor-juridico
   ```

2. **Criar o ambiente virtual Python (`3.12.7`):**

   - **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - **Linux/macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Instalar as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

---

## 5. Configuração das Variáveis de Ambiente (`.env`)

1. Copie o arquivo modelo `.env.example` para `.env`:

   - **Windows (PowerShell):**
     ```powershell
     Copy-Item .env.example .env
     ```
   - **Linux/macOS:**
     ```bash
     cp .env.example .env
     ```

2. Ajuste as variáveis no `.env` conforme o servidor Ollama disponível:

   | Variável | Descrição | Exemplo |
   | :--- | :--- | :--- |
   | `OLLAMA_HOST` | URL base do servidor Ollama. Use `http://localhost:11434` para Ollama local ou `https://llm-internal.softex:9001` no ambiente institucional (rede interna `llm-network`). | `http://localhost:11434` |
   | `OLLAMA_MODEL` | Tag exata do modelo instalado no servidor Ollama em uso. | `qwen3.5` |
   | `LLM_VERIFY_SSL` | Define se o certificado SSL será validado. Use `false` para o servidor institucional (certificado SSL autogerado) e `true` quando houver certificado válido. | `false` |

---

## 6. Como Executar (`python main.py`)

Com o ambiente virtual ativado e o servidor Ollama acessível, execute:

```bash
python main.py
```

Cole o trecho contratual no terminal (suporta múltiplas linhas) e pressione **Enter** em uma linha vazia para enviar.

### Exemplo fictício de entrada e saída

> Nota: O exemplo abaixo utiliza uma cláusula fictícia criada apenas para fins de demonstração.

**Entrada (colada no terminal):**

```text
CLÁUSULA 8ª — DA RESCISÃO ANTECIPADA: O CONTRATANTE poderá resilir unilateralmente o presente instrumento mediante comunicação prévia por escrito com antecedência mínima de 30 (trinta) dias, ficando sujeito à multa compensatória equivalente a 20% (vinte por cento) do saldo remanescente das parcelas vincendas.
```

*(seguido de `Enter` em linha vazia)*

**Saída ilustrativa esperada:**

```text
--- Tradução Simplificada ---
Você pode cancelar o contrato antes do fim se avisar por escrito com pelo menos 30 dias de antecedência.
Ao cancelar antes do prazo, haverá uma multa de 20% sobre o valor das parcelas que ainda faltavam pagar.
O risco principal é pagar essa multa caso desista do serviço antes do término previsto.

Aviso: Esta tradução tem caráter meramente informacional e preliminar e não substitui orientação jurídica profissional.
```

---

## 7. Limitações Conhecidas da Versão Básica

- **Não bloqueia entrada vazia:** Se o usuário pressionar `Enter` sem digitar texto, a requisição ainda será enviada ao modelo.
- **Tratamento de erros mínimo:** Falhas de rede, servidor offline, URL incorreta ou resposta inesperada interrompem o script com erro padrão do Python/requests.
- **Dependência de servidor Ollama ativo:** Requer acesso a uma instância Ollama em execução (local ou na rede institucional) com o modelo configurado previamente baixado.
- **Parâmetros do modelo fixos:** Temperatura, limite de tokens e timeout ainda não são configuráveis externamente nesta versão.
- **Uso preliminar:** O resumo de até 3 linhas simplifica o texto e pode omitir nuances que exijam leitura completa ou apoio jurídico.

---

## 8. Segurança e Boas Práticas

- **Proteção de configuração:** O arquivo `.env` está listado no `.gitignore` e nunca deve ser versionado no Git. Não coloque senhas, tokens ou endereços privados em arquivos rastreados (`.env.example`, `main.py` ou `README.md`).
- **Privacidade dos dados:** Não insira documentos reais com dados pessoais (CPF, RG, endereço, dados bancários) ou informações sigilosas durante os testes; utilize apenas cláusulas fictícias ou trechos públicos genéricos.
