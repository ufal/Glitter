from typing import List

from flask import jsonify
from torch import torch


class GlitteredToken:

    def __init__(self, original_token: str, raw_values):
        self.probability = 0
        self.original_token = original_token
        self.data = raw_values
        self.nth = -1
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
        }

    def to_html(self):
        output = f"<span class='glittered-token'>{self.original_token}</span>"
        return output


class GlitteredText:
    content: List[GlitteredToken] = list()
    used_models: List[str] = list()

    def __init__(self, models: List[str]):
        self.used_models = models

    def append(self, token: GlitteredToken) -> None:
        self.content.append(token)

    def get_content(self) -> List[GlitteredToken]:
        return self.content

    def to_json(self):
        return jsonify({
            "content": [token.to_dict() for token in self.content],
            "used_models": self.used_models
        })

    def to_html(self) -> str:
        output = ""
        for token in self.content:
            output += token.to_html()
        return output


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

