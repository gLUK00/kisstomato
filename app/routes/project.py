import base64, json, os, glob
from flask import Blueprint, jsonify, request

# importation du CORE
# from core import config, model, plugin # Already imported below, ensure no duplication if core also changes

project_bp = Blueprint('project_routes', __name__, url_prefix='/api/project')

# importation du CORE
from core import config, model, plugin

# creation du fichier d'un projet
@project_bp.route('/create_file', methods=['POST'])
def flask_get_create_file_project():
    data = request.json
    try:

        # recuperation du json du modele selectionne
        data = plugin.exeMethodModel( data[ 'model' ], 'model', 'getJsonCreateNewProject', data )

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

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
    config.addProject( filename, relatif_path = ( data.get('relatif-path') != None and data.get('relatif-path') ) )

    return jsonify({'status': 'success', 'filename': filename})

# ajout du fichier d'un projet
@project_bp.route('/set_file', methods=['POST'])
def flask_set_file_project():
    req_data = request.json
    filename = req_data.get('filename')
    relatif_path = req_data.get('relatif_path')

    # referencement du projet
    config.addProject( filename, relatif_path )

    return jsonify({'status': 'success'})

# recupere tous les projets
@project_bp.route('/get_all', methods=['GET'])
def flask_get_all_projects():
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

    return jsonify(oProjects)

# supprime un projet
@project_bp.route('/delete', methods=['POST'])
def flask_del_project():
    req_data = request.json
    filename = req_data.get('filename')
    deletefile = req_data.get('deletefile')

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

    return jsonify({'status': 'success'})

# ouverture d'un projet
@project_bp.route('/open', methods=['POST'])
def flask_open_project():
    req_data = request.json
    filename = req_data.get('filename')

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

    return jsonify({ 'file': filename, 'info': oProject, 'model': oModel, 'data': oData, 'properties': oProperties, 'js': oJs })

# mise a jour des donnees d'un projet
@project_bp.route('/update', methods=['POST'])
def flask_update_project():
    req_data = request.json
    filename = req_data.get('filename')
    properties = req_data.get('properties')
    data = req_data.get('data') # This is 'data' from the request, not the oProject['data']

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

    # Instead of calling the old open_project, we might need to call the new flask_open_project
    # or simply return the updated project data directly. For now, let's assume the client
    # might re-fetch if needed, or we return the same structure as open_project.
    # For simplicity, let's just return a success message, the client can re-fetch project details.
    # Alternatively, replicate the data fetching part of flask_open_project here if needed.
    # For now, returning a simple success. The frontend will need to adjust.
    # If a full project reload is needed, the frontend should call /api/project/open again.
    return jsonify({'status': 'success', 'message': 'Project updated. Call /api/project/open to get updated details if needed.', 'filename': filename})