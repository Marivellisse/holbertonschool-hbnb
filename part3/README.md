# HBnB - Part 3: Persistence, Authentication & Authorization

This is the third part of the **HBnB project**, where we transition from in-memory storage to a persistent database using **SQLAlchemy**. We also implement user authentication using JWT and secure access control using role-based permissions (`user`, `admin`).

---

## 🚀 Features Implemented

* SQLAlchemy database integration (SQLite)
* JWT-based login and access token authentication
* Role-based authorization (user/admin)
* Secure password storage using bcrypt
* CRUD operations for:

  * Users
  * Places
  * Reviews
  * Amenities
* Database schema generation using raw SQL scripts
* Entity-Relationship diagram for database visualization

---

## 🗂️ Project Structure

```
part3/
﻿├── app/
│   ├── models/
│   ├── repository/
│   ├── facade/
│   ├── routes/
│   ├── settings.py
│   └── main.py
│
├── sql_scripts/
│   ├── 1-schema.sql
│   └── 2-seed.sql
│
├── diagrams/
│   └── er_diagram.mmd
│   └── er_diagram.png
│
├── hbnb.db
└── README.md
```

---

## 🛠️ Setup Instructions

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create and seed the database:

```bash
sqlite3 hbnb.db < sql_scripts/1-schema.sql
sqlite3 hbnb.db < sql_scripts/2-seed.sql
```

3. Run the app:

```bash
export FLASK_APP=app.main
export FLASK_ENV=development
flask run
```

4. Test endpoints (login, CRUD) using Postman or cURL.

---

## 🔐 Admin Credentials (Seeded)

```json
{
  "email": "admin@example.com",
  "password": "admin123"
}
```

Use this to authenticate and receive a JWT token.

---

## 📊 ER Diagram

You can view the entity relationships for the application below:

### Embedded PNG (GitHub-compatible)

> 🖼️ **Place your exported diagram image here**: `part3/diagrams/er_diagram.png`

```markdown
![ER Diagram](./diagrams/er_diagram.png)
```

Or you can embed it in Markdown directly (if GitHub supports Mermaid rendering):

### Mermaid.js

```mermaid
erDiagram
    users {
        INTEGER id PK
        TEXT username
        TEXT email
        TEXT password_hash
        TEXT role
        BOOLEAN is_active
        DATETIME created_at
        DATETIME updated_at
    }

    places {
        INTEGER id PK
        TEXT name
        TEXT description
        INTEGER owner_id FK
        DATETIME created_at
        DATETIME updated_at
    }

    reviews {
        INTEGER id PK
        TEXT content
        INTEGER rating
        INTEGER user_id FK
        INTEGER place_id FK
        DATETIME created_at
        DATETIME updated_at
    }

    amenities {
        INTEGER id PK
        TEXT name
        DATETIME created_at
        DATETIME updated_at
    }

    place_amenity {
        INTEGER place_id PK, FK
        INTEGER amenity_id PK, FK
    }

    users ||--o{ places : owns
    users ||--o{ reviews : writes
    places ||--o{ reviews : has
    places ||--o{ place_amenity : has
    amenities ||--o{ place_amenity : linked_to
```

---

## 📌 Resources

* Flask
* Flask-SQLAlchemy
* Flask-JWT-Extended
* Flask-Bcrypt
* SQLite3
* Mermaid.js

---

## 👩‍💻 Author

Developed by [Marivellisse García Lebrón](https://www.linkedin.com/in/marivellisse-garcia),
as part of Holberton School’s full-stack curriculum.

---

