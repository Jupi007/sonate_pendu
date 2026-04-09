from flask import Flask, render_template

from src.routes import routes


def create_app():
    app = Flask(__name__)

    app.register_blueprint(routes)

    return app
