# importation du CORE
from core import config, plugin

import base64, json, os

# creation du fichier d'un projet
def createFileProject( data ):
    try:

        # recuperation du json du modele selectionne
        data = plugin.exeMethodModel( data[ 'model' ], 'model', 'getJsonCreateNewProject', data )

    except Exception as e:
        return str( e )

    # supprime les cles non necessaires
    filename = data[ 'file' ]
    data.pop( 'file', None )

    # enregistrement du fichier
    def dumper(obj):
        try:
            return obj.toJSON()
        except:
            if isinstance( obj, bytes ):
                return base64.b64encode( obj ).decode( 'utf-8' )
            return obj.__dict__

    oFile = open( filename, "w", encoding="utf-8" )
    oFile.write( json.dumps( data, default=dumper, indent=4 ) )
    oFile.close()

    # referencement du projet
    config.addProject( filename )

    return True

# recupere tous les projets
def getAll():
    oProjects = []

    for pathProject in config.configuration[ 'projects' ]:
        try:
            f = open( pathProject )
            oProject = json.load(f)
            oProject[ 'file' ] = pathProject
            oProjects.append( oProject )
        except Exception as e:
            oProjects.append( { 'file': pathProject, 'error':str( e ) } )

    return oProjects

# supprime un projet
def delProject( filename, deletefile ):

    oProjects = []
    for pathProject in config.configuration[ 'projects' ]:
        if pathProject == filename:
            if deletefile and  os.path.isfile( filename ):
                os.remove( filename )
            continue
        oProjects.append( pathProject )

    config.configuration[ 'projects' ] = oProjects
    config.saveConf()

    return True