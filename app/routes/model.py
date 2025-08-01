import os
from flask import Blueprint, jsonify, send_from_directory, current_app

# importation du CORE
from core import model as core_model # Alias to avoid conflict if we name blueprint 'model'

model_bp = Blueprint('model_routes', __name__, url_prefix='/api/model')

# recupere les informations des projets
@model_bp.route('/get_all', methods=['GET'])
def flask_get_all_models():
    return jsonify(core_model.getAll())

# telechargement d'un fichier javascript d'un modele
@model_bp.route('/js/<path:model_name>/<path:file_name>', methods=['GET'])
def flask_get_javascript(model_name, file_name):
    # Construct the path relative to the 'plugins/models/<model_name>/js' directory
    # The base path for send_from_directory should be the 'plugins' directory.
    # Correctly determine the path to the 'plugins' directory from the app's root or a known base.
    # Assuming 'run.py' is in the project root, and 'plugins' is a subdirectory.
    # path_base = current_app.root_path # This is usually the directory of run.py
    # For send_from_directory, the first arg is the directory, the second is the path relative to that directory.
    # We need to serve from 'eel/plugins/models/<model_name>/js/<file_name>'
    # So, directory for send_from_directory is 'eel/plugins/models/<model_name>/js'
    # and path is 'file_name'
    # A more robust way is to define PLUGINS_FOLDER = os.path.join(current_app.root_path, 'plugins')

    # The original code calculated path_base from __file__, which is .../eel/routes
    # So path_base + /plugins/models/... becomes .../eel/routes/../plugins/models = .../eel/plugins/models
    # This seems correct.
    # Let's use a path relative to the application's root directory for send_from_directory.
    # current_app.root_path is the directory where run.py is (i.e., /home/hidalgo/Documents/projects/kisstomato/eel)
    
    # Path to the 'js' directory for the specific model
    model_js_dir_relative_to_plugins = os.path.join('models', model_name, 'js')
    plugins_dir = os.path.join(current_app.root_path, 'plugins')
    
    # The directory from which files will be served.
    directory_to_serve_from = os.path.join(plugins_dir, 'models', model_name, 'js')

    # Check if file exists to provide a better error than Werkzeug's default
    file_path_to_check = os.path.join(directory_to_serve_from, file_name)
    if not os.path.isfile(file_path_to_check):
        print(f'Error : get_javascript : fichier introuvable : {file_path_to_check}')
        return jsonify({'status': 'error', 'message': 'File not found'}), 404

    # print(f"Serving JS file: {file_name} from model: {model_name} from directory: {directory_to_serve_from}")
    return send_from_directory(directory_to_serve_from, file_name, mimetype='application/javascript')