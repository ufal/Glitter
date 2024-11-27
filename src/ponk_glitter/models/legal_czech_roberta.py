from lib.glitter_models import GlitterUnmaskingModel, register_model
from typing import Optional


@register_model("legal-czech-roberta")
class Robeczech(GlitterUnmaskingModel):

    def __init__(self,
                 context_window_size: int = 100,
                 top_k: Optional[int] = None):
        super().__init__(name="Legal Czech RoBERTa",
                         lang="cs",
                         model_path="joelniklaus/legal-czech-roberta-base",
                         context_window_size=context_window_size,
                         top_k=top_k)

