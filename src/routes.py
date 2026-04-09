from flask import Blueprint, render_template, request

routes = Blueprint("routes", __name__, template_folder="templates")


@routes.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", username=request.form.get("username"))
