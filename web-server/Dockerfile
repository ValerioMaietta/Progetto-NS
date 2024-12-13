# Usa l'immagine ufficiale di Nginx
FROM nginx:alpine

# Copia la configurazione personalizzata di Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copia il file index.html
COPY index.html /usr/share/nginx/html/

# Esponi la porta 80
EXPOSE 80

# Avvia Nginx in foreground
CMD ["nginx", "-g", "daemon off;"]