from flask_restx import Api
from flask import Blueprint
from .users import api as user_ns

blueprint = Blueprint('api', __name__)
api = Api(blueprint, title="HBnB API", version="1.0", description="HBnB Evolution REST API")
api.add_namespace(user_ns, path="/users")

