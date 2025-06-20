from app.business.models.base_model import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, **kwargs):
        super().__init__(**kwargs)

        if not first_name or not first_name.strip():
            raise ValueError("First name is required")
        if not last_name or not last_name.strip():
            raise ValueError("Last name is required")
        if not email or not self._is_valid_email(email):
            raise ValueError("Invalid email format")
        if not password or len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def _is_valid_email(self, email):
        # Simple regex for basic email validation
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

