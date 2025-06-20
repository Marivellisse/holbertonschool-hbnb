from flask_restx import Api
from flask import Blueprint

# Importa los namespaces
from .users import api as user_ns
from .amenities import api as amenity_ns
from .places import api as place_ns
from .reviews import api as review_ns

# Crea el blueprint
blueprint = Blueprint('api', __name__)

# Crea el objeto Api y lo asocia al blueprint
api = Api(
    blueprint,
    title="HBnB API",
    version="1.0",
    description="HBnB Evolution REST API"
)

# Añade los namespaces sin duplicar el prefijo /api/v1
api.add_namespace(user_ns, path="/users")
api.add_namespace(amenity_ns, path="/amenities")
api.add_namespace(place_ns, path="/places")
api.add_namespace(review_ns, path="/reviews")

