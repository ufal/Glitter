
PHONY: run

run:
	python preload_gpt2.py
	python server.py --address "0.0.0.0" --port "8000"

