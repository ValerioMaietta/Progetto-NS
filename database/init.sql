-- Crea una tabella di esempio per i test
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserisce alcuni dati di esempio
INSERT INTO users (username, email) VALUES
    ('test_user1', 'user1@example.com'),
    ('test_user2', 'user2@example.com'),
    ('admin', 'admin@example.com');

-- Crea una tabella per i log delle attività
CREATE TABLE activity_logs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    action VARCHAR(100) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);