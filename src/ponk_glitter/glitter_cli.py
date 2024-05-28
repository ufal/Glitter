#!/usr/bin/env python3
from rich import print
from rich.console import Console
from rich.table import Table

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
        top_n = " ".join([i[0] for i in token.data]) if len(token.data) < 10 else " ".join(
            [token.data[i][0] for i in range(10)])
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
    elif args.to_table:
        print_table_of_glittered_text(gt)
    else:
        print_color_gradient()
        print("")
        print(str(gt))
