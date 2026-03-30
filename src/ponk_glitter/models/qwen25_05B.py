from lib.glitter_models import GlitterGenerativeModel, register_model
from typing import Optional


@register_model("qwen25-05b")
class Qwen25_05B(GlitterGenerativeModel):
    """Qwen2.5-0.5B causal language model."""

    def __init__(
        self,
        context_window_size: int = 512,
        top_k: Optional[int] = 10,
    ) -> None:
        super().__init__(
            name="Qwen2.5-0.5B",
            lang="multilingual",
            model_path="Qwen/Qwen2.5-0.5B",
            context_window_size=context_window_size,
            top_k=top_k,
        )
