# kisstomato-module-a-start-user-code-kisstomato
# kisstomato-module-a-stop-user-code-kisstomato

import json, os, sys, shutil

from core import generator

# referencement du repertoire parent
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)

from classes import *

# kisstomato-module-b-start-user-code-kisstomato
# kisstomato-module-b-stop-user-code-kisstomato

# Génération du code

# Génération de l'application Flask
# Argument :
# - data : object : (obligatoire) Données du formulaire JS
def generateFlaskCode(data):
    oResult = None

    # kisstomato-fonction-generateFlaskCode-init-start-user-code-kisstomato
    # kisstomato-fonction-generateFlaskCode-init-stop-user-code-kisstomato

    try:
        # kisstomato-fonction-generateFlaskCode-try-start-user-code-kisstomato
        pass()
        # kisstomato-fonction-generateFlaskCode-try-stop-user-code-kisstomato

    except Exception as e:
        # kisstomato-exception-generateFlaskCode-a-start-user-code-kisstomato
        # kisstomato-exception-generateFlaskCode-a-stop-user-code-kisstomato
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        # kisstomato-exception-generateFlaskCode-b-start-user-code-kisstomato
        # kisstomato-exception-generateFlaskCode-b-stop-user-code-kisstomato

    # kisstomato-return-generateFlaskCode-return-start-user-code-kisstomato
    # kisstomato-return-generateFlaskCode-return-stop-user-code-kisstomato
    return oResult

# kisstomato-module-c-start-user-code-kisstomato
# kisstomato-module-c-stop-user-code-kisstomato