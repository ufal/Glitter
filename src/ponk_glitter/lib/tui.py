from math import floor

from rich import print
from rich.console import Console
from rich.table import Table

from lib.glitter_common import GlitteredText, GlitteredToken

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
                  "deep_pink4"
                  "dark_red"]

NOT_FOUND_COLOR = "deep_sky_blue1"


def color_by_prob(token: GlitteredToken) -> str:
    i = floor(token.probability * (len(COLOR_GRADIENT) + 1))
    return f"[{COLOR_GRADIENT[int(i)]}]{token.original_token}[/]"


def color_by_frequency(token, step=900):
    ceiling = 100
    if token.nth == -1:
        return f"[{NOT_FOUND_COLOR}]{token.original_token}[/]"
    for i, c in enumerate(COLOR_GRADIENT, start=1):
        if token.nth <= ceiling:
            return f"[{c}]{token.original_token}[/]"
        ceiling = i * step
    return f"[{COLOR_GRADIENT[-1]}]{token.original_token}[/]"


def print_glittered_text_by_prob(gt: GlitteredText) -> None:
    for token in gt.get_content():
        print(color_by_prob(token), end=" ")
    print("\n")


def print_table_of_glittered_text(gt: GlitteredText, title="") -> None:
    table = Table(title=title)
    table.add_column("Word", justify="left", no_wrap=True)
    table.add_column("Nth", justify="center")
    table.add_column("Probability", justify="right")
    table.add_column("Top 3", justify="right")
    for token in gt.get_content():
        table.add_row(token.original_token,
                      str(token.nth) if token.nth != -1 else "?",
                      f"{token.probability:.8f}",
                      " ".join([token.data[i][0] for i in range(3)]))
    console = Console()
    console.print(table)


def print_glittered_text(gt: GlitteredText):
    for token in gt.get_content():
        print(color_by_frequency(token), end="")
    print("\n")


def print_color_gradient():
    for c in COLOR_GRADIENT:
        print(f"[{c}]███[/]")
