from app import create_app
from app.settings import Config

if __name__ == "__main__":
    app = create_app(Config)
    app.run(debug=True, port=5001)

