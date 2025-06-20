# app/persistence/repository.py

import uuid
from datetime import datetime

class InMemoryRepository:
    def __init__(self):
        self.storage = {}

    def save(self, obj):
        obj.id = str(uuid.uuid4())
        obj.created_at = datetime.utcnow()
        obj.updated_at = datetime.utcnow()
        self.storage[obj.id] = obj
        return obj

    def get(self, obj_id):
        return self.storage.get(obj_id)

    def all(self):
        return list(self.storage.values())

    def update(self, obj_id, fields):
        obj = self.get(obj_id)
        if not obj:
            return None
        for key, value in fields.items():
            setattr(obj, key, value)
        obj.updated_at = datetime.utcnow()
        return obj

    def delete(self, obj_id):
        return self.storage.pop(obj_id, None)

