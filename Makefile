fmt:
	poetry run isort ./mkpp/
	poetry run black ./mkpp/

lint:
	poetry run flake8 ./mkpp/
