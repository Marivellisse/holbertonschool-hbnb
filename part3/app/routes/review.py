# app/routes/review.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app import db
from models.review import Review
from models.place import Place

review_bp = Blueprint('review', __name__)

@review_bp.route('/', methods=['POST'])
@jwt_required()
def create_review():
    data = request.get_json()
    user_id = get_jwt_identity()
    claims = get_jwt()

    place_id = data.get("place_id")
    content = data.get("content")
    rating = data.get("rating")

    if not all([place_id, content, rating]):
        return jsonify({"error": "Missing fields"}), 400

    place = Place.query.get(place_id)
    if not place:
        return jsonify({"error": "Place not found"}), 404
    if place.owner_id == user_id and not claims.get("is_admin", False):
        return jsonify({"error": "You can't review your own place"}), 403

    existing = Review.query.filter_by(place_id=place_id, user_id=user_id).first()
    if existing:
        return jsonify({"error": "You already reviewed this place"}), 400

    review = Review(
        content=content,
        rating=rating,
        user_id=user_id,
        place_id=place_id
    )
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict()), 201


@review_bp.route('/<int:review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    user_id = get_jwt_identity()
    claims = get_jwt()
    review = Review.query.get(review_id)

    if not review:
        return jsonify({"error": "Review not found"}), 404
    if review.user_id != user_id and not claims.get("is_admin", False):
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    review.content = data.get("content", review.content)
    review.rating = data.get("rating", review.rating)

    db.session.commit()
    return jsonify(review.to_dict()), 200

