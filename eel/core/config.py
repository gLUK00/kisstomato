import json, os, base64
configuration = None

# recupere le chemin de base de l'application
def getPathBase():
    return os.path.dirname( os.path.dirname( os.path.realpath( __file__ ) ) )

# chargement de la configuration
def load():
    global configuration

    path_base = getPathBase()

    # chargement du fichier de configuration
    with open( path_base + os.sep + 'configuration.json', 'r' ) as j:
        configuration = json.loads(j.read())

# ajout d'un projet dans la configuration
def addProject( path, relatif_path = False ):
    global configuration

    path_base = getPathBase()

    if relatif_path:
        oPathBase = path_base.split( os.sep )
        iPosSearch = len( oPathBase )
        iDiffSep = 0
        while True:
            
            sSearch = os.sep.join( oPathBase[ : iPosSearch ] )
            sReplace = "{path_base}" + ( ( os.sep + '..' ) * iDiffSep )

            iPosSearch -= 1
            iDiffSep += 1

            path = path.replace( sSearch, sReplace )

            if path.find( "{path_base}" ) != -1 or iPosSearch < 0:
                break

    if path in configuration[ "projects" ]:
        return

    configuration[ "projects" ].append( path )

    saveConf()

# enregistrement de la configuration
def saveConf():
    global configuration

    # enregistrement du fichier
    oFile = open( getPathBase() + os.sep + 'configuration.json', "w", encoding="utf-8" )
    oFile.write( json.dumps( configuration, default=dumperJson, indent=4 ) )
    oFile.close()

def dumperJson(obj):
    try:
        return obj.toJSON()
    except:
        if isinstance( obj, bytes ):
            return base64.b64encode( obj ).decode( 'utf-8' )
        return obj.__dict__