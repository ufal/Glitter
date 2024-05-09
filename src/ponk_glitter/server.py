from flask import Flask, jsonify, send_from_directory, request, render_template
from functools import cache

from models.robeczech import Robeczech

MODELS = dict()
app = Flask(__name__, static_folder="static")


######################################################################################
# Interface


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/<path:path>", methods=["GET"])
def static_route(path):
    return send_from_directory("static", path)


######################################################################################
# API


"""
{
    "model": "robeczech",
    "text": text,
    "context_size": 1000
}
"""

@app.route("/glitter_text", methods=["POST"])
def glitter_text():
    text_to_glitter = request.form["text_to_glitter"]
    model = request.form["model"]
    return render_template("index.html", glittered_text=model)


######################################################################################
# Server

def server_init():
    global MODELS
    MODELS["robeczech"] = Robeczech()


if __name__ == "__main__":
    server_init()
    app.run()

