import eel, os

# importation du CORE
from core import model

# recupere les informations des projets
@eel.expose
def get_all_models():

    return model.getAll()

# telechargement d'un fichier javascript d'un modele
@eel.expose
def get_javascript( model, file ):

    path_base = os.path.dirname( os.path.dirname( os.path.realpath( __file__ ) ) )
    sFile = path_base + os.sep + 'plugins' + os.sep + 'models' + os.sep + model + os.sep + 'js' + os.sep + file
    if not os.path.isfile( sFile ):
        print( 'Error : get_javascript : fichier introuvable : ' + sFile )
        return ''

    sContent = ''
    with open( sFile, "r", encoding="utf-8" ) as oFile:
        sContent = oFile.read()

    return str( sContent )