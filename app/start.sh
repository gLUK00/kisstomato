#!/bin/bash

# installation de tk
# sudo apt-get install python3-tk

virtualenv venv
#virtualenv venv --python=python2.7

source venv/bin/activate

#Set "VIRTUAL_ENV=/home/hidalgo/Documents/projects/kisstomato/eel/venv"

# lancement de l'application
pip install tkinter
pip install -r requirements.txt
python3 run.py

deactivate
