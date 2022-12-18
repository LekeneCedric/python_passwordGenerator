init:
	pip install -r requirements.txt

test:
	nosetests tests

run:
	python3 sample/main.py
