from flask import Flask, request, render_template

# Inizializza l'applicazione Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    # Gestisce le richieste POST (invio form)
    if request.method == 'POST':
        # Recupera i dati dal form
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Stampa le credenziali ricevute (solo per demo)
        print(f"Login attempt - Username: {username}, Password: {password}")
        return "Login attempt recorded"
    
    # Per richieste GET, mostra il form di login
    return render_template('login.html')

if __name__ == '__main__':
    # Avvia il server sulla porta 80, accessibile da qualsiasi IP
    app.run(host='0.0.0.0', port=80)