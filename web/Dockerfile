FROM nginx:latest

# Installa apache2-utils per htpasswd
RUN apt-get update && \
    apt-get install -y apache2-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Crea la directory admin
RUN mkdir -p /usr/share/nginx/html/admin

# Copia i file HTML
COPY html/ /usr/share/nginx/html/

# Copia la configurazione di nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Crea il file .htpasswd con credenziali admin:admin123
RUN htpasswd -bc /etc/nginx/.htpasswd admin admin123

# Permessi corretti
RUN chmod 644 /etc/nginx/.htpasswd

EXPOSE 80