FROM docker.elastic.co/elasticsearch/elasticsearch:7.14.0

# Configurazione di base per un nodo singolo
ENV discovery.type=single-node
ENV ES_JAVA_OPTS="-Xms512m -Xmx512m"

EXPOSE 9200 9300