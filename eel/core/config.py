import json, os

configuration = None

# chargement de la configuration
def load():
    global configuration

    path_base = os.path.dirname( os.path.dirname( os.path.realpath( __file__ ) ) )

    # chargement du fichier de configuration
    with open( path_base + os.sep + 'configuration.json', 'r' ) as j:
        configuration = json.loads(j.read())
    configuration[ "path_base" ] = path_base

# ajout d'un projet dans la configuration
def addProject( path ):
    global configuration

    if path in configuration[ "projects" ]:
        return

    configuration[ "projects" ].append( path )

    saveConf()

# enregistrement de la configuration
def saveConf():
    global configuration

    # enregistrement du fichier
    path_base = configuration[ "path_base" ]
    oFile = open( configuration[ "path_base" ] + os.sep + 'configuration.json', "w", encoding="utf-8" )
    oFile.write( json.dumps( configuration, default=dumperJson, indent=4 ) )
    oFile.close()
    configuration[ "path_base" ] = path_base

def dumperJson(obj):
    try:
        return obj.toJSON()
    except:
        if isinstance( obj, bytes ):
            return base64.b64encode( obj ).decode( 'utf-8' )
        return obj.__dict__