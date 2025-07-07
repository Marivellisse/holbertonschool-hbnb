from app.repository.amenity_repository import SQLAlchemyAmenityRepository

class AmenityFacade:
    def __init__(self):
        self.repo = SQLAlchemyAmenityRepository()

    def get_amenity(self, amenity_id):
        return self.repo.get_by_id(amenity_id)

    def get_all_amenities(self):
        return self.repo.get_all()

    def create_amenity(self, name):
        return self.repo.create(name)

    def update_amenity(self, amenity, data):
        return self.repo.update(amenity, data)

    def delete_amenity(self, amenity):
        self.repo.delete(amenity)

