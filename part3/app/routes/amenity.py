# app/routes/amenity.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.jwt_handler import admin_required
from models.amenity import Amenity

amenity_bp = Blueprint('amenity', __name__)

@amenity_bp.route('/', methods=['POST'])
@jwt_required()
@admin_required
def create_amenity():
    # Delayed import to avoid circular dependency
    from app import db

    data = request.get_json()
    if not data.get("name"):
        return jsonify({"error": "Amenity name required"}), 400

    if Amenity.query.filter_by(name=data["name"]).first():
        return jsonify({"error": "Amenity already exists"}), 409

    amenity = Amenity(name=data["name"])
    db.session.add(amenity)
    db.session.commit()

    return jsonify(amenity.to_dict()), 201

@amenity_bp.route('/<int:amenity_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_amenity(amenity_id):
    # Delayed import to avoid circular dependency
    from app import db

    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404

    data = request.get_json()
    amenity.name = data.get("name", amenity.name)
    db.session.commit()

    return jsonify(amenity.to_dict()), 200

