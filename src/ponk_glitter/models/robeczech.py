#!/usr/bin/env python3
from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline, logging, TensorType
import torch

from lib.glitter_models import GlitterUnmaskingModel

logging.set_verbosity(logging.CRITICAL)

class Robeczech(GlitterUnmaskingModel):
    SPECIAL_TOKENS = ["[SEP]", "[CLS]"]
    MODEL_PATH = "models/robeczech-base"

    def __init__(self,
                 context_window_size: int = 100,
                 top_k: int = None):
        super().__init__(name="Robeczech",
                         lang="cs",
                         context_window_size=context_window_size,
                         sample_size=top_k)
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



