from app.repository.place_repository import SQLAlchemyPlaceRepository

class PlaceFacade:
    def __init__(self):
        self.repo = SQLAlchemyPlaceRepository()

    def get_place(self, place_id):
        return self.repo.get_by_id(place_id)

    def get_all_places(self):
        return self.repo.get_all()

    def create_place(self, name, description, owner_id):
        return self.repo.create(name, description, owner_id)

    def update_place(self, place, data):
        return self.repo.update(place, data)

    def delete_place(self, place):
        self.repo.delete(place)

