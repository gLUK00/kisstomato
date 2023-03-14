#from importlib import import_module
import os, sys, importlib

from core import config

# execution d'une methode d'un modele
def exeMethodModel( model, module, method, data ):

    # determine le nom du module
    modulename = config.configuration[ "path_base" ] + os.sep + 'plugins' + os.sep + 'models' + os.sep + model + os.sep + module

    try:

        # chargement du module
        file_path = modulename + '.py'
        module_name = module

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        oModule = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(oModule)

        if not method in dir( oModule ):
            return data

        # execution de la methode
        fMethod = getattr( oModule, method )
        return fMethod( data )

    except Exception as e:
        print( 'error on exeMethodModel' )
        print( e )
        return data

    return data