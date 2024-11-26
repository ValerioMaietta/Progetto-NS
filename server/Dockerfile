# Usa Python come base per il server web
FROM python:3.9-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file necessari
COPY server.py .
COPY templates/ ./templates/

# Installa Flask per il server web
RUN pip install flask

# Espone la porta 80 per il web server
EXPOSE 80

# Avvia il server
CMD ["python3", "server.py"]