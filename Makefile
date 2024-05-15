SHELL=/usr/bin/sh
MAKEFLAGS += --silent
PHONY: run


download-models:
	echo "Downloading models..."
	echo "    RobeCzech"
	git clone https://huggingface.co/ufal/robeczech-base ./src/ponk_glitter/models/robeczech-base
	echo "    GPT2-small-czech-cs"
	git clone https://huggingface.co/spital/gpt2-small-czech-cs ./src/ponk_glitter/models/gpt2-small-czech-cs


install:
	pip install -r requirements.txt


run:
	python server.py --host "0.0.0.0" --port "8000"

