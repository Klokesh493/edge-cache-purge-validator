PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) purge_validator.py sample_purges.csv
