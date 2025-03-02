import os, gl, sys

from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask( __name__,
    static_url_path='', 
    static_folder='web' + os.sep + 'static',
    template_folder='web' + os.sep + 'templates' )

app.config['TIMEOUT'] = 18000  # 30 minutes
CORS(app)

# mise en place du socket
gl.socketio = SocketIO( app, cors_allowed_origins="*" )

# recuperation du fichier de configuration
configFile = sys.argv[ 1 ]
print( configFile )

# importation des routes
from fl_routes import routes

app.register_blueprint(routes)

@app.route('/')
def home():
   return render_template('index.html')

gl.socketio.run(app, host="0.0.0.0", port=8080, debug=True, allow_unsafe_werkzeug=True)