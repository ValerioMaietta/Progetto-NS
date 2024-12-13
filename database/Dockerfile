# Usa l'immagine ufficiale di PostgreSQL
FROM postgres:13-alpine

# Copia lo script di inizializzazione
COPY init.sql /docker-entrypoint-initdb.d/

# Esponi la porta standard di PostgreSQL
EXPOSE 5432