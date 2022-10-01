install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt 

format:
	#makesure the correct format of code
	black *.py src/*.py

lint:
	#check program syntatically correct using flame or pylint

test:
	#test program

deploy:
	#deploy code

all: install format lint test deploy
