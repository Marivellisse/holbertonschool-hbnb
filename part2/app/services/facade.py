from app.business.models.user import User
from app.business.models.place import Place
from app.business.models.amenity import Amenity
from app.business.models.review import Review
import uuid

USERS = {}
PLACES = {}
AMENITIES = {}
REVIEWS = {}

class HBnBFacade:

    def create_place(self, place_data):
        place_id = str(uuid.uuid4())
        owner_id = place_data['owner_id']
        amenity_ids = place_data['amenities']

        # Validación
        if place_data['price'] < 0:
            return {'message': 'Invalid price'}, 400
        if not -90 <= place_data['latitude'] <= 90:
            return {'message': 'Invalid latitude'}, 400
        if not -180 <= place_data['longitude'] <= 180:
            return {'message': 'Invalid longitude'}, 400

        owner = USERS.get(owner_id)
        if not owner:
            return {'message': 'Owner not found'}, 404

        amenities = []
        for aid in amenity_ids:
            amenity = AMENITIES.get(aid)
            if not amenity:
                return {'message': f'Amenity {aid} not found'}, 404
            amenities.append(amenity)

        place = Place(id=place_id, amenities=amenities, **place_data)
        PLACES[place_id] = place
        return place.to_dict(), 201

    def get_place(self, place_id):
        place = PLACES.get(place_id)
        if not place:
            return {'message': 'Place not found'}, 404

        owner = USERS.get(place.owner_id)
        amenity_dicts = [a.to_dict() for a in place.amenities]
        review_dicts = [r.to_dict() for r in REVIEWS.values() if r.place_id == place_id]

        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': owner.to_dict() if owner else None,
            'amenities': amenity_dicts,
            'reviews': review_dicts
        }, 200

    def get_all_places(self):
        return [
            {
                'id': p.id,
                'title': p.title,
                'latitude': p.latitude,
                'longitude': p.longitude
            } for p in PLACES.values()
        ], 200

    def update_place(self, place_id, place_data):
        place = PLACES.get(place_id)
        if not place:
            return {'message': 'Place not found'}, 404

        if 'price' in place_data and place_data['price'] < 0:
            return {'message': 'Invalid price'}, 400
        if 'latitude' in place_data and not -90 <= place_data['latitude'] <= 90:
            return {'message': 'Invalid latitude'}, 400
        if 'longitude' in place_data and not -180 <= place_data['longitude'] <= 180:
            return {'message': 'Invalid longitude'}, 400

        for key, value in place_data.items():
            if hasattr(place, key):
                setattr(place, key, value)

        return {'message': 'Place updated successfully'}, 200

    # --- Métodos de Review ---

    def create_review(self, review_data):
        review_id = str(uuid.uuid4())
        user = USERS.get(review_data['user_id'])
        place = PLACES.get(review_data['place_id'])

        if not user:
            return {'message': 'User not found'}, 404
        if not place:
            return {'message': 'Place not found'}, 404
        if not 1 <= review_data['rating'] <= 5:
            return {'message': 'Rating must be between 1 and 5'}, 400

        review = Review(id=review_id, **review_data)
        REVIEWS[review_id] = review
        return review.to_dict(), 201

    def get_review(self, review_id):
        review = REVIEWS.get(review_id)
        if review:
            return review.to_dict(), 200
        return {'message': 'Review not found'}, 404

    def get_all_reviews(self):
        return [r.to_dict() for r in REVIEWS.values()], 200

    def get_reviews_by_place(self, place_id):
        if place_id not in PLACES:
            return {'message': 'Place not found'}, 404
        return [r.to_dict() for r in REVIEWS.values() if r.place_id == place_id], 200

    def update_review(self, review_id, review_data):
        review = REVIEWS.get(review_id)
        if not review:
            return {'message': 'Review not found'}, 404

        if 'rating' in review_data and not 1 <= review_data['rating'] <= 5:
            return {'message': 'Rating must be between 1 and 5'}, 400

        for key, value in review_data.items():
            if hasattr(review, key):
                setattr(review, key, value)

        return {'message': 'Review updated successfully'}, 200

    def delete_review(self, review_id):
        if review_id in REVIEWS:
            del REVIEWS[review_id]
            return {'message': 'Review deleted successfully'}, 200
        return {'message': 'Review not found'}, 404

