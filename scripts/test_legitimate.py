import requests
import time
import psycopg2

def test_web_server():
    """Effettua richieste HTTP legittime al web server"""
    print("Eseguo richieste legittime al web server...")
    for _ in range(5):
        try:
            response = requests.get('http://web')
            print(f"Status code: {response.status_code}")
            time.sleep(1)
        except Exception as e:
            print(f"Errore nella richiesta HTTP: {e}")

def test_database():
    """Effettua query legittime al database"""
    print("Eseguo query legittime al database...")
    try:
        # psycopg2.connect() crea una connessione al database PostgreSQL
        conn = psycopg2.connect(
            dbname="testdb",
            user="testuser",
            password="testpass",
            host="db"
        )
        # Crea un cursore per eseguire query
        cur = conn.cursor()

        cur.execute("SELECT * FROM users;")

        # Recupera tutti i risultati
        results = cur.fetchall()
        print(f"Risultati query: {results}")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Errore nella connessione al database: {e}")

if __name__ == "__main__":
    test_web_server()
    test_database()