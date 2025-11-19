#!/usr/bin/env python3
from flask import Flask, send_from_directory, request, render_template
import logging
from functools import cache
from conllu import parse
from lib.arguments import get_server_args
from lib.glitter_models import load_models, categorize_models

MODELS = load_models(verbose=True)
CATEGORIZED_MODELS = categorize_models(MODELS)
COLOR_MODES = ("heatmap-logprob-custom", "heatmap-logprob-uniform", "heatmap-nth", "simple-nth")
SILENT_MODE = False

app = Flask(__name__, static_folder="static")


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
    if selected_model is None and models:
        selected_model = tuple(models)[0]
    if selected_color_mode is None and color_modes:
        selected_color_mode = COLOR_MODES[0]


    return render_template("index.html",
                           text_to_glitter=text_to_glitter,
                           glittered_text=glittered_text,
                           color_modes=color_modes,
                           categorized_models=CATEGORIZED_MODELS,
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
    glittered_text = model.glitter_text(text_to_glitter, silent=SILENT_MODE)
    return glittered_text.to_html(color_mode=color_mode)

@cache
def glitter_text_to_conllu(conllu_string: str, model_name: str) -> str:
    model = MODELS[model_name]
    conllu_data = parse(conllu_string)
    text_to_glitter = ""
    for sentence in conllu_data:
        if "text" in sentence.metadata:
            for word in sentence:
                form = word["form"].strip()
                lemma =  word["lemma"].strip()
                #if "misc" not in word or not isinstance(word["misc"], dict):
                #    print(f"SKIPPING no misc for word {form}")
                #    continue
                # Truecase
                if form[0].isupper() and lemma[0].islower():
                    text_to_glitter += f'{form.lower()} '
                else:
                    text_to_glitter += f'{form} '
    #print(text_to_glitter)
    glittered_text = model.glitter_text(text_to_glitter, silent=SILENT_MODE)
    return glittered_text.to_conllu(conllu_data)

@app.route("/", methods=["POST"])
def glitter_text_request():
    text_to_glitter = request.form["text_to_glitter"]
    model_name = request.form["model"]
    color_mode = request.form["color_mode"]
    print(f" * Glittering with model: {model_name} and color_mode: {color_mode}")
    return render_index_page(text_to_glitter=text_to_glitter,
                             glittered_text=glitter_text(text_to_glitter,
                                                         model_name,
                                                         color_mode),
                             selected_model=model_name,
                             selected_color_mode=color_mode)

@app.route('/process-conllu', methods=['POST'])
def process_conllu():
    conllu_string = request.data.decode('utf-8')
    modified_conllu_string = glitter_text_to_conllu(conllu_string, "GPT-2 XL Czech") #"Ngram-5") #"GPT-2 XL Czech") 
    result = {
        'result': modified_conllu_string,
        'colors' : 
            {
                1 : "#6d6df7", 
                2 : "#6d7ef7", 
                3 : "#6d8ff7", 
                4 : "#6da0f7", 
                5 : "#6db2f7", 
                6 : "#6dc3f7", 
                7 : "#6dd4f7", 
                8 : "#6de6f7", 
                9 : "#6df7f7", 
                10 : "#6df7b2", 
                11 : "#6df76d", 
                12 : "#b2f76d", 
                13 : "#f7f76d", 
                14 : "#f7d46d", 
                15 : "#f7b26d", 
                16 : "#f76d6d"
            } 
        }

    return result
######################################################################################
# Server


def detect_cuda():
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False



if __name__ == "__main__":
    args = get_server_args()

    log = logging.getLogger("werkzeug")
    if args.debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.ERROR)

    if len(MODELS) == 0:
        exit(1)

    if args.silent:
        SILENT_MODE = True

    if detect_cuda():
        print("CUDA is available")
    else:
        print("CUDA is NOT available, running on CPU")

    app.run(host=args.host, port=args.port, debug=args.debug)
