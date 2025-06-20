from flask import Flask
from flask_restx import Api
from app.presentation.routes import api as api_namespace

def create_app():
    app = Flask(__name__)
    api = Api(app, title="HBnB API", version="1.0", description="HBnB Evolution REST API")
    api.add_namespace(api_namespace, path="/api/v1")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

