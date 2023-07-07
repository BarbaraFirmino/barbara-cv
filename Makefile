precommit:
	poetry run pre-commit run --all-files

pylint:
	@pylint barbara_cv/**/**.py
	@pylint tests/**/**.py

mypy:
	@mypy barbara_cv
	@mypy tests
