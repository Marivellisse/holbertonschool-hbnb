from models.review import Review
from app import db

class SQLAlchemyReviewRepository:
    def get_by_id(self, review_id):
        return Review.query.get(review_id)

    def get_all(self):
        return Review.query.all()

    def create(self, content, rating, user_id, place_id):
        review = Review(
            content=content,
            rating=rating,
            user_id=user_id,
            place_id=place_id
        )
        db.session.add(review)
        db.session.commit()
        return review

    def update(self, review, data):
        review.content = data.get("content", review.content)
        review.rating = data.get("rating", review.rating)
        db.session.commit()
        return review

    def delete(self, review):
        db.session.delete(review)
        db.session.commit()

