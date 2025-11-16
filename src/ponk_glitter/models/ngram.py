from lib.glitter_models import GlitterNgramModel, register_model
from typing import Optional


@register_model("ngram5")
class Ngram(GlitterNgramModel):

    def __init__(self,
                 context_window_size: int = 10,
                 top_k: Optional[int] = 10) -> None:
        super().__init__(name="Ngram-5",
                         lang="cs",
                         model_path="../../models/czech.blm",
                         context_window_size=context_window_size,
                         top_k=top_k)
