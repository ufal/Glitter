# Model interface
Glitter is very extensible by design so you can easily add support for new models.
This is a tutorial how to add new models:

## Unmasking models
Create `.py` file in `src/models/` directory. It should contain a name of a model
you trying to add. File has to follow this template:

```py
# Unique model identificator. This will be used a key under which can be model class accessed
@register_model("model-identificator")
class ModelClass(GlitterUnmaskingModel):

    def __init__(self,
                 context_window_size: int = 100,
                 top_k: int = None):

        super().__init__(name="Model name",                        # Modela name in human readable format
                         lang="cs",                                # Language on which model was trained
                         model_path="models/robeczech-base",       # Path from projects root to directory wi model files
                         context_window_size=context_window_size,  # Size of default context window
                         top_k=top_k)                              # Size of list with top results (if is None than it is set to size of model vocab)
```

There are also special functions. Their implementation is not mandatory:

- `__text_preprocessing__(self, text: str) -> str` - this method will be applied to any text before glittering
- `__glittered_text_postprocessing__(self, glittered_text: GlitteredText) -> GlitteredText` - this method will be applied on Glittered text right after Glittering is finished

