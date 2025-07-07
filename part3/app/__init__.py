# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.routes.amenity import amenity_bp
app.register_blueprint(amenity_bp, url_prefix="/api/amenities")

from flask_jwt_extended import JWTManager
from app.routes.place import place_bp
from app.routes.review import review_bp

app.register_blueprint(place_bp, url_prefix="/api/places")
app.register_blueprint(review_bp, url_prefix="/api/reviews")


# Extensiones globales
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_class=None):
    app = Flask(__name__)

    # Configuración
    if config_class:
        app.config.from_object(config_class)
    else:
        from app.config import Config
        app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Blueprints
    from app.routes.auth import auth_bp
    from app.routes.user import user_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")

    # JWT config: añadir claims personalizados
    @jwt.user_identity_loader
    def user_identity_lookup(user_id):
        return user_id

    @jwt.additional_claims_loader
    def add_claims_to_access_token(identity):
        from models.user import User
        user = User.query.get(identity)
        return {
            'is_admin': user.is_admin() if user else False
        }

    return app

