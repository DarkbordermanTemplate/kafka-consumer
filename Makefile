.PHONY: init

init: clean
	pipenv --python 3.7
	pipenv install --dev --skip-lock

lint: pylint flake8

pylint:
	pipenv run pylint --rcfile=setup.cfg kafka/

flake8:
	pipenv run flake8 kafka/ --max-line-length=120

reformat: black isort

black:
	pipenv run black kafka/

isort:
	pipenv run isort kafka/*.py
	pipenv run isort kafka/**/*.py

test:
	pipenv run pytest --cov-report=term-missing --cov-config=.coveragerc --cov=kafka/topics kafka/tests

ci-bundle: reformat lint test

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf .hypothesis
	rm -rf .pytest_cache
	rm -rf .tox
	rm -f report.xml
	rm -f coverage.xml
