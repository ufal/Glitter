# **PONK:** Glitter
Glitter is set of tools for visualising lexical surprise by analysing entropy of outputs
of large language models. This can be used for research of text readability.

## Usage
- `make download-models` - downloads natively supported models
- `make`/`make run` - runs glitter server on localhost with port 4000


## Documetation
- ### [Glitter CLI](https://gitlab.mff.cuni.cz/teaching/nprg045/kvapilikova/ponk-glitter/-/blob/master/docs/glitter_cli.md?ref_type=heads)
- ### [Glitter server](https://gitlab.mff.cuni.cz/teaching/nprg045/kvapilikova/ponk-glitter/-/blob/master/docs/glitter_server.md?ref_type=heads)
- ### [Model interface](https://gitlab.mff.cuni.cz/teaching/nprg045/kvapilikova/ponk-glitter/-/blob/master/docs/model_interface.md?ref_type=heads)


## Models
Currently natively supported models:
- [Robeczech base](https://huggingface.co/ufal/robeczech-base)
- [BERT base model (uncased)](https://huggingface.co/google-bert/bert-base-uncased)
- [FERNET C5](https://huggingface.co/fav-kky/FERNET-C5)

For automatic model download run `make download-models` in project root directory.


## License
All code is licensed under [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html)

