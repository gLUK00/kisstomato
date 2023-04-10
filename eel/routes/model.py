import eel

# importation du CORE
from core import model

# recupere les informations des projets
@eel.expose
def get_all_models():

    return model.getAll()

# telechargement d'un fichier javascript d'un modele
@eel.expose
def get_javascript( model, file ):
    

    return 'console.log( "toto" );'