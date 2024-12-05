FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Installazione di Suricata e dipendenze
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:oisf/suricata-stable && \
    apt-get update && \
    apt-get install -y \
    suricata \
    iproute2 \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Crea directory per i log
RUN mkdir -p /var/log/suricata && \
    chown -R root:root /var/log/suricata

# Copia dei file di configurazione
COPY config/suricata.yaml /etc/suricata/
COPY config/rules/custom.rules /etc/suricata/rules/

# Script di avvio
COPY start.sh /
RUN chmod +x /start.sh

ENTRYPOINT ["/start.sh"]