install:
	#install the source code

format:
	#makesure the correct format of code

lint:
	#check program syntatically correct using flame or pylint

test:
	#test program

deploy:
	#deploy code

all: install format lint test deploy
