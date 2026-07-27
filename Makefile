.PHONY: install run format lint test

install:
	cd backend && poetry install --no-root

run:
	cd backend && poetry run uvicorn app.main:app --reload

test:
	cd backend && poetry run pytest

format:
	cd backend && poetry run black .

lint:
	cd backend && poetry run ruff check .