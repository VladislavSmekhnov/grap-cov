.PHONY: install run generate_requirements

install:
	pip3 --version
	pip3 install -r requirements.txt

run: install
	python3 main.py

generate_requirements:
	pip3 freeze > requirements.txt
