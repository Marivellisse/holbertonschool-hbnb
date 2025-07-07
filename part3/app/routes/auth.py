# app/routes/auth.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.facade.user_facade import UserFacade

auth_bp = Blueprint('auth', __name__)
user_facade = UserFacade()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or not all(k in data for k in ("username", "email", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    if user_facade.get_user_by_email(data['email']):
        return jsonify({"error": "Email already registered"}), 409

    new_user = user_facade.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not all(k in data for k in ("email", "password")):
        return jsonify({"error": "Missing email or password"}), 400

    user = user_facade.get_user_by_email(data['email'])
    if not user or not user.check_password(data['password']):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)

    return jsonify({
        "access_token": token,
        "user": user.to_dict(include_email=True)
    }), 200

