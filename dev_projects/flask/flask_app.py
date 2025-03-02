import os, gl, sys, json

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
configFile = os.path.dirname(os.path.realpath(__file__)) + os.sep + sys.argv[ 1 ]
gl.config = json.load( open( configFile ) )
print( configFile )
print( gl.config )

# importation des routes
from fl_routes import routes

app.register_blueprint(routes)

@app.route('/')
def home():
   return render_template('index.html')

gl.socketio.run(app, host=gl.config[ 'host' ], port=gl.config[ 'port' ], debug=gl.config[ 'debug' ], allow_unsafe_werkzeug=True)