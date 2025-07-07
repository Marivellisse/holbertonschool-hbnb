from models.place import Place
from app import db

class SQLAlchemyPlaceRepository:
    def get_by_id(self, place_id):
        return Place.query.get(place_id)

    def get_all(self):
        return Place.query.all()

    def create(self, name, description, owner_id):
        place = Place(name=name, description=description, owner_id=owner_id)
        db.session.add(place)
        db.session.commit()
        return place

    def update(self, place, data):
        place.name = data.get("name", place.name)
        place.description = data.get("description", place.description)
        db.session.commit()
        return place

    def delete(self, place):
        db.session.delete(place)
        db.session.commit()

