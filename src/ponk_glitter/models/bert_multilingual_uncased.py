from lib.glitter_models import GlitterUnmaskingModel, register_model
from lib.glitter_common import normalize_glittered_text_with_subword_tokens
from unidecode import unidecode
from typing import Optional

@register_model("bert-multilingual-uncased")
class BertMultilingualUncased(GlitterUnmaskingModel):

    def __init__(self,
                 context_window_size: int = 100,
                 top_k: Optional[int] = None):

        super().__init__(name="Bert multilingual uncased",
                         lang="multilingual",
                         model_path="models/bert-base-multilingual-uncased",
                         context_window_size=context_window_size,
                         top_k=top_k)

        self.__glittered_text_postprocessing__ = normalize_glittered_text_with_subword_tokens

    def __text_preprocessing__(self, text: str) -> str:
        return unidecode(text.lower())
