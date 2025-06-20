from app.business.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, description, price, latitude, longitude, owner_id, amenities=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities if amenities is not None else []

