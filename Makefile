SHELL=/usr/bin/sh
MAKEFLAGS += --silent
PHONY: run

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip


download-models:
	echo "Downloading models..."
	echo "    Robeczech"
	git clone https://huggingface.co/ufal/robeczech-base ./src/ponk_glitter/models/robeczech-base
	echo "    BERT base multilingual uncased"
	git clone https://huggingface.co/google-bert/bert-base-multilingual-uncased ./src/ponk_glitter/models/bert-base-multilingual-uncased
	echo "    Clonning FERNET"
	git clone https://huggingface.co/fav-kky/FERNET-C5 ./src/ponk_glitter/models/FERNET-C5


$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -r requirements.txt


run: $(VENV)/bin/activate
	cd ./src/ponk_glitter/ && ../../$(PYTHON) server.py --host "0.0.0.0" --port "8000"

