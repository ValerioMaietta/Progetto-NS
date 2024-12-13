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

# Copia i file di configurazione
COPY suricata.yaml /etc/suricata/
COPY rules/ /etc/suricata/rules/

# Crea directory per i log
RUN mkdir -p /var/log/suricata

# Avvia Suricata
CMD ["suricata", "-c", "/etc/suricata/suricata.yaml", "--af-packet"]