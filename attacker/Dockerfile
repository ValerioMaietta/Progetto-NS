# Usa Golang Alpine come base leggera
FROM golang:1.21.3-alpine

# Installa le dipendenze necessarie
RUN apk add --no-cache \
    # Shell per interazione
    bash \
    # Strumenti di compilazione
    build-base \
    # Libreria per cattura pacchetti (fondamentali per bettercap)
    libpcap-dev \
    # Libreria per manipolazione pacchetti (fondamentali per bettercap)
    libnetfilter_queue-dev \
    # Libreria che serve a Bettercap
    libusb-dev \
    # Per clonare Bettercap
    git \
    # Per compilare
    make \
    # Compilatore
    gcc \
    # Librerie di sviluppo
    musl-dev \
    # Header del kernel
    linux-headers \
    # Certificati SSL
    ca-certificates \
    # Dati timezone
    tzdata \
    # Per eventuali script proxy
    npm

# Imposto il PATH per Go
ENV PATH="/usr/local/go/bin:${PATH}"

# Installa Bettercap dalla sorgente
RUN git clone https://github.com/bettercap/bettercap.git /tmp/bettercap && \
    cd /tmp/bettercap && \
    make build && \
    make install

# Crea directory per logs e caplets
RUN mkdir -p /root/logs /usr/local/share/bettercap/caplets

WORKDIR /root

# Espone porte per interfaccia web e proxy
EXPOSE 8081 8080

# Copia configurazioni e script
COPY caplets/ /usr/local/share/bettercap/caplets/
COPY start.sh /root/start.sh
RUN chmod +x /root/start.sh

# Avvia Bettercap
CMD ["/root/start.sh"]