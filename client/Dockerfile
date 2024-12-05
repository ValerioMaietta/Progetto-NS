FROM python:3.9-slim

# Installa le dipendenze necessarie
RUN apt-get update && apt-get install -y \
    nmap \
    && rm -rf /var/lib/apt/lists/*

# Installa le librerie Python necessarie
RUN pip install requests python-nmap

# Copia gli script
COPY scripts/ /scripts/

WORKDIR /scripts

CMD ["tail", "-f", "/dev/null"]