SHELL=/usr/bin/sh
MAKEFLAGS += --silent

PHONY: run



install: pyproject.toml
	uv sync


run:
	cd ./src/ponk_glitter/ && uv run python server.py
