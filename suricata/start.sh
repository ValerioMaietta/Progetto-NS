# ./suricata/start.sh
#!/bin/bash

# Configura l'interfaccia di rete
ip link set eth0 up
ip link set eth0 promisc on

# Avvia Suricata con le opzioni corrette
exec suricata -c /etc/suricata/suricata.yaml --af-packet $SURICATA_OPTIONS