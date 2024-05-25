#!/usr/bin/env python3
from random import choice

from rich.progress import track
from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline, logging, TensorType
import torch
from functools import cache

from lib.context_window import TokenizedMaskedContextWindow
from lib.glitter_common import GlitterModel, get_top_k_tokens
from lib.glitter_common import GlitteredToken, GlitteredText, convert_tokenized_text_to_tensor

logging.set_verbosity(logging.CRITICAL)

class Robeczech(GlitterModel):
    SPECIAL_TOKENS = ["[SEP]", "[CLS]"]
    MODEL_PATH = "models/robeczech-base"

    def __init__(self,
                 context_window_size: int = 100,
                 top_k: int = None):
        super().__init__("Robeczech", "cs", context_window_size=context_window_size, sample_size=top_k)
        self.context_window_size = context_window_size
        self.model = AutoModelForMaskedLM.from_pretrained(self.MODEL_PATH)
        if top_k is None:
            top_k = self.model.config.vocab_size
        self.top_k = top_k
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL_PATH)
        self.tokenizer.add_special_tokens({"additional_special_tokens": self.SPECIAL_TOKENS})
        self.pipe = pipeline("fill-mask", model=self.model, tokenizer=self.tokenizer)
        self.start_token = self.tokenizer.convert_tokens_to_ids("[CLS]")
        self.end_token = self.tokenizer.convert_tokens_to_ids("[SEP]")


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
        if top_k is None:
            top_k = self.top_k
        # Create a new empty GlitteredText object
        gt = GlitteredText(models=["Robeczech"])
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

