# ./web-server/Dockerfile
FROM nginx:alpine

# Copia la configurazione di Nginx
COPY nginx.conf /etc/nginx/nginx.conf
# Copia il file index.html
COPY index.html /usr/share/nginx/html/

# Espone la porta 80
EXPOSE 80