FROM ubuntu:20.04

# Evita interazioni durante l'installazione
ENV DEBIAN_FRONTEND=noninteractive

# Installa Suricata e le dipendenze
RUN apt-get update && apt-get install -y \
    suricata \
    && rm -rf /var/lib/apt/lists/*

# Copia i file di configurazione
COPY config/suricata.yaml /etc/suricata/
COPY config/rules/custom.rules /etc/suricata/rules/

# Avvia Suricata in modalità IDS
CMD ["suricata", "-c", "/etc/suricata/suricata.yaml", "-i", "eth0"]