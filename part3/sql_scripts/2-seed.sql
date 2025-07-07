-- Insert administrator user
-- Replace password_hash with a real bcrypt hash if using authentication
INSERT INTO users (username, email, password_hash, role, is_active)
VALUES (
    'admin',
    'admin@example.com',
    '$2b$12$K2C8Lx3PQx7lLijX6KTXeeyZKmfrqlAVYxDOqNBN6B.xHP7DumG.C',
    'admin',
    1
);

-- Insert amenities
INSERT INTO amenities (name) VALUES ('Wi-Fi');
INSERT INTO amenities (name) VALUES ('Pool');
INSERT INTO amenities (name) VALUES ('Parking');
INSERT INTO amenities (name) VALUES ('Air Conditioning');
INSERT INTO amenities (name) VALUES ('Gym');

-- Optional: Insert a sample place owned by admin (user_id = 1)
INSERT INTO places (name, description, owner_id)
VALUES (
    'Modern Beach Villa',
    'A beautiful beachfront villa with stunning views and modern amenities.',
    1
);

-- Optional: Add reviews
INSERT INTO reviews (cont

