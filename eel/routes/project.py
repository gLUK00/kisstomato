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

    # si il n'y a pas de proprietes
    if "properties" not in data:
        data[ "properties" ] = {}

    # supprime les cles non necessaires
    filename = data[ 'file' ]
    data.pop( 'file', None )

    # enregistrement du fichier
    oFile = open( filename, "w", encoding="utf-8" )
    oFile.write( json.dumps( data, default=config.dumperJson, indent=4 ) )
    oFile.close()

    # referencement du projet
    config.addProject( filename, relatif_path = ( data[ 'relatif-path' ] != None and data[ 'relatif-path' ] ) )

    return True

# ajout du fichier d'un projet
@eel.expose
def set_file_project( filename, relatif_path ):

    # referencement du projet
    config.addProject( filename, relatif_path )

    return True

# recupere tous les projets
@eel.expose
def get_all_projects():
    oProjects = []

    for pathProject in config.configuration[ 'projects' ]:
        try:
            sPathProject = pathProject.replace( "{path_base}", config.getPathBase() )
            with open( sPathProject, 'r', encoding="utf-8" ) as j:
                oProject = json.loads(j.read())
                oProject[ 'file' ] = sPathProject
                oProjects.append( oProject )
        except Exception as e:
            oProjects.append( { 'file': pathProject, 'error':str( e ) } )

    return oProjects

# supprime un projet
@eel.expose
def del_project( filename, deletefile ):

    oProjects = []
    for pathProject in config.configuration[ 'projects' ]:
        sPathProject = pathProject.replace( "{path_base}", config.getPathBase() )
        if sPathProject == filename:
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
    with open( filename, 'r', encoding="utf-8" ) as j:
        oProject = json.loads(j.read())

        # recuperation du json du modele selectionne
        oProject, bUpdate = plugin.exeMethodModel( oProject[ 'model' ], 'model', 'openProject', oProject )

        # si le projet doit etre sauvegarde
        if bUpdate:
            with open( filename, "w", encoding="utf-8" ) as up:
                up.write( json.dumps( oProject, default=config.dumperJson, indent=4 ) )

    oData = oProject[ 'data' ]
    oProject.pop( 'data' )

    # si il y a des proprietes
    oProperties = {}
    if "properties" in oProject:
        oProperties = oProject[ "properties" ]

    # recupere le modele
    oModel = model.getOne( oProject[ 'model' ] )

    # determine si le modele a des fichiers javascript
    oJs = []

    # recupere les fichiers du modeles
    for sJsFile in glob.glob( config.getPathBase() + os.sep + 'plugins' + os.sep + 'models' + os.sep + oProject[ 'model' ] + os.sep + 'js' + os.sep + '*.js' ):
        oJs.append( { 'type': 'model', 'file': sJsFile.split( os.sep )[ -1 ] } )

    # recupere les fields des plugins des champs
    for sJsFile in glob.glob( config.getPathBase() + os.sep + 'plugins' + os.sep + 'fields' + os.sep + '*' + os.sep + 'field.js' ):

        # recupere le fichier "field.js"
        oJs.append( { 'type': 'field', 'file':  os.sep.join( sJsFile.split( os.sep )[ -2: ] ) } )

        # si il y a des sous fichiers JS
        for sSubJsFile in glob.glob( os.sep.join( sJsFile.split( os.sep )[ :-1 ] ) + os.sep + 'js' + os.sep + '*.js' ):
            oJs.append( { 'type': 'field', 'file': os.sep.join( sSubJsFile.split( os.sep )[ -3: ] ) } )

    return { 'file': filename, 'info': oProject, 'model': oModel, 'data': oData, 'properties': oProperties, 'js': oJs }

# mise a jour des donnees d'un projet
@eel.expose
def update_project( filename, properties, data ):

    oProject = {}
    with open( filename, 'r', encoding="utf-8" ) as j:
        oProject = json.loads(j.read())

    #print( properties )
    #print( data )
    oProject[ 'name' ] = properties[ 'name' ]
    oProject[ 'desc' ] = properties[ 'desc' ]
    oProject[ 'properties' ] = properties[ 'properties' ]
    oProject[ 'data' ] = data

    # enregistrement du fichier
    oFile = open( filename, "w", encoding="utf-8" )
    oFile.write( json.dumps( oProject, default=config.dumperJson, indent=4 ) )
    oFile.close()

    return open_project( filename )