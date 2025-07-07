from models.amenity import Amenity
from app import db

class SQLAlchemyAmenityRepository:
    def get_by_id(self, amenity_id):
        return Amenity.query.get(amenity_id)

    def get_all(self):
        return Amenity.query.all()

    def create(self, name):
        amenity = Amenity(name=name)
        db.session.add(amenity)
        db.session.commit()
        return amenity

    def update(self, amenity, data):
        amenity.name = data.get("name", amenity.name)
        db.session.commit()
        return amenity

    def delete(self, amenity):
        db.session.delete(amenity)
        db.session.commit()

