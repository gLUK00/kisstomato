#from importlib import import_module
import os, sys, importlib

from core import config

# execution d'une methode d'un modele
def exeMethodModel( model, module, method, data ):

    # determine le nom du module
    modulename = config.getPathBase() + os.sep + 'plugins' + os.sep + 'models' + os.sep + str( model ) + os.sep + str( module )

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
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print( 'error on exeMethodModel' )
        print(str( e ))
        print((exc_type, fname, exc_tb.tb_lineno))
        return 'error on exeMethodModel' + str( e ) + '\n' + str(exc_type) + ' : ' + str(fname) + ' : ' + str(exc_tb.tb_lineno)

    return data