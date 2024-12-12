# ./suricata/Dockerfile
FROM ubuntu:20.04

# Evita interazioni durante l'installazione
ENV DEBIAN_FRONTEND=noninteractive

# Installa le dipendenze necessarie e Suricata
RUN apt-get update && \
    apt-get install -y software-properties-common curl gpg && \
    add-apt-repository ppa:oisf/suricata-stable && \
    apt-get update && \
    apt-get install -y \
    suricata \
    iproute2 \
    && rm -rf /var/lib/apt/lists/*

# Crea le directory necessarie
RUN mkdir -p /var/log/suricata /var/run/suricata /etc/suricata/rules

# Copia i file di configurazione
COPY config/suricata.yaml /etc/suricata/
COPY config/rules/custom.rules /etc/suricata/rules/

# Imposta i permessi corretti
RUN chmod 750 /var/log/suricata && \
    chmod 750 /var/run/suricata && \
    chmod 640 /etc/suricata/suricata.yaml && \
    chmod 640 /etc/suricata/rules/custom.rules

# Script di avvio
COPY start.sh /
RUN chmod +x /start.sh

# Usa lo script di avvio invece del comando diretto
CMD ["/start.sh"]