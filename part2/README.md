
# HBnB Evolution - Part 2

## 📌 Project Overview

HBnB Evolution is a RESTful API application designed to simulate a simplified AirBnB-like platform. It allows users to register, create places, add amenities, leave reviews, and interact with property data through a structured layered architecture using Flask and Flask-RESTx.

This part of the project focuses on implementing:

- REST API endpoints for `User`, `Place`, `Amenity`, and `Review` entities
- Business logic abstraction via a Facade pattern
- Input validation
- Swagger documentation
- Testing using `cURL` and manual API interaction

---

## 🧱 Architecture

The application follows a 3-layer structure:

- **Presentation Layer**: Uses Flask-RESTx to define namespaces and endpoints (routes).
- **Business Logic Layer**: Contains core logic in the `services/facade.py` and model validations.
- **Data Layer**: For this version, data is stored in in-memory dictionaries (`USERS`, `PLACES`, `REVIEWS`, `AMENITIES`).

---

## 🚀 How to Run

### Step 1: Install Dependencies

```bash
pip install flask flask-restx
```

### Step 2: Run the Application

```bash
PYTHONPATH=. python3 app/main.py
```

The API will be available at:  
**http://127.0.0.1:5001/api/v1**

Swagger Docs:  
**http://127.0.0.1:5001/api/v1/**

---

## 📘 Available Endpoints

### 👤 Users

- `POST /users/` - Create a new user
- `GET /users/` - List all users

### 🏠 Places

- `POST /places/` - Create a new place
- `GET /places/` - List all places
- `GET /places/<place_id>` - Get place by ID
- `PUT /places/<place_id>` - Update place

### 🛋️ Amenities

- `POST /amenities/` - Create a new amenity
- `GET /amenities/` - List all amenities
- `GET /amenities/<amenity_id>` - Get amenity by ID

### 📝 Reviews

- `POST /reviews/` - Create a new review
- `GET /reviews/` - List all reviews
- `GET /reviews/<review_id>` - Get review by ID
- `PUT /reviews/<review_id>` - Update review
- `DELETE /reviews/<review_id>` - Delete review
- `GET /places/<place_id>/reviews` - List reviews for a place

---

## ✅ Example Test with cURL

Create a user:

```bash
curl -X POST http://127.0.0.1:5001/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{"first_name": "Ana", "last_name": "Martínez", "email": "ana@example.com", "password": "1234"}'
```

Create a place:

```bash
curl -X POST http://127.0.0.1:5001/api/v1/places/ \
-H "Content-Type: application/json" \
-d '{"title": "Beachfront Villa", "description": "Relaxing vibes", "price": 200, "latitude": 18.45, "longitude": -66.08, "owner_id": "USER_ID", "amenities": []}'
```

Create a review:

```bash
curl -X POST http://127.0.0.1:5001/api/v1/reviews/ \
-H "Content-Type: application/json" \
-d '{"text": "Amazing stay!", "rating": 5, "user_id": "USER_ID", "place_id": "PLACE_ID"}'
```

---

## 🧪 Validation Rules

- **Users**: `email`, `first_name`, and `last_name` must be provided and valid.
- **Places**: `title`, `price`, `latitude`, and `longitude` are required and validated.
- **Reviews**: Must include `text`, `rating` (1–5), `user_id`, and `place_id`.

---

## 👩‍💻 Technologies

- Python 3
- Flask + Flask-RESTx
- RESTful APIs
- In-memory Data Storage
- Swagger UI Documentation

---

## 📎 Notes

- This application is for development/demo purposes.
- No persistent database is used—data resets on restart.
- Error handling and validations are basic and extendable.

---

## ✨ Authors

- Marivellisse Garcia Lebron


Holberton School – Cohort 26 
Puerto Rico, 2025

