-- ./database/init.sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR(100) NOT NULL
);

-- Inserisce alcuni dati di esempio
INSERT INTO users (username, email, password_hash) VALUES
    ('admin', 'admin@example.com', 'hash1'),
    ('user1', 'user1@example.com', 'hash2'),
    ('user2', 'user2@example.com', 'hash3');