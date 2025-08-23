from flask import Blueprint, jsonify, request
from core import app as core_app

# Blueprint for app-related routes
app_bp = Blueprint('app_routes', __name__, url_prefix='/api/app')

# Placeholder for directory selection logic
# In a web app, this would typically be handled by frontend JS and a file upload to an endpoint.
@app_bp.route('/set_dir', methods=['POST'])
def flask_app_set_dir():
    data = request.json
    dir_path = data.get('dir_path') if data else None
    if not dir_path:
        return jsonify({'status': 'error', 'message': 'Missing dir_path in request'}), 400
    
    result_path = core_app.setDir(dir_path)
    if result_path:
        return jsonify({'status': 'success', 'message': 'app_set_dir processed', 'dir_path': result_path})
    else:
        # core_app.setDir might return None if validation fails (if implemented)
        return jsonify({'status': 'error', 'message': 'Failed to process directory path', 'dir_path': dir_path}), 500

# Placeholder for file selection logic
@app_bp.route('/set_file', methods=['POST'])
def flask_app_set_file():
    data = request.json
    file_path = data.get('file_path') if data else None
    ext = data.get('ext') if data else None

    if not file_path:
        return jsonify({'status': 'error', 'message': 'Missing file_path in request'}), 400
    # ext can be optional depending on use case, core_app.setFile handles it

    result_path = core_app.setFile(file_path, ext)
    if result_path:
        return jsonify({'status': 'success', 'message': 'app_set_file processed', 'file_path': result_path, 'ext': ext})
    else:
        # core_app.setFile might return None if validation fails (if implemented)
        return jsonify({'status': 'error', 'message': 'Failed to process file path', 'file_path': file_path}), 500

# Placeholder for save file logic
# In a web app, frontend JS would send file data to this endpoint.
@app_bp.route('/save_as', methods=['POST']) # Renamed route for clarity, maps to core_app.saveAs
def flask_app_save_as(): # Renamed function for clarity
    data = request.json
    dialog_title_text = data.get('dialog_title_text') if data else 'Save As'
    ext = data.get('ext') if data else None
    initialfile_name = data.get('initialfile_name') if data else None

    if not initialfile_name:
        return jsonify({'status': 'error', 'message': 'Missing initialfile_name in request'}), 400

    constructed_path = core_app.saveAs(dialog_title_text, ext, initialfile_name)
    # This function in core_app now just constructs a path.
    # The actual saving of a file would require more logic here or in the frontend.
    return jsonify({'status': 'success', 'message': 'app_save_as processed (path constructed)', 'constructed_path': constructed_path})

# Placeholder for new window logic
@app_bp.route('/new_window', methods=['POST'])
def flask_app_new_window():
    # data = request.json # Not strictly needed anymore as we don't use file_path
    print(f"Received request for app_new_window. This functionality is deprecated on server-side.")
    return jsonify({'status': 'error', 'message': 'Server-side newWindow is deprecated. This should be handled by client-side JavaScript.'}), 410 # 410 Gone