import requests
import time
import subprocess

def simulate_unauthorized_access():
    """Simula tentativi di accesso non autorizzato"""
    print("Simulazione accessi non autorizzati...")
    malicious_urls = [
        'http://172.18.0.2:80/admin',
        'http://172.18.0.2:80/login?username=admin&password=1234',
        'http://172.18.0.2:80/config'
    ]
    
    headers = {
        'User-Agent': 'MaliciousScanner/1.0'
    }
    
    for url in malicious_urls:
        for _ in range(3):  # Prova ogni URL più volte
            try:
                print(f"Tentativo di accesso a {url}")
                response = requests.get(url, headers=headers)
                print(f"Status code: {response.status_code}")
                time.sleep(1)
            except Exception as e:
                print(f"Errore: {e}")

def simulate_port_scan():
    """Simula una scansione delle porte"""
    print("\nSimulazione port scanning...")
    try:
        for port in [80, 8080, 443, 22]:
            print(f"Scanning port {port} su 172.18.0.2")
            subprocess.run(["nmap", "-sS", "-p", str(port), "172.18.0.2"], 
                         check=True, capture_output=True)
            time.sleep(1)
    except Exception as e:
        print(f"Errore durante il port scanning: {e}")

if __name__ == "__main__":
    print("Iniziando i test...")
    simulate_port_scan()
    print("\nAttendendo 5 secondi prima dei test HTTP...")
    time.sleep(5)
    simulate_unauthorized_access()
    print("\nTest completati.")