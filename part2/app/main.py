from flask import Flask
from app.presentation.routes import blueprint  # Importa el blueprint, no el api directo

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint, url_prefix="/api/v1")  # Aquí se activa la API
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5001)  # Usa un puerto alterno porque el 5000 está ocupado

