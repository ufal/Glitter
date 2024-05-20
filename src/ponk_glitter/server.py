#!/usr/bin/env python3
from flask import Flask, jsonify, send_from_directory, request, render_template
from functools import cache
from lib.arguments import get_server_args
from models.robeczech import Robeczech
from lib.glitter_common import GlitteredText

MODELS = dict()
COLOR_MODES = ("simple", "heatmap")
app = Flask(__name__, static_folder="static")


######################################################################################
# Interface + Static

def sanitize_path(path):
    return path.replace("../", "").replace("./", "")


def render_index_page(glittered_text="", models=MODELS.keys(), color_modes=COLOR_MODES):
    return render_template("index.html",
                           glittered_text=glittered_text,
                           color_modes=color_modes,
                           models=models)


@app.route("/", methods=["GET"])
def index():
    return render_index_page("", MODELS.keys())


@app.route("/<path:path>", methods=["GET"])
def static_route(path):
    path = sanitize_path(path)
    return send_from_directory("static", path)



######################################################################################
# API

@cache
def glitter_text(text_to_glitter: str, model_name: str, color_mode: str) -> str:
    model = MODELS[model_name]
    glittered_text = model.glitter_text(text_to_glitter)
    return glittered_text.to_html()


@app.route("/", methods=["POST"])
def glitter_text_request():
    text_to_glitter = request.form["text_to_glitter"]
    model_name = request.form["model"]
    #color_mode = request.form["color_mode"]
    return render_index_page(glitter_text(text_to_glitter, model_name, ""))


######################################################################################
# Server

def server_init():
    global MODELS
    MODELS["Robeczech"] = Robeczech()

    print(" * Models loaded:")
    for model_name in MODELS.keys():
        print(f"   - {model_name}")


if __name__ == "__main__":
    args = get_server_args()
    server_init()
    app.run(host=args.host, port=args.port, debug=args.debug)

