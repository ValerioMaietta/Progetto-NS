FROM ubuntu:22.04

# Evita prompt interattivi durante l'installazione
ENV DEBIAN_FRONTEND=noninteractive

# Installa Suricata e dipendenze
RUN apt-get update && \
    apt-get install -y \
    suricata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crea le directory necessarie
RUN mkdir -p /var/log/suricata /etc/suricata/rules
RUN touch /var/log/suricata/fast.log \
    /var/log/suricata/eve.json \
    /var/log/suricata/suricata.log

# Modifica i permessi
RUN chmod 666 /var/log/suricata/fast.log \
    /var/log/suricata/eve.json \
    /var/log/suricata/suricata.log \
    && chmod -R 755 /var/log/suricata

# Copia la configurazione
COPY suricata.yaml /etc/suricata/suricata.yaml

# Comando di avvio
CMD ["suricata", "-c", "/etc/suricata/suricata.yaml", "-i", "eth0", "--init-errors-fatal"]
# L'opzione --init-errors-fatal specifica che qualsiasi errore durante la fase di inizializzazione
#deve essere trattato come fatale, causando il fallimento immediato dell'avvio del programma.