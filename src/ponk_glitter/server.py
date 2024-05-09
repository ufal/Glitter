from flask import Flask, jsonify, send_from_directory, request, render_template
from functools import cache
from lib.arguments import get_args

from models.robeczech import Robeczech

MODELS = dict()
app = Flask(__name__, static_folder="static")


######################################################################################
# Interface + Static

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/<path:path>", methods=["GET"])
def static_route(path):
    return send_from_directory("static", path)


######################################################################################
# API

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
    args = get_args()
    server_init()
    app.run(host=args.address, port=args.port, debug=args.debug)

