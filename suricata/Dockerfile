# Usa Ubuntu come base
FROM ubuntu:20.04

# Evita interazioni durante l'installazione
ENV DEBIAN_FRONTEND=noninteractive

# Installa Suricata e dipendenze
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:oisf/suricata-stable \
    && apt-get update \
    && apt-get install -y suricata \
    && rm -rf /var/lib/apt/lists/*

# Crea directory per i log e le regole
RUN mkdir -p /var/log/suricata /etc/suricata/rules

# Copia i file di configurazione
COPY suricata.yaml /etc/suricata/
COPY rules/custom.rules /etc/suricata/rules/

# Imposta i permessi
RUN chmod -R 755 /var/log/suricata && \
    chmod -R 755 /etc/suricata

# Avvia Suricata
CMD ["suricata", "-c", "/etc/suricata/suricata.yaml", "--af-packet", "-v"]