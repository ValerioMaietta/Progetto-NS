# ./client/scripts/normal_traffic.py
import requests
import time
import random

def generate_normal_traffic():
    """
    Genera traffico HTTP normale verso il web server
    """
    while True:
        try:
            # Effettua richieste GET al web server
            response = requests.get('http://web:80')
            print(f"Normal request sent. Status: {response.status_code}")
            
            # Attende un intervallo casuale tra 1 e 5 secondi
            time.sleep(random.uniform(1, 5))
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    generate_normal_traffic()