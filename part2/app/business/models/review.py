from app.business.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, user_id, place_id, **kwargs):
        super().__init__(**kwargs)

        if not text or not text.strip():
            raise ValueError("Review text is required.")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5.")
        if not user_id or not isinstance(user_id, str):
            raise ValueError("Valid user_id is required.")
        if not place_id or not isinstance(place_id, str):
            raise ValueError("Valid place_id is required.")

        self.text = text
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id

