SHELL := /bin/bash

init:
	python3 ./createEnv.py
	source vEnv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt
update:
	source vEnv/bin/activate && \
	pip install -r requirements.txt
clean:
	rm -R -f vEnv
	rm -R -f __pycache__
	rm -R -f *.egg-info
