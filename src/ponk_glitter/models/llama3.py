from lib.glitter_models import GlitterGenerativeModel, register_model
from typing import Optional


#@register_model("llama3-8b-instruct")
class Robeczech(GlitterGenerativeModel):

    def __init__(self,
                 context_window_size: int = 512,
                 top_k: Optional[int] = 10):
        super().__init__(name="Llama-3-8B-Instruct",
                         lang="cs",
                         model_path="meta-llama/Meta-Llama-3-8B-Instruct",
                         context_window_size=context_window_size,
                         top_k=top_k)

@register_model("tiny-llama")
class Robeczech(GlitterGenerativeModel):

    def __init__(self,
                 context_window_size: int = 512,
                 top_k: Optional[int] = 10):
        super().__init__(name="TinyLlama-1.1B-Chat-v1.0",
                         lang="cs",
                         model_path="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                         context_window_size=context_window_size,
                         top_k=top_k)
