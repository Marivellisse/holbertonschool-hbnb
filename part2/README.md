# HBnB Evolution - Part 2: Business Logic and API

## 📘 Overview

This part of the HBnB project focuses on bringing the previously documented design to life by implementing the core business logic and RESTful API using Python, Flask, and flask-restx. It covers the construction of the application's Presentation and Business Logic layers using modular architecture and the facade pattern.

---

## 📁 Project Structure

```
part2/
├── app/
│   ├── main.py
│   ├── presentation/
│   │   └── routes/
│   ├── business/
│   │   └── models/
│   ├── persistence/
├── requirements.txt
└── README.md
```

- `presentation/`: Contains all Flask API endpoints (Presentation Layer).
- `business/`: Core classes and relationships (Business Logic Layer).
- `persistence/`: Temporary in-memory storage (will be replaced by DB in Part 3).

---

## 🧱 Implemented Layers

### 🔹 Business Logic Layer
- Defines models: `User`, `Place`, `Review`, `Amenity`
- Relationships and data validation logic
- Centralized communication via a `Facade` class

### 🔹 Presentation Layer
- Built using `Flask` and `flask-restx`
- RESTful endpoints for each model (CRUD)
- Swagger UI auto-generated for testing and documentation

---

## 🎯 Objectives

- [x] Create modular project structure
- [x] Implement business models and logic
- [x] Apply the facade pattern to connect layers
- [x] Build RESTful endpoints for `User`, `Place`, `Review`, `Amenity`
- [x] Support in-memory persistence with UUIDs and timestamps
- [x] Test with Swagger, Postman, and cURL

---

## 🔌 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the API server:
   ```bash
   python app/main.py
   ```

3. Access Swagger UI:
   ```
   http://localhost:5000/
   ```

---

## 🧪 Testing

- Use **Postman** or **cURL** to test endpoints.
- Use **Swagger UI** for interactive testing and docs.
- All endpoints are designed to handle edge cases and return proper status codes.

---

## 🧰 Technologies Used

- Python 3.x
- Flask
- flask-restx
- UUID4 for object identifiers
- In-memory repository (Part 3 will use SQLAlchemy)

---

## 🔒 Coming Soon in Part 3

- JWT Authentication
- Role-based Access Control (RBAC)
- SQL-based Persistence Layer

---

## 📂 Repository

This code belongs to:
`holbertonschool-hbnb/part2`

> Developed by [Marivellisse Garcia] — Holberton School 🇵🇷

