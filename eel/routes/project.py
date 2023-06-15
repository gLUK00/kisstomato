import eel, base64, json, os, glob

# importation du CORE
from core import config, model, plugin

# creation du fichier d'un projet
@eel.expose
def get_create_file_project( data ):
    try:

        # recuperation du json du modele selectionne
        data = plugin.exeMethodModel( data[ 'model' ], 'model', 'getJsonCreateNewProject', data )

    except Exception as e:
        return str( e )

    # si il n'y a pas de donnees
    if "data" not in data:
        data[ "data" ] = []

    # supprime les cles non necessaires
    filename = data[ 'file' ]
    data.pop( 'file', None )

    # enregistrement du fichier
    oFile = open( filename, "w", encoding="utf-8" )
    oFile.write( json.dumps( data, default=config.dumperJson, indent=4 ) )
    oFile.close()

    # referencement du projet
    config.addProject( filename )

    return True

# ajout du fichier d'un projet
@eel.expose
def set_file_project( filename ):

    # referencement du projet
    config.addProject( filename )

    return True

# recupere tous les projets
@eel.expose
def get_all_projects():
    oProjects = []

    for pathProject in config.configuration[ 'projects' ]:
        try:
            with open( pathProject, 'r' ) as j:
                oProject = json.loads(j.read())
                oProject[ 'file' ] = pathProject
                oProjects.append( oProject )
        except Exception as e:
            oProjects.append( { 'file': pathProject, 'error':str( e ) } )

    return oProjects

# supprime un projet
@eel.expose
def del_project( filename, deletefile ):

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

# ouverture d'un projet
@eel.expose
def open_project( filename ):

    # ouverture du projet
    oProject = {}
    with open( filename, 'r' ) as j:
        oProject = json.loads(j.read())
    oData = oProject[ 'data' ]
    oProject.pop( 'data' )

    # determine si le modele a des fichiers javascript
    oJs = []
    for sJsFile in glob.glob( config.configuration[ "path_base" ] + os.sep + 'plugins' + os.sep + 'models' + os.sep + oProject[ 'model' ] + os.sep + 'js' + os.sep + '*.js' ):
        oJs.append( sJsFile.split( os.sep )[ -1 ] )

    return { 'file': filename, 'info': oProject, 'model': model.getOne( oProject[ 'model' ] ), 'data': oData, 'js': oJs }

# mise a jour des donnees d'un projet
@eel.expose
def update_project( filename, data ):

    oProject = {}
    with open( filename, 'r' ) as j:
        oProject = json.loads(j.read())
    oProject[ 'data' ] = data

    # enregistrement du fichier
    oFile = open( filename, "w", encoding="utf-8" )
    oFile.write( json.dumps( oProject, default=config.dumperJson, indent=4 ) )
    oFile.close()

    return True