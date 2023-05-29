fmt:
	poetry run black .
	poetry run isort .

lint:
	-poetry run flake8p ./example_fastapi_sqlmodel_alembic ./tests
	poetry run mypy ./example_fastapi_sqlmodel_alembic ./tests

up:
	poetry run uvicorn example_fastapi_sqlmodel_alembic.api.app:app --reload
