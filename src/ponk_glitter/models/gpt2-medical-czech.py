from lib.glitter_models import GlitterGenerativeModel, register_model


@register_model("gpt2-medical-czech")
class Robeczech(GlitterGenerativeModel):

    def __init__(self,
                 context_window_size: int = 512):
        super().__init__(name="GPT-2 medical Czech",
                         lang="cs",
                         model_path="lchaloupsky/czech-gpt2-medical",
                         context_window_size=context_window_size)
