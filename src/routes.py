import random
from flask import Blueprint, redirect, render_template, request

from src.game_state import game_state
from src.dictionnary import dictionnary


routes = Blueprint("routes", __name__, template_folder="templates")


@routes.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        game_state.clear()
        game_state.username = request.form.get("username")
        game_state.word_id = random.randint(0, dictionnary.len)
        return redirect("/jouer", 303)


@routes.route("/jouer", methods=["GET"])
def game():
    return render_template(
        "game.html",
        username=game_state.username,
        word=dictionnary.get(game_state.word_id),
    )
