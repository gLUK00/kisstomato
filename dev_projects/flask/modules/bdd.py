# kisstomato-module-import-start-user-code-kisstomato
import gl, json
from pymongo import MongoClient
# kisstomato-module-import-stop-user-code-kisstomato

"""
module d’accès à la base de donnée
"""

# kisstomato-module-properties-start-user-code-kisstomato
_oBdd = None
# kisstomato-module-properties-stop-user-code-kisstomato

"""
récupération de la base de donnée
"""
def getBdd():
    oResult = None

    # kisstomato-methode-getBdd-start-user-code-kisstomato
    global _oBdd
    if _oBdd == None:
        sUri = 'mongodb://' + gl.config[ 'mongo' ][ 'user' ] + ':' + gl.config[ 'mongo' ][ 'pass' ] + '@' + gl.config[ 'mongo' ][ 'host' ] + ':' + str( gl.config[ 'mongo' ][ 'port' ] ) + '/'
        _oBdd = MongoClient( sUri )[ gl.config[ 'mongo' ][ 'bdd' ] ]
    oResult = _oBdd
    # kisstomato-methode-getBdd-stop-user-code-kisstomato

    return oResult

"""
Determine si une collection existe
"""
# Argument :
# - collection : string : (obligatoire) Nom de la collection
def collectionExist(collection):
    oResult = None

    # kisstomato-methode-collectionExist-start-user-code-kisstomato

    oBdd = getBdd()
    oResult = collection in oBdd.list_collection_names()
    #print( collection )
    #print( oBdd.list_collection_names() )

    # kisstomato-methode-collectionExist-stop-user-code-kisstomato

    return oResult

"""
Supprime une collection
"""
# Arguments :
# - collection : string : (obligatoire) Nom de la collection
# - createIndex : string : (facultatif) Nom de l'index à créer
def dropCollection(collection, createIndex=None):
    # kisstomato-methode-dropCollection-start-user-code-kisstomato

    oBdd = getBdd()
    if collectionExist( collection ):
        oBdd[ collection ].drop()
    oBdd.create_collection( collection )
    if createIndex != None:
        oBdd[ collection ].create_index( createIndex )

    # kisstomato-methode-dropCollection-stop-user-code-kisstomato

"""
Importation de l'historique des transactions
"""
# Arguments :
# - collection : string : (obligatoire) Collection cible
# - pair : string : (obligatoire) Paire à importer
# - listFiles : string : (obligatoire) Clé du cache correspondante aux fichiers
def importHistory(collection, pair, listFiles):
    # kisstomato-methode-importHistory-start-user-code-kisstomato

    # pour tous les fichiers
    oBdd = getBdd()
    for sFileName in listFiles:

        # ouverture du fichier
        print( 'Importation du fichier : ' + sFileName )
        f = open( sFileName )
        oData = json.load(f)
        f.close()

        # pour tous les enregistrements
        for oLine in oData[ 'result' ][ pair.upper() ]:
            oBdd[ collection ].insert_one( { 'time': oLine[ 2 ], 'qte': oLine[ 1 ], 'val': oLine[ 0 ], 'action': oLine[ 3 ], 'type': oLine[ 4 ] } )
    
    # kisstomato-methode-importHistory-stop-user-code-kisstomato

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato