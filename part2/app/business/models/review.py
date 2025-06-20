from app.business.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, user_id, place_id, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.user_id = user_id
        self.place_id = place_id

