FROM python:3.9-slim

# Installa nmap e altre dipendenze di sistema necessarie
RUN apt-get update && \
    apt-get install -y nmap && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Installa le dipendenze Python necessarie
RUN pip install requests psycopg2-binary

# Crea la directory per gli script
RUN mkdir /scripts

# Imposta la directory di lavoro
WORKDIR /scripts

# Mantieni il container in esecuzione
CMD ["tail", "-f", "/dev/null"]