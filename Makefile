.PHONY: run-test

all:

run-test:
	pipenv run python3 -m pytest -s -v .
