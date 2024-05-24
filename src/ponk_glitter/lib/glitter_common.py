from typing import List

from torch import torch
from jinja2 import Template
import json


class GlitteredToken:
    __HEATMAP_CATEGORIES = tuple(enumerate([1, 3, 5, 10, 15, 25, 50, 75, 100,
                            250, 500, 1000, 5000, 10000, 15000, 20000]))
    __SIMPLE_CATEGORY = ((0,1), (3, 10), (7, 100), (10, 1000), (14, 10000))
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


class GlitterModel:

    def __init__(self, name: str, lang: str, context_window_size: int = 5, sample_size: int = 1000) -> None:
        self.name: str = name
        self.lang: str = lang
        self.context_window_size: int = context_window_size
        self.top_k: int = sample_size
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def glitter_masked_token(self, original_token: str, masked_context: str) -> GlitteredToken:
        """
        Given a masked context and a token, return a list of tuples, where each tuple is a token and a score.
        """
        raise NotImplementedError()

    def glitter_text(self, text: str) -> GlitteredText:
        """
        Given a text, return a list of tuples, where each tuple is a token and a tuple of token and score.
        """
        raise NotImplementedError()

    def generate_text(self, prompt: str) -> str:
        """
        Given a prompt, generate a text.
        """
        raise NotImplementedError()

    def __str__(self):
        return f"{self.name} (context_window_size={self.context_window_size})"


def convert_tokenized_text_to_tensor(tokenized_text: {str: [int]}) -> {str: torch.Tensor}:
    return {key: torch.tensor([value]) for key, value in tokenized_text.items()}


def get_top_k_tokens(logits: list, tokenizer, top_k: int,) -> [(str, float)]:
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

