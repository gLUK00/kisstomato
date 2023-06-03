import glob, os, json

from core import config

# recupere les informations des projets
def getAll():
    oModels = []

    oPathConfModels = glob.glob( config.configuration[ "path_base" ] + os.sep + 'plugins' + os.sep + 'models' + os.sep + '*' + os.sep + 'configuration.json' )
    for conf_model in oPathConfModels:
        #print( 'debug : getAll : ' + conf_model )
        name_model = conf_model.split( os.sep )[ -2 ]
        oElement = {"name":name_model}
        with open(conf_model, 'r') as j:
            oElement.update( json.loads(j.read()) )
        oModels.append( oElement )

    return oModels

# recupere les informations d'un modele
def getOne( modele ):

    sPathConfModel = glob.glob( config.configuration[ "path_base" ] + os.sep + 'plugins' + os.sep + 'models' + os.sep + modele + os.sep + 'configuration.json' )[ 0 ]
    f = open( sPathConfModel )
    return json.load(f)
