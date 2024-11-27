from lib.glitter_models import GlitterGenerativeModel, register_model


@register_model("gpt2-xl-czech")
class Robeczech(GlitterGenerativeModel):

    def __init__(self,
                 context_window_size: int = 1024,
                 top_k=None):
        super().__init__(name="GPT-2 XL Czech",
                         lang="cs",
                         model_path="BUT-FIT/Czech-GPT-2-XL-133k",
                         context_window_size=context_window_size,
                         top_k=top_k)
