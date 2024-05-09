#!/usr/bin/env python3
from random import choice

from rich.progress import track
from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline, logging, TensorType

from lib.context_window import TokenizedMaskedContextWindow
from lib.glitter_common import GlitterModel
from lib.glitter_common import GlitteredToken, GlitteredText, convert_tokenized_text_to_tensor

logging.set_verbosity(logging.CRITICAL)

class Robeczech(GlitterModel):
    SPECIAL_TOKENS = ["[SEP]", "[CLS]"]
    MODEL_PATH = "models/robeczech-base"

    def __init__(self,
                 context_window_size: int = 5,
                 top_k: int = 1000):
        super().__init__("Robeczech", "cs", context_window_size=context_window_size, sample_size=top_k)
        self.context_window_size = context_window_size
        self.top_k = top_k
        self.model = AutoModelForMaskedLM.from_pretrained(self.MODEL_PATH)
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL_PATH)
        self.tokenizer.add_special_tokens({"additional_special_tokens": self.SPECIAL_TOKENS})
        self.pipe = pipeline('fill-mask', model=self.model, tokenizer=self.tokenizer)
        self.start_token = self.tokenizer.convert_tokens_to_ids("[CLS]")
        self.end_token = self.tokenizer.convert_tokens_to_ids("[SEP]")

    def glitter_masked_token(self, original_token: str,
                             masked_tokenized_text: {str: TensorType},
                             top_k: int = None) -> GlitteredToken:
        if top_k is None:
            top_k = self.top_k

        results = self.model(**masked_tokenized_text).logits
        probs = results.softmax(dim=2)
        probs = probs[0, -1, :].tolist()
        indexed_probs = [(index, p) for index, p in enumerate(probs)]
        indexed_probs.sort(key=lambda x: x[1], reverse=True)
        probs_top_k = indexed_probs[:top_k]
        str_prob = [(self.tokenizer.convert_ids_to_tokens([index])[0], p) for index, p in probs_top_k]
        print("Len prob", len(str_prob))
        return GlitteredToken(self.tokenizer.convert_tokens_to_string(original_token), str_prob)

    def glitter_text(self, text: str) -> GlitteredText:
        gt = GlitteredText(models=["Robeczech"])
        tokenized_text = self.tokenizer(text)
        mask_token = self.tokenizer.convert_tokens_to_ids("[MASK]")

        for ot, tmcw in track(zip(tokenized_text,
                                  TokenizedMaskedContextWindow(
                                      tokenized_text,
                                      self.context_window_size,
                                      mask_token=mask_token
                                  )),
                              description="Glittering...",
                              total=len(tokenized_text)):
            tensorified_tmcw = convert_tokenized_text_to_tensor(tmcw)
            gt.append(self.glitter_masked_token(ot, tensorified_tmcw, top_k=self.top_k))
        return gt

    def generate_text(self, prompt: str, length: int = 20, top_k: int = 50) -> str:
        text = prompt
        for _ in track(range(length), description="Generating...", total=length):
            new_token = choice(self.pipe(text + " [MASK]", top_k=top_k))["token_str"]
            text += " " if new_token == "[SEP]" else new_token
        for st in self.SPECIAL_TOKENS:
            text = text.replace(st, "")
        return text
