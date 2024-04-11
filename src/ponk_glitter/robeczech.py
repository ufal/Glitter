#!/usr/bin/env python3
from random import choice

from rich.progress import track
from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline, logging, AutoModelForCausalLM

from lib.glitter_common import GlitterModel
from lib.glitter_common import GlitteredToken, GlitteredText
from lib.masked_context_window import MaskedContextWindow

logging.set_verbosity(logging.CRITICAL)


class Robeczech(GlitterModel):
    SPECIAL_TOKENS = ["[SEP]", "[CLS]"]

    def __init__(self,
                 context_window_size: int = 5,
                 top_k: int = 1000):
        super().__init__("Robeczech", "cs", context_window_size=context_window_size, sample_size=top_k)
        self.context_window_size = context_window_size
        self.top_k = top_k
        self.model = AutoModelForCausalLM.from_pretrained("models/robeczech")
        self.tokenizer = AutoTokenizer.from_pretrained("models/robeczech")
        self.tokenizer.add_special_tokens({"additional_special_tokens": self.SPECIAL_TOKENS})
        self.model = AutoModelForMaskedLM.from_pretrained("models/robeczech")
        self.pipe = pipeline('fill-mask', model=self.model, tokenizer=self.tokenizer)

    def glitter_masked_token(self, original_token: str, masked_text: str, top_k: int = None) -> GlitteredToken:
        if top_k is None:
            top_k = self.top_k

        results = self.pipe(masked_text, top_k=top_k)
        return GlitteredToken(original_token, results)

    def glitter_text(self, text: str) -> GlitteredText:
        gt = GlitteredText(models=["Robeczech"])
        split_text = text.split()
        for ot, mcw in track(zip(split_text,
                                    MaskedContextWindow(text, self.context_window_size)),
                                description="Glittering...",
                                total=len(split_text)):
            gt.append(self.glitter_masked_token(ot, mcw))
        return gt

    def generate_text(self, prompt: str, length: int = 20, top_k: int = 50) -> str:
        text = prompt
        for i in track(range(length), description="Generating...", total=length):
            new_token = choice(self.pipe(text + " [MASK]", top_k=top_k))["token_str"]
            text += " " if new_token == "[SEP]" else new_token
        for st in self.SPECIAL_TOKENS:
            text = text.replace(st, "")
        return text
