from flask import Flask, render_template

from src.routes import routes


def create_app():
    app = Flask(__name__)
    app.secret_key = "NOTSOSECRETKEY"
    app.register_blueprint(routes)

    return app
