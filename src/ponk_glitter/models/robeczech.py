from lib.glitter_models import GlitterUnmaskingModel, register_model
from typing import Optional


@register_model("robeczech")
class Robeczech(GlitterUnmaskingModel):

    def __init__(self,
                 context_window_size: int = 100,
                 top_k: Optional[int] = None):
        super().__init__(name="Robeczech",
                         lang="cs",
                         model_path="models/robeczech-base",
                         context_window_size=context_window_size,
                         top_k=top_k)
