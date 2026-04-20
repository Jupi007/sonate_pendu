from flask import Flask

from src.game_routes import gameRoutes


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "NOTASECRETKEY"
    app.register_blueprint(gameRoutes)

    return app
