from app.business.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None, **kwargs):
        super().__init__(**kwargs)

        if not title or not title.strip():
            raise ValueError("Title is required and cannot be empty.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a positive number.")
        if not isinstance(latitude, (int, float)) or not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        if not isinstance(longitude, (int, float)) or not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180.")
        if not owner_id or not isinstance(owner_id, str):
            raise ValueError("Owner ID is required and must be a string.")
        if amenities is not None and not isinstance(amenities, list):
            raise ValueError("Amenities must be a list if provided.")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities if amenities is not None else []

