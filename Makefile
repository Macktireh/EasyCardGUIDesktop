.PHONY: run rufffix ruffformat ruff clean

.DEFAULT_GOAL := run

run:
	poetry run python main.py

rufffix:
	poetry run ruff --fix --exit-zero .

ruffformat:
	poetry run ruff format .

ruff:
	poetry run ruff check .

clean: rufffix ruffformat ruff
