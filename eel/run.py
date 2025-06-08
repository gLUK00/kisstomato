import os, sys, json, time
from datetime import datetime
from flask import Flask, send_from_directory, render_template

# inclusion des elements communs
from core import config
# We will re-introduce routes later as Flask blueprints or by direct import
from routes.app import app_bp
from routes.project import project_bp
from routes.model import model_bp
from routes.plugin import plugin_bp

# chargement du fichier de configuration
config.load()

app = Flask(__name__, template_folder='web', static_folder='web')

# Commenting out watchdog for now, can be re-added if needed for Flask dev server
# class MyHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         if event.src_path.endswith(".py") or event.src_path.endswith(".json"):
#             print("Fichier modifie, redemarrage de l'application...")
#             # Flask's dev server handles auto-reloading for .py changes
#             # For other files, a browser refresh might be needed or more advanced setup
#             # os.execv(sys.executable, [os.path.basename(sys.executable)] + sys.argv)

@app.route('/')
def index():
    # Assuming your main html file is index.html in the 'web' folder
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Register Blueprints
app.register_blueprint(app_bp)
app.register_blueprint(project_bp)
app.register_blueprint(model_bp)
app.register_blueprint(plugin_bp)

# We will define API endpoints based on the old eel.expose functions later

if __name__ == '__main__':
    # observer = Observer()
    # observer.schedule(MyHandler(), '.', recursive=True)
    # observer.start()
    app.run(debug=True, port=config.configuration["port"]) # Using the same port as before for consistency