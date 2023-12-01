.PHONY: build
build:
	pip install -e .

.PHONY: clean
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -name "*.pyc" -exec rm -f "{}" +
	find . -name ".DS_Store" -exec rm -f "{}" +
	find . -name "__pycache__" -exec rm -rf "{}" +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf "{}" +

