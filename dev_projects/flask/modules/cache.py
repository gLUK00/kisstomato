# kisstomato-module-import-start-user-code-kisstomato
import os, requests, json, time, gl, glob
from datetime import datetime
# kisstomato-module-import-stop-user-code-kisstomato

"""
module de gestion du cache
"""

# kisstomato-module-properties-start-user-code-kisstomato
# kisstomato-module-properties-stop-user-code-kisstomato

# Initialisation du cache
# Argument :
# - path : string : (obligatoire) Chemin du cache
def initCache(path):
    # kisstomato-methode-initCache-start-user-code-kisstomato
    if not os.path.exists( path ):
        os.mkdir( path )
    # kisstomato-methode-initCache-stop-user-code-kisstomato

# Déterminé si une clé de cache existe
# Argument :
# - key : string : (obligatoire) Identifiant du cache
def cacheExists(key):
    oResult = None

    # kisstomato-methode-cacheExists-start-user-code-kisstomato
    oResult = os.path.isfile( gl.config[ "paths" ][ "cache" ] + os.sep + key )
    # kisstomato-methode-cacheExists-stop-user-code-kisstomato

    return oResult

# Retourne les données d'un cache
# Argument :
# - key : string : (obligatoire) Identifiant du cache
def getDataCache(key):
    oResult = None

    # kisstomato-methode-getDataCache-start-user-code-kisstomato
    sDirCache = gl.config[ "paths" ][ "cache" ] + os.sep + key.split( os.sep )[ 0 ]
    if not os.path.exists( sDirCache ):
        print( sDirCache )
        os.mkdir( sDirCache )
    sFileName = sDirCache + os.sep + key.split( os.sep )[ 1 ]
    if not os.path.isfile( sFileName ):
        return None

    oData = {}
    f = open( sFileName )
    oData = json.load(f)
    f.close()

    oResult = oData
    # kisstomato-methode-getDataCache-stop-user-code-kisstomato

    return oResult

# Enregistrement d'un cache
# Arguments :
# - key : string : (obligatoire) Identifiant du cache
# - data : object : (obligatoire) Données du cache
def setDataCache(key, data):
    # kisstomato-methode-setDataCache-start-user-code-kisstomato
    sDirCache = gl.config[ "paths" ][ "cache" ] + os.sep + key.split( os.sep )[ 0 ]
    if not os.path.exists( sDirCache ):
        #print( sDirCache )
        os.mkdir( sDirCache )
    sFileName = sDirCache + os.sep + key.split( os.sep )[ 1 ]
    oFile = open( sFileName, "w" )
    oFile.write( data )
    oFile.close()
    # kisstomato-methode-setDataCache-stop-user-code-kisstomato

# Récupere l'ensemble des fichiers d'un répertoire
# Argument :
# - keyDir : string : (obligatoire) Clé du répertoire du cache
def getAllFiles(keyDir):
    oResult = None

    # kisstomato-methode-getAllFiles-start-user-code-kisstomato

    oResult = glob.glob( gl.config[ "paths" ][ "cache" ] + os.sep + keyDir + os.sep + "*.json" )
    sorted( oResult )

    # kisstomato-methode-getAllFiles-stop-user-code-kisstomato

    return oResult

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato