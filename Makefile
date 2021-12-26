fmt:
	pdm run isort mkpp/
	pdm run black mkpp/

lint:
	pdm run flake8 mkpp/
