# kisstomato-module-import-start-user-code-kisstomato
import os, json, gl
# kisstomato-module-import-stop-user-code-kisstomato

"""
gestion de la configuration
"""

# kisstomato-module-properties-start-user-code-kisstomato
# kisstomato-module-properties-stop-user-code-kisstomato

# chargement de la configuration
# Argument :
# - conf : string : (facultatif) nom du fichier de configuration
def load(conf=None):
    # kisstomato-methode-load-start-user-code-kisstomato

    if not conf:
        conf='configuration.json'

    # chargement du fichier de configuration
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + '/../' + conf)
    gl.config = json.load(f)

    # kisstomato-methode-load-stop-user-code-kisstomato

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato