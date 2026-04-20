import string

from flask import Blueprint, redirect, render_template, request

from src.constants import PLAYER_LIFES
from src.gallows import Gallows
from src.session_game_state import session_game_state
from src.dictionnary import dictionnary


game = Blueprint("game", __name__, template_folder="templates")


@game.route("/", methods=["GET", "POST"])
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


@game.route("/jouer", methods=["GET"])
def play():
    word_id=session_game_state.word_id
    if not word_id:  
        return redirect("/", 303)
    
    word = dictionnary.get(word_id)
    player_attempts = session_game_state.player_attempts

    hint = ""
    for letter in word:
        if letter in player_attempts:
            hint += letter
        else:
            hint += "_"

    remaining_lifes = PLAYER_LIFES
    for letter in player_attempts:
        if not letter in word:
            remaining_lifes -= 1

    return render_template(
        "game.html",
        username=session_game_state.username,
        hint=hint,
        alphabet=string.ascii_uppercase,
        player_attempts=player_attempts,
        remaining_lifes=remaining_lifes,
        gallows=Gallows.get_progress_ascii(remaining_lifes),
    )


@game.route("/jouer/envoyer", methods=["POST"])
def play_send():
    word_id=session_game_state.word_id
    if not word_id:  
        return redirect("/", 303)
    
    letter = request.form.get("letter", type=str)
    if not letter:  
        return redirect("/jouer", 303)

    session_game_state.add_player_attempt(letter)

    word = dictionnary.get(word_id)
    player_attempts = session_game_state.player_attempts

    remaining_word_letters = list(set(word))
    remaining_lifes = PLAYER_LIFES
    for letter in player_attempts:
        if letter in remaining_word_letters:
            remaining_word_letters.remove(letter)
        else:
            remaining_lifes -= 1

    if len(remaining_word_letters) == 0:
        return redirect("/gameover?victory=1", 303)
    elif remaining_lifes <= 0:
        return redirect("/gameover?victory=0", 303)

    return redirect("/jouer", 303)


@game.route("/gameover", methods=["GET"])
def gameover():
    word = dictionnary.get(session_game_state.word_id)
    session_game_state.clear()
    return render_template(
        "gameover.html",
        word = word,
        victory=request.args.get("victory") == "1",
        failed_gallows=Gallows.get_progress_ascii(0),
    )
