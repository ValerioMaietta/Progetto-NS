#!/usr/bin/env python3

import requests
import nmap
import time
import random
from scapy.all import *
import psycopg2
from datetime import datetime

def generate_normal_traffic(web_server_url):
    """Genera traffico web normale"""
    try:
        response = requests.get(web_server_url)
        print(f"Normal request to {web_server_url}: {response.status_code}")
    except Exception as e:
        print(f"Error generating normal traffic: {e}")

def scan_ports(target):
    """Esegue una scansione delle porte usando nmap"""
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-p 80,443,5432 -sS')
    print(f"Port scan completed on {target}")

def sql_injection_simulation(db_host):
    """Simula tentativi di SQL injection"""
    payloads = [
        "' OR '1'='1",
        "'; DROP TABLE users; --",
        "' UNION SELECT * FROM users; --"
    ]
    
    for payload in payloads:
        try:
            conn = psycopg2.connect(
                dbname="testdb",
                user="testuser",
                password="testpass",
                host=db_host
            )
            cur = conn.cursor()
            
            # Simula una query malevola
            query = f"SELECT * FROM users WHERE username = '{payload}'"
            print(f"Attempting SQL injection with payload: {payload}")
            
            # Non eseguiamo realmente la query per sicurezza
            # cur.execute(query)
            
        except Exception as e:
            print(f"SQL injection simulation error: {e}")
        finally:
            if 'conn' in locals():
                conn.close()

def main():
    WEB_SERVER = "http://web-server"
    DB_HOST = "database"
    
    while True:
        # Genera traffico normale
        generate_normal_traffic(WEB_SERVER)
        time.sleep(random.uniform(1, 5))
        
        # Occasionalmente esegue una scansione delle porte
        if random.random() < 0.2:
            scan_ports(WEB_SERVER)
        
        # Occasionalmente simula tentativi di SQL injection
        if random.random() < 0.1:
            sql_injection_simulation(DB_HOST)
        
        time.sleep(5)

if __name__ == "__main__":
    # Attendi che i servizi siano pronti
    time.sleep(30)
    main()