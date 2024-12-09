from lib.glitter_models import GlitterUnmaskingModel, register_model
from lib.glitter_common import normalize_glittered_text_with_subword_tokens
from typing import Optional


@register_model("fernet")
class Robeczech(GlitterUnmaskingModel):

    def __init__(self,
                 context_window_size: int = 100,
                 top_k: Optional[int] = 10):

        super().__init__(name="Fernet",
                         lang="cs",
                         model_path="fav-kky/FERNET-C5",
                         context_window_size=context_window_size,
                         top_k=top_k)
        self.__glittered_text_postprocessing__ = normalize_glittered_text_with_subword_tokens
