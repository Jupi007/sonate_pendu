import string

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
        game_state.word_id = dictionnary.get_random_word_id()
        return redirect("/jouer", 303)


@routes.route("/jouer", methods=["GET"])
def game():
    word = dictionnary.get(game_state.word_id)
    player_attempts = game_state.player_attempts
    hint = ""

    for letter in word:
        if letter.upper() in player_attempts:
            hint += letter
        else:
            hint += "_"

    return render_template(
        "game.html",
        username=game_state.username,
        hint=hint,
        word=word,
        alphabet=string.ascii_uppercase,
        player_attempts=player_attempts,
    )


@routes.route("/jouer/envoyer", methods=["POST"])
def game_send():
    game_state.add_player_attempt(request.form.get("letter"))
    return redirect("/jouer", 303)
