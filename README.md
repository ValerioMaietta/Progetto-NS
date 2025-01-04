# Progetto Network Security

## Panoramica

Questo progetto implementa un sistema di monitoraggio della sicurezza di rete utilizzando container Docker. Include:

- Server Web (Nginx)
- Database (PostgreSQL)
- IDS di Rete (Suricata)
- Stack ELK (Elasticsearch, Kibana) per la visualizzazione dei log
- Client di test per le prove di sicurezza

## Prerequisiti

- Docker
- Docker Compose
- Almeno 4GB di RAM disponibile
- Porte 8080 (web), 5601 (Kibana) e 9200 (Elasticsearch) disponibili

## Installazione e Configurazione

1. Clonare il repository:

```bash
git clone https://github.com/ValerioMaietta/Progetto-NS.git
cd Progetto-NS
```

2. Avviare il sistema:

```bash
docker-compose up --build
```

3. Attendere che tutti i servizi si avviino (potrebbe richiedere alcuni minuti al primo avvio)

## Configurazione

### Configurazione della Visualizzazione in Kibana

1. Accedere a Kibana (http://localhost:5601)
2. Creare il pattern di indice "suricata-\*"
3. Cliccare su Visualize e creare le visualizzazioni da utilizzare per la creazione della dashboard per il monitoraggio degli alert

### Esecuzione dei Test di Sicurezza

```bash
# Esegui gli script di test dal container client
docker-compose exec client python /scripts/test_legitimate.py
docker-compose exec client python /scripts/test_malicious.py
```

## Monitoraggio

Il sistema rileva e registra vari eventi di sicurezza tra cui:

- Tentativi di port scanning
- Tentativi di SQL injection
- Tentativi di accesso non autorizzato
- Attacchi DDoS
- Tentativi di login sospetti

I log possono essere visualizzati in:

- Dashboard di Kibana
- Log grezzi nella cartella ./logs
- Alert di Suricata in logs/fast.log

## Considerazioni sulla Sicurezza

- Questo è un ambiente di test/monitoraggio
- Vengono utilizzate credenziali di default per scopo dimostrativo
- Non è raccomandato per l'uso in produzione senza un appropriato rafforzamento della sicurezza
- Modificare le regole in suricata/rules/custom.rules per le proprie esigenze specifiche
