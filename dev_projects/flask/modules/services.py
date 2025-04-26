# kisstomato-module-import-start-user-code-kisstomato
import requests, json, gl, os, time
from datetime import datetime
from modules import cache
# kisstomato-module-import-stop-user-code-kisstomato

"""
Services en ligne
"""

# kisstomato-module-properties-start-user-code-kisstomato
# kisstomato-module-properties-stop-user-code-kisstomato

"""
Recupère la liste des paires
"""
def getPairs():
    oResult = None

    # kisstomato-methode-getPairs-start-user-code-kisstomato
    oResult = cache.getDataCache( 'pairs/data.json' )
    if oResult == None:

        print( 'Telechargement des PAIRS' )
        resp = requests.get( gl.config[ "services" ][ "get-pairs" ] )
        oResult = resp.json()
        cache.setDataCache( 'pairs/data.json', json.dumps( oResult ) )
    # kisstomato-methode-getPairs-stop-user-code-kisstomato

    return oResult

"""
Retourne la liste des fichiers d'historiques des trades
"""
# Argument :
# - pair : string : (obligatoire) Paire à récupérer
def getTradesFiles(pair):
    oResult = None

    # kisstomato-methode-getTradesFiles-start-user-code-kisstomato

    oResult = []
    iSince = 0

    while True:

        # si le fichier de cache existe
        sKey = 'trades_' + pair + '/' + str( iSince ) + '.json'
        if not cache.cacheExists( sKey ):

            print( 'Telechargement ' + pair + ' depuis l\'index ' + str( iSince ) + ' du ' + datetime.fromtimestamp( int( str( iSince )[ 0:10 ] ) ).strftime('%Y/%m/%d %H:%M:%S') )
            time.sleep( 1 )
            resp = requests.get( gl.config[ "services" ][ "get-trades" ].replace( "{pair}", pair ).replace( "{since}", str( iSince ) ) )
            oPairs = resp.json()
            cache.setDataCache( sKey, json.dumps( oPairs ) )  

        # lecture du fichier et recherche de l'index suivant
        oData = cache.getDataCache( sKey )

        # recupere le nom du fichier
        oResult.append( gl.config[ "paths" ][ "cache" ] + os.sep + sKey )

        # si c'est le dernier fichier
        if oData[ 'result' ][ 'last' ] == str( iSince ):
            break

        # recupere le prochain index
        iSince = int( oData[ 'result' ][ 'last' ] )

    # kisstomato-methode-getTradesFiles-stop-user-code-kisstomato

    return oResult

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato