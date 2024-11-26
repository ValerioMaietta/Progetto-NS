# Usa Python come base per poter eseguire richieste HTTP
FROM python:3.9-slim

# Installa utility di rete necessarie
RUN apt-get update && apt-get install -y \
    # Per effettuare richieste HTTP uso curl
    curl \
    # Per testare la connettività faccio un ping
    iputils-ping \
    # Per troubleshooting di rete uso i net tools
    net-tools \
    && rm -rf /var/lib/apt/lists/*  # Pulizia per ridurre dimensione immagine

# Directory di lavoro per i nostri script
WORKDIR /app

# Mantieni il container in esecuzione
CMD ["/bin/bash"]