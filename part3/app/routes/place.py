# app/routes/place.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app import db
from models.place import Place

place_bp = Blueprint('place', __name__)

@place_bp.route('/', methods=['POST'])
@jwt_required()
def create_place():
    data = request.get_json()
    user_id = get_jwt_identity()

    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    new_place = Place(
        name=data["name"],
        description=data.get("description"),
        owner_id=user_id
    )
    db.session.add(new_place)
    db.session.commit()

    return jsonify(new_place.to_dict()), 201


@place_bp.route('/<int:place_id>', methods=['PUT'])
@jwt_required()
def update_place(place_id):
    user_id = get_jwt_identity()
    claims = get_jwt()
    place = Place.query.get(place_id)

    if not place:
        return jsonify({"error": "Place not found"}), 404
    if place.owner_id != user_id and not claims.get("is_admin", False):
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    place.name = data.get("name", place.name)
    place.description = data.get("description", place.description)

    db.session.commit()
    return jsonify(place.to_dict()), 200


@place_bp.route('/<int:place_id>', methods=['DELETE'])
@jwt_required()
def delete_place(place_id):
    user_id = get_jwt_identity()
    claims = get_jwt()
    place = Place.query.get(place_id)

    if not place:
        return jsonify({"error": "Place not found"}), 404
    if place.owner_id != user_id and not claims.get("is_admin", False):
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(place)
    db.session.commit()
    return jsonify({"message": "Place deleted"}), 200

