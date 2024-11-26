#!/bin/bash

# Crea directory per i log se non esiste
mkdir -p /root/logs

# Assicurati che i file di log esistano
touch /root/logs/bettercap_events.log
touch /root/logs/sniffed_traffic.pcap

# Genera una password casuale per l'interfaccia web
RANDOM_PASSWORD=$(openssl rand -hex 32)
echo "Password interfaccia web: $RANDOM_PASSWORD" > /root/logs/web_credentials.txt

# Avvia Bettercap con la configurazione
bettercap -caplet mitm-advanced.cap -eval "set api.rest.password $RANDOM_PASSWORD"

# Se Bettercap si interrompe, mostra i log
tail -f /root/logs/bettercap_events.log