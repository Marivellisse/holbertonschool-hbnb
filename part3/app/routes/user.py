# app/routes/user.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.facade.user_facade import UserFacade
from app.utils.jwt_handler import admin_required

user_bp = Blueprint('user', __name__)
user_facade = UserFacade()

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def get_my_profile():
    user_id = get_jwt_identity()
    user = user_facade.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict(include_email=True)), 200

@user_bp.route('/me', methods=['PUT'])
@jwt_required()
def update_my_profile():
    user_id = get_jwt_identity()
    user = user_facade.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    updated = user_facade.update_user(user, {
        "username": data.get("username"),
        "role": data.get("role")
    })

    return jsonify(updated.to_dict(include_email=True)), 200

# ADMIN — create user
@user_bp.route('/', methods=['POST'])
@jwt_required()
@admin_required
def create_user_admin():
    data = request.get_json()
    if not data or not all(k in data for k in ("username", "email", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    if user_facade.get_user_by_email(data['email']):
        return jsonify({"error": "Email already exists"}), 409

    user = user_facade.create_user(
        username=data["username"],
        email=data["email"],
        password=data["password"],
        role=data.get("role", "user")
    )
    return jsonify(user.to_dict(include_email=True)), 201

# ADMIN — update any user
@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_any_user(user_id):
    user = user_facade.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    updated = user_facade.update_user(user, data)

    return jsonify(updated.to_dict(include_email=True)), 200

