#!/usr/bin/env python3
import os
import sys

from rich import print
from rich.console import Console
from rich.table import Table
from conllu import parse_incr

from lib.arguments import get_cli_args
from lib.glitter_common import GlitteredText, GlitteredToken
from lib.glitter_models import get_registered_models

COLOR_GRADIENT = ["cornsilk1",
                  "wheat1",
                  "khaki1",
                  "gold1",
                  "bright_yellow",
                  "orange1",
                  "dark_orange",
                  "deep_pink2",
                  "red1",
                  "red3",
                  "deep_pink4",
                  "dark_red"]

NOT_FOUND_COLOR = "deep_sky_blue1"


def print_table_of_glittered_text(gt: GlitteredText, title="") -> None:
    table = Table(title=title)
    table.add_column("Word", justify="left", no_wrap=True)
    table.add_column("Nth", justify="center")
    table.add_column("Probability", justify="right")
    table.add_column("Top results", justify="right")
    for token in gt.get_content():
        top_n = " ".join([i[0] for i in token.top_k_tokens]) if len(token.top_k_tokens) < 10 else " ".join(
            [token.top_k_tokens[i][0] for i in range(10)])
        table.add_row(token.original_token.replace("\n", r"[\n]"),
                      str(token.nth) if token.nth != -1 else "ε",
                      f"{token.probability:.8f}",
                      top_n)
    console = Console()
    console.print(table)


def print_color_gradient():
    print("Smallest entropy", end=" ")
    for c in GlitteredToken.HEATMAP_TERMINAL_COLORS:
        print(f"[{c}]███[/]", end="")
    print(" Highest entropy")

########################################################################################

def cmd_list_models():
    print("Available models:")
    for model in AVAILABLE_MODELS:
        print(f"  {model}")
    exit(0)


def is_conllu_file(filename):
    return filename.lower().endswith(".conllu") or filename.lower().endswith(".conll")


def read_conllu(filename):
    text = ""
    with open(input_file, "r") as file:
        data = parse_incr(file)
        for sentence in data:
            if "text" in sentence.metadata:
               text += sentence.metadata["text"]
               text += " "
    return data, text


if __name__ == "__main__":
    args = get_cli_args()
    AVAILABLE_MODELS = get_registered_models()

    if args.list_models:
        cmd_list_models()

    input_file = args.input if args.input else "/dev/stdin"
    output_file = args.output if args.output else "/dev/stdout"
    args.model = args.model.lower()


    if args.model not in AVAILABLE_MODELS:
        print("Model not found")
        exit(1)
    m = AVAILABLE_MODELS[args.model]()

    if is_conllu_file(input_file) or args.to_conllu:
        conllu_data, text = read_conllu(input_file)
    else:
        with open(input_file, "r") as file:
            text = file.read()
    
    gt = m.glitter_text(text)

    if args.to_json:
        with open(output_file, "w") as file:
            file.write(gt.to_json())
    elif args.to_html:
        with open(output_file, "w") as file:
            file.write(gt.to_html())
    elif args.to_dict:
        with open(output_file, "w") as file:
            file.write(str(gt.to_dict()))
    elif args.to_tex:
        with open(output_file, "w") as file:
            file.write(gt.to_tex())
    elif args.to_table:
        print_table_of_glittered_text(gt)
    elif args.to_conllu:
        with open(output_file, "w") as file:
            file.write(gt.to_conllu(conllu_data))
    else:
        print_color_gradient()
        print("")
        print(str(gt))
