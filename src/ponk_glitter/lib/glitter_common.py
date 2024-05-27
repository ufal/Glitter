import json
from typing import List

from jinja2 import Template
from torch import torch


class GlitteredToken:
    __HEATMAP_CATEGORIES = tuple(enumerate([1, 3, 5, 10, 15, 25, 50, 75, 100,
                                            250, 500, 1000, 5000, 10000, 15000, 20000]))
    __SIMPLE_CATEGORY = ((0, 1), (3, 10), (7, 100), (10, 1000), (14, 10000))
    # from cold to hot
    __HEATMAP_TERMINAL_COLORS = ["blue1", "dodger_blue1", "deep_sky_blue3", "cyan1",
                                 "spring_green1", "green1", "chartreuse1", "yellow1",
                                 "light_goldenrod1", "gold1", "orange1", "orange_red1",
                                 "red1", "deep_pink1", "magenta1", "plum1"]

    __HTML_TEMPLATE = '''
    <div class="glitter-token">
        <span class="gt-heatmap-{{- heatmap_color_index -}}">{{ original_token }}</span>
            <div class="gt-context">
                <span class="gt-probability">P: {{ probability -}}</span>
                <span class="gt-nth">N: {{ nth -}}</span>
                <hr>
                <ol>
                    {% for item in data -%}
                        <li>{{ item }}</li>
                    {%- endfor -%}
                </ol>
                </div>
            </div>
    '''.strip()

    def __init__(self, original_token: str, raw_values):
        self.probability = 0
        self.original_token = original_token
        self.data = raw_values
        self.nth = -1
        self.vocab_size = len(raw_values)
        for n, (token, prob) in enumerate(raw_values, start=1):
            if token.strip() == original_token.strip():
                self.probability = prob
                self.nth = n
                break

    def to_dict(self):
        return {
            "original_token": self.original_token,
            "probability": self.probability,
            "nth": self.nth,
            "top_5": self.data[:5]
        }

    def __get_heatmap_color_index__(self, color_map=__HEATMAP_CATEGORIES) -> int:
        color_index = 15
        for i, category in color_map:
            if self.nth <= category:
                color_index = i
                break
        return color_index

    def to_html(self, color_mode="heatmap"):
        color_mode = color_mode.lower()
        if color_mode == "simple":
            color_map = self.__SIMPLE_CATEGORY
        else:
            color_map = self.__HEATMAP_CATEGORIES

        color_index = self.__get_heatmap_color_index__(color_map)

        # Render the template with the context
        output = Template(self.__HTML_TEMPLATE).render(
            heatmap_color_index=color_index,
            original_token=self.original_token.replace(" ", "&nbsp;"),
            probability=f"{self.probability:.8f}",
            nth=self.nth,
            data=[f"{token} ({prob:.8f})" for token, prob in self.data[:5]]
        )

        return output

    def __str__(self):
        # rich color output
        return f"[{self.__HEATMAP_TERMINAL_COLORS[self.__get_heatmap_color_index__()]}]{self.original_token}[/]"


class GlitteredText:

    def __init__(self, models: List[str]):
        self.used_models = models
        self.content: List[GlitteredToken] = list()
        self.used_models: List[str] = list()

    def append(self, token: GlitteredToken) -> None:
        self.content.append(token)

    def get_content(self) -> List[GlitteredToken]:
        return self.content

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_html(self) -> str:
        output = '<div class="glittered-text">'
        for token in self.content:
            output += token.to_html()
        return output + "</div>"

    def to_dict(self):
        return {
            "content": [token.to_dict() for token in self.content],
            "used_models": self.used_models
        }

    def __str__(self):
        return "".join([str(token) for token in self.content])

    def __len__(self):
        return len(self.content)

    def __getitem__(self, item):
        return self.content[item]

    def __iter__(self):
        return iter(self.content)

    def __reversed__(self):
        return reversed(self.content)

    def __contains__(self, item):
        return item in self.content


def convert_tokenized_text_to_tensor(tokenized_text: {str: [int]}) -> {str: torch.Tensor}:
    return {key: torch.tensor([value]) for key, value in tokenized_text.items()}


def get_top_k_tokens(logits: list, tokenizer, top_k: int, ) -> [(str, float)]:
    # Get the probabilities of the last token
    # Create list of tuples with the index(token ID) and its probability
    indexed_probs = [(index, p) for index, p in enumerate(logits)]
    # Sort the list by probability
    indexed_probs.sort(key=lambda x: x[1], reverse=True)
    # Get the top k probabilities
    probs_top_k = indexed_probs[:top_k]
    # Create list of tuples with the token and its probability
    str_prob = [(tokenizer.decode([index]), p) for index, p in probs_top_k]
    return str_prob


def normalize_glittered_text_with_subword_tokens(glittered_text: GlitteredText) -> GlitteredText:
    for token in glittered_text.get_content():
        if token.original_token.startswith("##"):
            token.original_token = token.original_token[2:]
        else:
            token.original_token = " " + token.original_token
    return glittered_text
