install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt 

format:
	#makesure the correct format of code
	black *.py src/*.py

lint:
	#check program syntatically correct using flame or pylint, disabling R,C avoid warnig and avoid ci fail
	pylint --disable=R,C *.py src/*.py

test:
	#test program cov flag says how much test coverage inside
	python -m pytest -vv --cov=src test_logic.py

deploy:
	#deploy code

all: install format lint test deploy
