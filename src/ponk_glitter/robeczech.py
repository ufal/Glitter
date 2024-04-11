#!/usr/bin/env python3

from rich.progress import track
from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline, logging, AutoModelForCausalLM
from lib.glitter_common import GlitteredToken, GlitteredText
from lib.masked_context_window import MaskedContextWindow
from lib.glitter_common import GlitterModel

logging.set_verbosity(logging.CRITICAL)


class Robeczech(GlitterModel):

    def __init__(self,
                 context_window_size: int = 5,
                 top_k: int = 1000):
        super().__init__("Robeczech", "cs", context_window_size=context_window_size, sample_size=top_k)
        self.context_window_size = context_window_size
        self.top_k = top_k

        self.model = AutoModelForCausalLM.from_pretrained("models/robeczech")
        self.tokenizer = AutoTokenizer.from_pretrained("models/robeczech")
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
        for ot, mcw, _ in zip(split_text,
                              MaskedContextWindow(text, self.context_window_size),
                              track(range(len(split_text) + 1), description="Glittering...")):
            gt.append(self.glitter_masked_token(ot, mcw))
        return gt

    def generate_text(self, prompt, length=20, top_k=50):
        text = prompt
        for i in range(length):
            text += " " + self.pipe(text + " [MASK]", top_k=top_k)
        return text
