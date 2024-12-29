-- Crea una tabella di esempio
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100)
);

-- Inserisce alcuni dati di esempio
INSERT INTO users (username, password, email) 
VALUES 
    ('admin', 'admin123', 'admin@example.com'),
    ('user1', 'pass123', 'user1@example.com');