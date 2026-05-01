.PHONY: setup test check run clean format lint

setup:
	pip install pytest mypy black isort pre-commit
	pre-commit install

test:
	pytest

check: lint format-test mypy

lint:
	black --check --line-length 100 src/
	isort --check-only --profile black src/

format:
	black --line-length 100 src/
	isort --profile black src/

mypy:
	mypy --strict src/

run:
	python src/main.py

clean:
	rm -rf __pycache__ .pytest_cache .mypy_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

pre-commit:
	pre-commit run --all-files