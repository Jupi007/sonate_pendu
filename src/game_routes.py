import string

from flask import Blueprint, redirect, render_template, request

from src.game.game import HangmanGame
from src.game.game_state import UNDEFINED_WORD_ID
from src.session_game_state import session_game_state
from src.game.dictionnary import dictionnary


gameRoutes = Blueprint("gameRoutes", __name__, template_folder="templates")


@gameRoutes.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        username = request.form.get("username", type=str)
        if not username:
            return redirect("/", 303)

        session_game_state.clear()
        session_game_state.username = username
        session_game_state.word_id = dictionnary.get_random_word_id()
        return redirect("/jouer", 303)


@gameRoutes.route("/jouer", methods=["GET"])
def play():
    word_id = session_game_state.word_id
    if word_id == UNDEFINED_WORD_ID:
        return redirect("/", 303)

    game = HangmanGame(session_game_state)

    return render_template(
        "game.html",
        username=session_game_state.username,
        hint=game.hint,
        alphabet=string.ascii_uppercase,
        player_attempts=session_game_state.player_attempts,
        remaining_lifes=game.remaining_lifes,
    )


@gameRoutes.route("/jouer/envoyer", methods=["POST"])
def play_send():
    word_id = session_game_state.word_id
    if word_id == UNDEFINED_WORD_ID:
        return redirect("/", 303)

    letter = request.form.get("letter", type=str)
    if not letter:
        return redirect("/jouer", 303)

    game = HangmanGame(session_game_state)
    game.attempt(letter)

    if game.remaining_word_letters == 0:
        return redirect("/gameover?victory=1", 303)
    elif game.remaining_lifes <= 0:
        return redirect("/gameover?victory=0", 303)

    return redirect("/jouer", 303)


@gameRoutes.route("/gameover", methods=["GET"])
def gameover():
    word_id = session_game_state.word_id
    if word_id == UNDEFINED_WORD_ID:
        return redirect("/", 303)

    word = dictionnary.get(word_id)
    return render_template(
        "gameover.html",
        word=word,
        victory=request.args.get("victory") == "1",
    )
