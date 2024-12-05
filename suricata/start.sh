#!/bin/bash

# Configura l'interfaccia di rete
ip link set eth0 up
ip link set eth0 promisc on

# Avvia Suricata con configurazioni specifiche
exec suricata -c /etc/suricata/suricata.yaml --pidfile /var/run/suricata.pid -i eth0 --init-errors-fatal