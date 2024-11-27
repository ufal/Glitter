SHELL=/usr/bin/sh
MAKEFLAGS += --silent
PHONY: run

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip


$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -r requirements.txt


run: $(VENV)/bin/activate
	cd ./src/ponk_glitter/ && ../../$(PYTHON) server.py

