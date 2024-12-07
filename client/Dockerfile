# Usa Ubuntu come base
FROM ubuntu:20.04

# Evita interazioni durante l'installazione
ENV DEBIAN_FRONTEND=noninteractive

# Installa le dipendenze necessarie
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nmap \
    curl \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Crea la directory per gli script
WORKDIR /app

# Copia i file necessari
COPY scripts/requirements.txt .
COPY scripts/traffic_generator.py .

# Installa le dipendenze Python
RUN pip3 install -r requirements.txt

# Rendi eseguibile lo script
RUN chmod +x traffic_generator.py

# Script di avvio
COPY scripts/start.sh /start.sh
RUN chmod +x /start.sh

# Usa lo script di avvio come entrypoint
ENTRYPOINT ["/start.sh"]