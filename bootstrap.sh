#!/bin/sh
export FLASK_APP=./produto/index.py
#export FLASK_APP=./index.py ## for localhost
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0 --port=8080