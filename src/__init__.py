from flask import Flask, render_template

from src.game import game


def create_app():
    app = Flask(__name__)
    app.secret_key = "NOTASECRETKEY"
    app.register_blueprint(game)

    return app
