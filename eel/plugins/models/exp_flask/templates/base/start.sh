#!/bin/bash

# kisstomato-start-sh-a-start-user-code-kisstomato
# kisstomato-start-sh-a-stop-user-code-kisstomato

virtualenv venv

# kisstomato-start-sh-b-start-user-code-kisstomato
# kisstomato-start-sh-b-stop-user-code-kisstomato

source venv/bin/activate

# kisstomato-start-sh-c-start-user-code-kisstomato
# kisstomato-start-sh-c-stop-user-code-kisstomato

# lancement de l'application
pip install -r requirements.txt

# kisstomato-start-sh-d-start-user-code-kisstomato
# kisstomato-start-sh-d-stop-user-code-kisstomato

# lancement de l'application
python3 api.py

# kisstomato-start-sh-e-start-user-code-kisstomato
# kisstomato-start-sh-e-stop-user-code-kisstomato

deactivate

# kisstomato-start-sh-f-start-user-code-kisstomato
# kisstomato-start-sh-f-stop-user-code-kisstomato