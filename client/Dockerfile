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
    postgresql \
    postgresql-contrib \
    libpq-dev \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Crea la directory per gli script
WORKDIR /app

# Copia i file necessari
COPY scripts/requirements.txt .
COPY scripts/traffic_generator.py .

# Installa le dipendenze Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Mantieni il container in esecuzione
CMD ["tail", "-f", "/dev/null"]