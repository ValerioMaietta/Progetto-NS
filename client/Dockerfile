FROM python:3.9-slim

# Installa nmap e altre dipendenze di sistema necessarie
RUN apt-get update && \
    apt-get install -y nmap && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Crea la directory per gli script
WORKDIR /scripts

# Installa le librerie Python necessarie
RUN pip install requests urllib3

# Mantieni il container in esecuzione
CMD ["tail", "-f", "/dev/null"]