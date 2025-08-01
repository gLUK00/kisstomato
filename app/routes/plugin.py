import os
from flask import Blueprint, jsonify, request, send_from_directory, current_app

# importation du CORE
from core import plugin as core_plugin # Alias to avoid conflict

plugin_bp = Blueprint('plugin_routes', __name__, url_prefix='/api/plugin')

# execution d'une methode d'un modele
@plugin_bp.route('/exec_method_model', methods=['POST'])
def flask_plugin_exec_method_model():
    req_data = request.json
    model_name = req_data.get('model')
    module_name = req_data.get('module')
    method_name = req_data.get('method')
    data_payload = req_data.get('data')
    try:
        result = core_plugin.exeMethodModel( model_name, module_name, method_name, data_payload )
        # exeMethodModel might return a tuple (data, boolean) or just data, or raise an exception.
        # We need to ensure it's JSON serializable.
        if isinstance(result, tuple):
             # Assuming the tuple is (data, status_flag) or similar
             return jsonify({'status': 'success', 'result': result[0], 'flag': result[1]})
        else:
             return jsonify({'status': 'success', 'result': result})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# telechargement du fichier javascript d'un field
@plugin_bp.route('/js/field/<path:file_path>', methods=['GET'])
def flask_plugin_get_javascript_field(file_path):
    # file_path can be 'field_type/field.js' or 'field_type/js/sub_file.js'
    # The base directory for serving these files is 'plugins/fields'
    fields_dir = os.path.join(current_app.root_path, 'plugins', 'fields')
    
    # Check if file exists to provide a better error
    full_file_path_to_check = os.path.join(fields_dir, file_path)
    if not os.path.isfile(full_file_path_to_check):
        print(f'Error : get_javascript_field : fichier introuvable : {full_file_path_to_check}')
        return jsonify({'status': 'error', 'message': 'File not found'}), 404

    # print(f"Serving JS field file: {file_path} from directory: {fields_dir}")
    return send_from_directory(fields_dir, file_path, mimetype='application/javascript')