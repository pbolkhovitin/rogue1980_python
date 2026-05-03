.PHONY: setup test check run clean format lint mypy pre-commit

setup:
	pip install pytest mypy ruff pre-commit
	pre-commit install

test:
	pytest tests/

check: mypy test lint

lint:
	ruff check src/ tests/

format:
	ruff check --fix src/ tests/
	ruff format src/ tests/

mypy:
	mypy --strict src/

run:
	python3 src/main.py

clean:
	rm -rf __pycache__ .pytest_cache .mypy_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

pre-commit:
	pre-commit run --all-files