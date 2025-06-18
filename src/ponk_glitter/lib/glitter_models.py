from random import choice
from typing import Optional

import torch
from rich import print
from rich.progress import track
from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline, logging, TensorType, AutoModelForCausalLM
from datetime import datetime

from lib.context_window import TokenizedMaskedContextWindow, GPTContextWindow
from lib.glitter_common import *

logging.set_verbosity(logging.CRITICAL)

AVAILABLE_MODELS = {}
PUNCTUATION = (" ",".",",","?","!",":",";","'",'"')


def register_model(name):
    def decorator(cls):
        # print(f" * Registered model {cls} with name {name}")
        AVAILABLE_MODELS[name] = cls
        return cls

    return decorator


def get_registered_models():
    from os import listdir
    for module in listdir("models"):
        if module == "__init__.py" or module[-3:] != ".py":
            continue
        __import__(f"models.{module[:-3]}", locals(), globals())
    return AVAILABLE_MODELS


def load_models(verbose=False):
    get_registered_models()
    models = dict()
    if verbose:
        print(" * Models loaded:")
    for model_name in AVAILABLE_MODELS.keys():
        try:
            model = AVAILABLE_MODELS[model_name]()
            models[model.name] = model
            if verbose:
                print(f"   - {model.name} ({model.device})")
        except Exception as e:
            if verbose:
                print(f"   - {model_name} failed to load: {e}")
    if len(models) == 0 and verbose:
        print(" * No models loaded.")
    return models


class GlitterModel:
    """
    Base class for Glitter models. All Glitter models should inherit from this class.
    """

    def __init__(self, name: str,
                 lang: str,
                 context_window_size: Optional[int] = 1024,
                 sample_size: Optional[int] = 1000) -> None:
        self.name: str = name
        self.lang: str = lang
        self.context_window_size: int = context_window_size
        self.top_k: int = sample_size
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_type = "base"

    def glitter_text(self, text: str, silent=False) -> GlitteredText:
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

    @staticmethod
    def __glittered_text_postprocessing__(glittered_text: GlitteredText) -> GlitteredText:
        return glittered_text


def categorize_models(models: Dict[str, GlitterModel]) -> Dict[str, List[GlitterModel]]:
    categorized_models = dict()

    for model_name in models.keys():
        model = models[model_name]
        if model.model_type not in categorized_models:
            categorized_models[model.model_type] = []
        categorized_models[model.model_type].append(model)

    for model_type in categorized_models.keys():
        categorized_models[model_type] = sorted(categorized_models[model_type], key=lambda x: x.name)

    return categorized_models


class GlitterUnmaskingModel(GlitterModel):
    """
    Base class for Glitter models of the unmasking type.
    """

    def __init__(self, name: str,
                 lang: str,
                 model_path: str,
                 context_window_size: int = 100,
                 top_k=None
                 ) -> None:
        super().__init__(name,
                         lang,
                         context_window_size,
                         top_k)
        self.model_type = "unmasking"
        self.model_path = model_path
        self.model = AutoModelForMaskedLM.from_pretrained(model_path)  # .to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.pipeline = pipeline("fill-mask", model=self.model, tokenizer=self.tokenizer)

        if top_k is None:
            top_k = self.model.config.vocab_size
        self.top_k = top_k

    # @cache # dict is not hashable
    def glitter_masked_token(self, original_token: int,
                             masked_tokenized_text: {str: TensorType},
                             top_k: int) -> GlitteredToken:
        masked_tokenized_text = convert_tokenized_text_to_tensor(masked_tokenized_text)
        with torch.no_grad():
            results = self.model(**masked_tokenized_text).logits
            normalized_results = results.softmax(dim=-1)
            # Shape: Batch x Seq len x Vocab size
            probs = normalized_results[0, -1, :]

        original_token_str = self.tokenizer.decode(original_token)
        sorted_tokens = get_tokens_sorted_by_probability(probs, self.tokenizer)
        nth, prob = get_order_and_probability_of_original_token(original_token_str, sorted_tokens)
        top_tokens = sorted_tokens[:top_k]
        return GlitteredToken(original_token_str, nth, prob, top_tokens)

    def glitter_text(self, text: str, top_k: int = None, silent=False) -> GlitteredText:
        text = self.__text_preprocessing__(text)
        if top_k is None:
            top_k = self.top_k
        # Create a new empty GlitteredText object
        gt = GlitteredText(models=[self.name])
        tokenized_text = self.tokenizer(text)["input_ids"]
        mask_token = self.tokenizer.convert_tokens_to_ids("[MASK]")

        iterator = zip(tokenized_text,
                       TokenizedMaskedContextWindow(
                           tokenized_text,
                           self.context_window_size,
                           mask_token=mask_token))
        if not silent:
            iterator = track(iterator, description="Glittering...", total=len(tokenized_text))

        for ot, tmcw in iterator:
            gt.append(self.glitter_masked_token(ot, tmcw, top_k=top_k))
        return self.__glittered_text_postprocessing__(gt)

    def generate_text(self, prompt: str, length: int = 20, top_k: int = 50) -> str:
        text = prompt
        for _ in track(range(length), description="Generating...", total=length):
            new_token = choice(self.model.pipe(text + " [MASK]", top_k=top_k))["token_str"]
            text += " " if new_token == "[SEP]" else new_token
        return text


class GlitterGenerativeModel(GlitterModel):
    """
    Base class for Glitter models of the GPT type.
    WIP
    """

    def __init__(self, name: str,
                 lang: str,
                 model_path: str,
                 context_window_size: int = None,
                 top_k: Optional[int] = None
                 ) -> None:
        super().__init__(name,
                         lang,
                         context_window_size,
                         top_k)
        self.model_type = "generative"
        self.model_path = model_path
        self.model = AutoModelForCausalLM.from_pretrained(model_path).eval()
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.top_k = self.tokenizer.vocab_size
        if context_window_size is None:
            # set to the maximum possible value (n_positions)
            self.context_window_size = self.model.config.n_positions

    def glitter_window(self,
                       tokenized_text: {str: torch.Tensor},
                       n_last_related_tokens: int,
                       top_k: int) -> List[GlitteredToken]:
        print(f"Window length: {len(tokenized_text['input_ids'])}")
        # Move to GPU if available
        self.model.to(self.device)
        tokenized_text = {k: v.to(self.device) for k, v in tokenized_text.items()}
        # Forward pass through the model to get logits
        with torch.no_grad():  # Disable gradient calculation for faster inference
            outputs = self.model(**tokenized_text)  # this is 2D
            glittered_window = []
            for i in reversed(range(0, n_last_related_tokens-1)):
                if -i - 2 <= -self.context_window_size:
                    continue
                logits = outputs.logits[-i - 2, :].detach().cpu()
                probs = torch.nn.functional.softmax(logits, dim=-1)
                sorted_tokens = get_tokens_sorted_by_probability(probs, self.tokenizer)
                original_token = self.tokenizer.decode(tokenized_text["input_ids"][-(i + 1)].item())
                nth, prob = get_order_and_probability_of_original_token(original_token, sorted_tokens)
                top_tokens = sorted_tokens[:top_k]
                if not original_token.startswith(PUNCTUATION)and glittered_window:
                    last_token = glittered_window.pop()
                    prob = last_token.probability * prob 
                    original_token = last_token.original_token + original_token 
                    nth = get_approx_order_from_probability(prob, sorted_tokens)
                    top_tokens = last_token.top_k_tokens
                elif not glittered_window and not original_token.startswith(" ") and not glittered_window:
                    nth = 1
                    prob = 1.0
                    

                glittered_window.append(GlitteredToken(original_token, nth, prob, top_tokens))
        return glittered_window


    def glitter_text(self, text: str, top_k: int = None, silent=False) -> GlitteredText:
        start = datetime.now()
        print(f"Started {start}")
        text = self.__text_preprocessing__(text)
        if top_k is None:
            top_k = self.top_k
        # Create a new empty GlitteredText object
        gt = GlitteredText(models=[self.name])

        tokenized_text = self.tokenizer.encode(text, return_tensors="pt")[-1]

        # Add first token
        gt.append(GlitteredToken(self.tokenizer.decode(tokenized_text[0].item()), 1, 1.0, []))

        iterator = GPTContextWindow(tokenized_text, self.context_window_size)
        if not silent:
            iterator = track(iterator, description="Glittering...", total=len(tokenized_text))

        for last_n_tokens, cw in iterator:
            glittered_window = self.glitter_window(convert_list_of_tokens_to_tensor(cw),
                                                   last_n_tokens,
                                                   top_k=top_k)
            for token in glittered_window:
                gt.append(token)

        end = datetime.now()
        print(f"Finished {end}")
        print(f"Gliiering took {end-start} seconds.")
        return self.__glittered_text_postprocessing__(gt)
