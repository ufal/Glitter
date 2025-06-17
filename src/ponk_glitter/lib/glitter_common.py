import html
import json
from typing import List, Tuple, Dict, Optional
from conllu import parse_incr
from collections import deque

from jinja2 import Template
from torch import torch


class GlitteredToken:
    """
    This class represents a token that has been glittered by a model.
    It contains the original token, the probability of the token, the position of the token in the top-k list
    """
    HEATMAP_CATEGORIES = tuple(enumerate([1, 3, 5, 10, 15, 25, 50, 75, 100,
                                          250, 500, 1000, 5000, 10000, 15000, 20000]))
    SIMPLE_CATEGORY = ((0, 1), (3, 10), (7, 100), (10, 1000), (14, 10000))
    # from cold to hot
    HEATMAP_TERMINAL_COLORS = ["blue1", "dodger_blue1", "deep_sky_blue3", "cyan1",
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

    def __init__(self, original_token: str, nth: int, probability: float, top_k_tokens: List[Tuple[str, float]]):
        self.probability = probability
        self.original_token = original_token
        self.top_k_tokens = top_k_tokens
        self.nth = nth
        self.top_k = len(top_k_tokens)
        self.surprisal = self.__get_heatmap_color_index__() + 1

    def to_dict(self) -> Dict:
        return {
            "original_token": self.original_token,
            "probability": self.probability,
            "nth": self.nth,
            "top_5": self.top_k_tokens[:5]
        }

    def __get_heatmap_color_index__(self, color_map=HEATMAP_CATEGORIES) -> int:
        color_index = 15
        for i, category in color_map:
            if self.nth <= category:
                color_index = i
                break
        return color_index

    def to_html(self, color_mode="heatmap") -> str:
        color_mode = color_mode.lower()
        if color_mode == "simple":
            color_map = self.SIMPLE_CATEGORY
        else:
            color_map = self.HEATMAP_CATEGORIES

        color_index = self.__get_heatmap_color_index__(color_map)

        # Render the template with the context
        output = Template(self.__HTML_TEMPLATE).render(
            heatmap_color_index=color_index,
            original_token=html.escape(self.original_token).replace(" ", "&nbsp;"),
            probability=f"{self.probability:.8f}",
            nth=self.nth,
            data=[f"{html.escape(token)} ({prob:.8f})" for token, prob in self.top_k_tokens[:5]]
        )

        return output

    def to_tex(self) -> str:
        return f"\\hm{'ABCDEFGHIJKLMNOP'[self.__get_heatmap_color_index__()]}{{{self.original_token}}}"

    def __str__(self) -> str:
        # rich color output
        return f"[{self.HEATMAP_TERMINAL_COLORS[self.__get_heatmap_color_index__()]}]{self.original_token}[/]"


class GlitteredText:
    """
    This class represents a text that has been glittered by a model.
    It contains a list of GlitteredToken objects and the models that have been used to glitter the text.
    """

    def __init__(self, models: List[str]):
        self.used_models = models
        self.content: List[GlitteredToken] = list()
        self.used_models: List[str] = list()

    def append(self, token: GlitteredToken) -> None:
        self.content.append(token)

    def get_content(self) -> List[GlitteredToken]:
        return self.content

    def find_token(self, conllu_token,  start_from, finish_at):
        start_from = min(start_from, len(self.content) - 1)
        finish_at = min(finish_at, len(self.content) - 1)
        for i, tok in enumerate(self.content[start_from:finish_at]):
            if tok.original_token.strip() == conllu_token["form"].strip():
                return tok, i + start_from
        print("WARNING: Token '{conllu_token['form']}' not found in Glittered text, moving to next token")
        return None, start_from

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_html(self, color_mode="heatmap") -> str:
        output = '<div class="glittered-text">'
        for token in self.content:
            output += token.to_html(color_mode)
        return output + "</div>"

    def to_dict(self):
        return {
            "content": [token.to_dict() for token in self.content],
            "used_models": self.used_models
        }

    def to_tex(self):
        return "".join([token.to_tex() for token in self.content])

    def to_conllu(self, conllu_data):
        output = ""
        start_from = 0
        finish_at = 5
        for sentence in conllu_data:
            for conllu_token in sentence:
                glittered_token, pos = self.find_token(conllu_token, start_from, finish_at)
                if glittered_token:
                    conllu_token["misc"]["PonkApp2:Surprisal"] = glittered_token.surprisal
                    conllu_token["misc"]["PonkApp2:Prob"] = "%.5f" % glittered_token.probability
                    conllu_token["misc"]["PonkApp2:VocabRank"] = glittered_token.nth
                    start_from = pos + 1
                    finish_at += 1
            output += sentence.serialize()
        return output
    

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
    """
    Convert a tokenized text to a Pytorch tensor
    """
    return {key: torch.tensor([value]) for key, value in tokenized_text.items()}


def convert_list_of_tokens_to_tensor(tokenized_text: torch.Tensor) -> Dict[str, torch.Tensor]:
    """
    Convert a list of tokens to a Pytorch tensor
    """
    if type(tokenized_text) is torch.Tensor:
        return {"input_ids": tokenized_text, "attention_mask": torch.ones(len(tokenized_text))}
    print("Warning: convert list received list type (not torch.Tensor), this is inefficient")
    return {"input_ids": torch.tensor(tokenized_text), "attention_mask": torch.ones(len(tokenized_text))}


def get_tokens_sorted_by_probability(logits: torch.Tensor,
                                     tokenizer,
                                     top_k: Optional[int] = None) -> List[Tuple[str, float]]:
    if top_k is None:
        top_k = len(logits)
    top_probs, top_indices = torch.topk(logits,
                                        largest=True,
                                        sorted=True,
                                        k=top_k)
    decoded_tokens = tokenizer.batch_decode([[idx] for idx in top_indices.tolist()])
    return [(token, prob.item()) for token, prob in zip(decoded_tokens, top_probs)]


def get_top_k_tokens(logits: torch.Tensor, tokenizer, top_k: int, ) -> List[Tuple[str, float]]:
    # Get the probabilities of the last token
    indexed_probs = get_tokens_sorted_by_probability(logits, tokenizer)
    # Get the top k probabilities
    probs_top_k = indexed_probs[:top_k]
    return probs_top_k


def get_order_and_probability_of_original_token(original_token: str, tokens: List[Tuple[str, float]]):
    for i, (token, prob) in enumerate(tokens):
        if token == original_token:
            return i, prob
    return -1, 0.0


def get_approx_order_from_probability(prob: float, tokens: List[Tuple[str, float]]):
    for i, (token, approx_prob) in enumerate(tokens):
        if prob > approx_prob:
            return i
    return i


def normalize_glittered_text_with_subword_tokens(glittered_text: GlitteredText) -> GlitteredText:
    """
    Normalize the GlitteredText object by removing the '##' from the subword tokens
    and adding a space before the token.
    """
    for token in glittered_text.get_content():
        if token.original_token.startswith("##"):
            token.original_token = token.original_token[2:]
        else:
            token.original_token = " " + token.original_token
    return glittered_text
