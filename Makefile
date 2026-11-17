SHELL := /bin/sh

.PHONY: test evidence lab serve

test:
	python -m unittest discover -s tests -v

evidence:
	python scripts/validate_evidence.py

lab:
	python -m rotation.lab

serve:
	python -m http.server 8000
