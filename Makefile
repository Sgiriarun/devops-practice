install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt 

format:
	#makesure the correct format of code
	black *.py src/*.py

lint:
	#check program syntatically correct using flame or pylint, disabling R,C (recomended & configuration warnig)avoid warnig and avoid ci fail
	pylint --disable=R,C *.py src/*.py

test:
	#test program cov flag says how much test coverage inside
	python -m pytest -vv --cov=src --cov=main test_*.py

build:
	#docker build
	docker build -t devops-practice .

run:
	#run docker 
	docker run -p 127.0.0.1:8080:8080 4ad68334a6a6
	
deploy:
	#deploy code


all: install format lint test deploy
