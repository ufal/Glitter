SHELL=/usr/bin/sh
MAKEFLAGS += --silent

PHONY: run

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip



install: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt --upgrade


run: $(VENV)/bin/activate
	cd ./src/ponk_glitter/ && ../../$(PYTHON) server.py

