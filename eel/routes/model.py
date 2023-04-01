import eel

# importation du CORE
from core import model

# recupere les informations des projets
@eel.expose
def get_all_models():

    return model.getAll()