
PHONY: run


download-models:
	echo "Downloading models..."
	echo "\tRobeCzech"
	git clone https://huggingface.co/ufal/robeczech-base ./src/models/robeczech-base
	echo "\tGPT2-small-czech-cs"
	git clone https://huggingface.co/spital/gpt2-small-czech-cs ./src/models/gpt2-small-czech-cs


run:
	python preload_gpt2.py
	python server.py --address "0.0.0.0" --port "8000"

