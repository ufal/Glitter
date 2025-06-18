# **PONK:** Glitter
Glitter is set of tools for visualising lexical surprise by analysing entropy of outputs
of large language models. This can be used for research of text readability.

PONK project: [ufal.mff.cuni.cz/ponk](https://ufal.mff.cuni.cz/ponk)

## Usage
- `make`/`make run` - runs glitter server on _localhost_ with port _4000_


## Documentation
- [Glitter CLI](https://github.com/ufal/Glitter/blob/master/docs/glitter_cli.md)
- [Glitter server](https://github.com/ufal/Glitter/blob/master/docs/glitter_server.md)
- [Model interface](https://github.com/ufal/Glitter/blob/master/docs/model_interface.md)


## Models
Currently natively supported models:
- [Robeczech (base)](https://huggingface.co/ufal/robeczech-base)
- [BERT base model (uncased)](https://huggingface.co/google-bert/bert-base-uncased)
- [FERNET C5](https://huggingface.co/fav-kky/FERNET-C5)
- [Czech GPT2 XL](https://huggingface.co/BUT-FIT/Czech-GPT-2-XL-133k)
- [Czech GPT2 medical](https://huggingface.co/lchaloupsky/czech-gpt2-medical)
- [GPT2](https://huggingface.co/openai-community/gpt2)
- [Legal Czech Roberta (base)](https://huggingface.co/joelniklaus/legal-czech-roberta-base)

Glitter will look for models locally first. If some model is not available it will
download it automatically.


## License
All code is licensed under [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html)

