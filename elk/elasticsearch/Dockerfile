FROM docker.elastic.co/elasticsearch/elasticsearch:7.14.0

USER root
RUN apk add --no-cache curl

# Configurazione di base per un nodo singolo
ENV discovery.type=single-node

COPY config/elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

# Imposta i permessi corretti
USER root
RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/config/elasticsearch.yml
USER elasticsearch