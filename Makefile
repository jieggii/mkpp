fmt:
	poetry run isort ./mkpm/
	poetry run black ./mkpm/

lint:
	poetry run flake8 ./mkpm/
