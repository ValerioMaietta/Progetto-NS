#!/bin/bash

# Attendi che gli altri servizi siano pronti
echo "Waiting for services to be ready..."
sleep 30

# Avvia il generatore di traffico
echo "Starting traffic generator..."
python3 /app/traffic_generator.py