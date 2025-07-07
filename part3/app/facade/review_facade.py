from app.repository.review_repository import SQLAlchemyReviewRepository

class ReviewFacade:
    def __init__(self):
        self.repo = SQLAlchemyReviewRepository()

    def get_review(self, review_id):
        return self.repo.get_by_id(review_id)

    def get_all_reviews(self):
        return self.repo.get_all()

    def create_review(self, content, rating, user_id, place_id):
        return self.repo.create(content, rating, user_id, place_id)

    def update_review(self, review, data):
        return self.repo.update(review, data)

    def delete_review(self, review):
        self.repo.delete(review)

