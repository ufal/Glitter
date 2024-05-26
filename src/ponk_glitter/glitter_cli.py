#!/usr/bin/env python3
from rich import print
from rich.console import Console
from rich.table import Table

from lib.glitter_common import GlitteredText
from lib.arguments import get_cli_args

RBCZ = Robeczech()
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
    table.add_column("Top 10", justify="right")
    for token in gt.get_content():
        table.add_row(token.original_token.replace("\n", r"[\n]"),
                      str(token.nth) if token.nth != -1 else "ε",
                      f"{token.probability:.8f}",
                      " ".join([token.data[i][0] for i in range(10)]))
    console = Console()
    console.print(table)


def print_color_gradient():
    for c in COLOR_GRADIENT:
        print(f"[{c}]███[/]")


if __name__ == '__main__':
    args = get_cli_args()
    input_file = args.input if args.input else "/dev/stdin"
    output_file = args.output if args.output else "/dev/stdout"
    args.model = args.model.lower()

    with open(input_file, "r") as file:
        text = file.read()
        gt = RBCZ.glitter_text(text)

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
