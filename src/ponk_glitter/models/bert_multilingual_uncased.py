from lib.glitter_models import GlitterUnmaskingModel, register_model
from unidecode import unidecode

@register_model("bert_multilingual_uncased")
class BertMultilingualUncased(GlitterUnmaskingModel):

    def __init__(self,
                 context_window_size: int = 100,
                 top_k: int = None):

        super().__init__(name="Bert multilingual uncased",
                         lang="multilingual",
                         model_path="models/bert-base-multilingual-uncased",
                         context_window_size=context_window_size,
                         top_k=top_k)


    def __text_preprocessing__(self, text: str) -> str:
        return unidecode(text.lower())
