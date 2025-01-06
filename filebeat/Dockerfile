FROM docker.elastic.co/beats/filebeat:7.9.3
COPY filebeat.yml /usr/share/filebeat/filebeat.yml
USER root
# Imposta i permessi corretti per root
RUN chown root:filebeat /usr/share/filebeat/filebeat.yml
# Rimuove permessi di scrittura per gli altri
RUN chmod go-w /usr/share/filebeat/filebeat.yml