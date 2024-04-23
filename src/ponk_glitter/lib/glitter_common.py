from typing import List
from torch import torch


# {'score': 0.12831833958625793, 'token': 14064, 'token_str': ' všední', 'sequence': 'Dneska je všední den.'}
class GlitteredToken:

    def __init__(self, original_token, raw_values):
        self.data = raw_values
        self.probability = 0
        self.original_token = original_token
        self.nth = -1
        for n, value in enumerate(raw_values, start=1):
            if value["token_str"] == original_token:
                self.probability = value["score"]
                self.nth = n


class GlitteredText:
    content: List[GlitteredToken] = list()
    used_models: List[str] = list()

    def __init__(self, models: List[str]):
        self.used_models = models

    def append(self, token: GlitteredToken) -> None:
        self.content.append(token)

    def get_content(self) -> List[GlitteredToken]:
        return self.content


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
