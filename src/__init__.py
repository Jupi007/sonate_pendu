from flask import Flask

from src.game import game


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "NOTASECRETKEY"
    app.register_blueprint(game)

    return app
