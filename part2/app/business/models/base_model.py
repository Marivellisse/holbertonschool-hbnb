import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id", str(uuid.uuid4()))
        self.created_at = kwargs.get("created_at", datetime.utcnow())
        self.updated_at = kwargs.get("updated_at", datetime.utcnow())

    def update(self):
        self.updated_at = datetime.utcnow()

