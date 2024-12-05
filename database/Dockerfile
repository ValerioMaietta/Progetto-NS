FROM postgres:13

# Copia lo script di inizializzazione
COPY init.sql /docker-entrypoint-initdb.d/

# Espone la porta standard di PostgreSQL
EXPOSE 5432