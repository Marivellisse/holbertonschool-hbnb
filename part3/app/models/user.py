# models/user.py
from app import db, bcrypt
from models.base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')  # 'admin' o 'user'
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, username, email, password, role='user'):
        self.username = username
        self.email = email
        self.set_password(password)
        self.role = role

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self, include_email=False):
        data = {
            "id": self.id,
            "username": self.username,
            "role": self.role,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        if include_email:
            data["email"] = self.email
        return data

    def is_admin(self):
        return self.role == 'admin'

places = db.relationship('Place', backref='owner', lazy=True)
reviews = db.relationship('Review', backref='author', lazy=True)


