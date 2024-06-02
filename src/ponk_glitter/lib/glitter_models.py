from random import choice

from rich import print
from rich.progress import track
from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline, logging, TensorType

from lib.context_window import TokenizedMaskedContextWindow
from lib.glitter_common import *

logging.set_verbosity(logging.CRITICAL)

AVAILABLE_MODELS = {}


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
    del module
    return AVAILABLE_MODELS


def load_models(logging=False):
    get_registered_models()
    models = dict()
    if logging:
        print(" * Models loaded:")
    for model_name in AVAILABLE_MODELS.keys():
        model = AVAILABLE_MODELS[model_name]()
        models[model.name] = model
        if logging:
            print(f"   - {model.name}")
    if len(models) == 0 and logging:
        print(" * No models loaded.")
    return models


class GlitterModel:
    """
    Base class for Glitter models. All Glitter models should inherit from this class.
    """

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

    def __glittered_text_postprocessing__(self, glittered_text: GlitteredText) -> GlitteredText:
        return glittered_text


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
            probs = normalized_results[0, -1, :].tolist()

        top_tokens = get_top_k_tokens(probs, self.tokenizer, top_k)
        return GlitteredToken(self.tokenizer.decode(original_token), top_tokens)

    def glitter_text(self, text: str, top_k: int = None) -> GlitteredText:
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
        return self.__glittered_text_postprocessing__(gt)

    def generate_text(self, prompt: str, length: int = 20, top_k: int = 50) -> str:
        text = prompt
        for _ in track(range(length), description="Generating...", total=length):
            new_token = choice(self.pipe(text + " [MASK]", top_k=top_k))["token_str"]
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
                 context_window_size: int = 100,
                 top_k=None
                 ) -> None:
        super().__init__(name,
                         lang,
                         context_window_size,
                         top_k)
        self.model_type = "generative"
        self.model_path = model_path
