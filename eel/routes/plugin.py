import eel

# importation du CORE
from core import plugin

# execution d'une methode d'un modele
@eel.expose
def plugin_exec_method_model( model, module, method, data ):
    return plugin.exeMethodModel( model, module, method, data )
