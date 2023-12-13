.PHONY: install run generate_requirements

VENV_PATH = venv/bin/activate
ACTIVATE_VENV_CMD = . ./$(ACTIVATE_VENV_PATH)

install:
	$(ACTIVATE_VENV_CMD) && pip3 --version
	pip3 install -r requirements.txt

run:
	$(ACTIVATE_VENV_CMD) && python3 main.py

generate_requirements:
	pip3 freeze > requirements.txt

chmod_venv_activate:
	chmod +x venv/bin/activate
