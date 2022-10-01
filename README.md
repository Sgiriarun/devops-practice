[![python application test with github actions](https://github.com/Sgiriarun/devops-practice/actions/workflows/devops_python.yml/badge.svg)](https://github.com/Sgiriarun/devops-practice/actions/workflows/devops_python.yml)

# devops-practice
## this is devops practice library (using makefile, requirements.txt, source file, Dockerfile )
## representation 
create virtual 
![docerpractice](https://user-images.githubusercontent.com/38005622/193394734-291ff405-491e-4c70-b870-c6044ee95f0d.png)
1. creat virtual environment:
    'python3 -m venv ~/.venv' or 'virtualvenv ~/.venv'
    and souce virtual environment 'source ~/.venv/bin/activate' in ~/.bashrc 
    so whenever we open new terminal, it is processed to open virtual environment.
2. create empty file requirements.txt Dockerfile Makefile and src folder and fill the Makefile with 
    dummy fills(install, test, lint, format, deploy, all)
3. fill the requirements file and add make install correctly 
4. pin the version number for installed package by 'pip freeze | less'
5. create workflow,(helps in ci/cd) by use of github actions (.github/workflows/devops_python.yml)
6. add format in the make file for src/logic.py and main.py
