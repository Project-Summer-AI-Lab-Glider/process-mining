init:
	pip install -r requirements.txt
	flake8 ./src
	flake8 ./tests

.PHONY : init