import eel, os

# importation du CORE
from core import plugin

# execution d'une methode d'un modele
@eel.expose
def plugin_exec_method_model( model, module, method, data ):
    return plugin.exeMethodModel( model, module, method, data )

# telechargement du fichier javascript d'un field
@eel.expose
def plugin_get_javascript_field( file ):

    path_base = os.path.dirname( os.path.dirname( os.path.realpath( __file__ ) ) )
    sFile = path_base + os.sep + 'plugins' + os.sep + 'fields' + os.sep + file
    if not os.path.isfile( sFile ):
        print( 'Error : get_javascript_field : fichier introuvable : ' + sFile )
        return ''

    sContent = ''
    with open( sFile, "r", encoding="utf-8" ) as oFile:
        sContent = oFile.read()

    return str( sContent )