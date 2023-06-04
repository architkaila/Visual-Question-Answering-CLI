setup:
	pip install --upgrade pip
	pip install -r requirements.txt
	python setup.py develop

format:
	black *.py
	black tests/*.py
	black model/*.py

lint:
	pylint --disable=R,C model/run_model.py

test:
	python -m pytest -vv --cov=model tests/test_run_model.py

all: setup format lint test