#!/usr/bin/env python3
from flask import Flask, jsonify, send_from_directory, request, render_template
import logging
from functools import cache

from lib.arguments import get_server_args
from lib.glitter_common import GlitteredText
from lib.glitter_models import AVAILABLE_MODELS, load_models

MODELS = load_models(logging=True)
COLOR_MODES = ("heatmap", "simple")

app = Flask(__name__, static_folder="static")
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)


######################################################################################
# Interface + Static

def sanitize_path(path):
    return path.replace("../", "").replace("./", "")


def render_index_page(text_to_glitter="",
                      glittered_text="",
                      models=MODELS.keys(),
                      color_modes=COLOR_MODES,
                      selected_model=None,
                      selected_color_mode=None):
    if selected_model == None and models:
        selected_model = tuple(models)[0]
    if selected_color_mode == None and color_modes:
        selected_color_mode = COLOR_MODES[0]

    return render_template("index.html",
                           text_to_glitter=text_to_glitter,
                           glittered_text=glittered_text,
                           color_modes=color_modes,
                           models=models,
                           selected_model=selected_model,
                           selected_color_mode=selected_color_mode)


@app.route("/", methods=["GET"])
def index():
    return render_index_page()


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
    color_mode = request.form["color_mode"]
    print(f" * Glittering with model: {model_name} and color_mode: {color_mode}")
    return render_index_page(text_to_glitter=text_to_glitter,
                             glittered_text=glitter_text(text_to_glitter, model_name, color_mode),
                             selected_model=model_name,
                             selected_color_mode=color_mode)


######################################################################################
# Server

if __name__ == "__main__":
    args = get_server_args()
    if len(MODELS) == 0:
        exit(1)
    app.run(host=args.host, port=args.port, debug=args.debug)
