from lib.glitter_models import GlitterGenerativeModel, register_model


@register_model("gpt2")
class Robeczech(GlitterGenerativeModel):

    def __init__(self,
                 context_window_size: int = 1024):
        super().__init__(name="GPT-2",
                         lang="en",
                         model_path="gpt2",
                         context_window_size=context_window_size)
