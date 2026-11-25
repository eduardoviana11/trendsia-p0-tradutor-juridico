FROM python:3.12.7-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    OLLAMA_HOST=https://llm-internal.softex:9001 \
    OLLAMA_MODEL=qwen3.5:9b-q4_K_M \
    LLM_VERIFY_SSL=false

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["sh", "-c", "TEXTO=\"${TEXTO_JURIDICO:-CLÁUSULA 8ª — DA RESCISÃO ANTECIPADA: O CONTRATANTE poderá resilir unilateralmente o presente instrumento mediante comunicação prévia por escrito com antecedência mínima de 30 (trinta) dias, ficando sujeito à multa compensatória equivalente a 20% (vinte por cento) do saldo remanescente das parcelas vincendas.}\"; echo \"Entrada enviada:\"; echo \"$TEXTO\"; echo \"\"; printf '%s\\n\\n' \"$TEXTO\" | python -u main.py"]
