SHELL=/usr/bin/sh
MAKEFLAGS += --silent
PHONY: run


download-models:
	echo "Downloading models..."
	echo "    Robeczech"
	git clone https://huggingface.co/ufal/robeczech-base ./src/ponk_glitter/models/robeczech-base
	echo "    BERT base multilingual uncased"
	git clone https://huggingface.co/google-bert/bert-base-multilingual-uncased ./src/ponk_glitter/models/bert-base-multilingual-uncased


install:
	pip install -r requirements.txt


run:
	python ./src/ponk_glitter/server.py --host "0.0.0.0" --port "8000"

