from flask import Blueprint, render_template

routes = Blueprint("routes", __name__, template_folder="templates")


@routes.route("/")
def home():
    with open("src/data/dictionnaire.txt", "r") as file:
        word_list = [line.split(";")[0].strip() for line in file if line.strip()]

    return render_template("index.html", word_list=word_list)
