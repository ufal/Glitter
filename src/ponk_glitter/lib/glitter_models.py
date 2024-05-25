from typing import List

from torch import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline, logging, TensorType
from rich.progress import track
from lib.glitter_common import *
from lib.context_window import TokenizedMaskedContextWindow


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

    def __text_preprocessing__(self, text: str) -> str:
        return text


class GlitterUnmaskingModel(GlitterModel):

    def __init__(self, name: str, lang: str, context_window_size: int = 5, sample_size: int = 1000) -> None:
        super().__init__(name, lang, context_window_size, sample_size)


    #@cache # dict is not hashable
    def glitter_masked_token(self, original_token: int,
                             masked_tokenized_text: {str: TensorType},
                             top_k:int ) -> GlitteredToken:
        masked_tokenized_text = convert_tokenized_text_to_tensor(masked_tokenized_text)
        with torch.no_grad():
            results = self.model(**masked_tokenized_text).logits
            normalized_results = results.softmax(dim=-1)
            # Shape: Batch x Seq len x Vocab size
            probs = normalized_results[0, -1, :].tolist()

        top_tokens = get_top_k_tokens(probs, self.tokenizer, top_k)
        return GlitteredToken(self.tokenizer.decode(original_token), top_tokens)


    def glitter_text(self, text: str, top_k:int=None) -> GlitteredText:
        text = self.__text_preprocessing__(text)
        if top_k is None:
            top_k = self.top_k
        # Create a new empty GlitteredText object
        gt = GlitteredText(models=[self.name])
        tokenized_text = self.tokenizer(text)["input_ids"]
        mask_token = self.tokenizer.convert_tokens_to_ids("[MASK]")

        for ot, tmcw in track(zip(tokenized_text,
                                  TokenizedMaskedContextWindow(
                                      tokenized_text,
                                      self.context_window_size,
                                      mask_token=mask_token
                                  )),
                              description="Glittering...",
                              total=len(tokenized_text)):
            gt.append(self.glitter_masked_token(ot, tmcw, top_k=top_k))
        return gt



    def generate_text(self, prompt: str, length: int = 20, top_k: int = 50) -> str:
        text = prompt
        for _ in track(range(length), description="Generating...", total=length):
            new_token = choice(self.pipe(text + " [MASK]", top_k=top_k))["token_str"]
            text += " " if new_token == "[SEP]" else new_token
        for st in self.SPECIAL_TOKENS:
            text = text.replace(st, "")
        return text


