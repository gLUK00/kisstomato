# kisstomato-module-import-start-user-code-kisstomato
import gl, json, pymongo, os
from pymongo import MongoClient
from bson import BSON, json_util, decode_file_iter
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
Export une collection
"""
# Argument :
# - collection : string : (obligatoire) Nom de la collection
def exportCollection(collection):
    # kisstomato-methode-exportCollection-start-user-code-kisstomato

    # determine l'eixstance du repertoire des dumps
    if not os.path.exists(gl.config[ 'paths' ][ 'dump' ]):
        os.makedirs(gl.config[ 'paths' ][ 'dump' ])
    
    oBdd = getBdd()
    print( "Ecriture du fichier " + gl.config[ 'paths' ][ 'dump' ] + "/" + collection + ".bson" )
    with open(gl.config[ 'paths' ][ 'dump' ] + "/" + collection + ".bson", "wb") as f:
        for doc in oBdd[ collection ].find({}):
            f.write(BSON.encode(doc))
    
    # kisstomato-methode-exportCollection-stop-user-code-kisstomato

"""
Import d'une collection
"""
# Argument :
# - collection : string : (obligatoire) Nom de la collection
def importCollection(collection):
    # kisstomato-methode-importCollection-start-user-code-kisstomato
    
    bdd = getBdd()

    file_path = os.path.join(gl.config['paths']['dump'], f"{collection}.bson")
    print( "Lecture du fichier " + file_path )
    
    documents = []
    # Le fichier est un flux de documents BSON, pas un JSON.
    # Nous le lisons en mode binaire et utilisons decode_file_iter.
    with open(file_path, 'rb') as f:
        try:
            documents = list(decode_file_iter(f))
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier BSON : {e}")
            return

    if documents:
        # Vider la collection avant d'importer les nouvelles données
        bdd[collection].delete_many({})
        # Insérer tous les documents décodés
        bdd[collection].insert_many(documents)

    # kisstomato-methode-importCollection-stop-user-code-kisstomato

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

"""
Récupère une plage d'historique
"""
# Arguments :
# - collection : string : (obligatoire) Collection cible
# - timeMin : number : (obligatoire) Temps minimum
# - timeMax : number : (obligatoire) Temps maximum
def getHistoryRange(collection, timeMin, timeMax):
    oResult = None

    # kisstomato-methode-getHistoryRange-start-user-code-kisstomato
    
    oBdd = getBdd()
    oResult = list( oBdd[ collection ].colHistory.find( { "time": {"$gte": timeMin, "$lt": timeMax } } ).sort( "time", pymongo.ASCENDING ) )
    
    # kisstomato-methode-getHistoryRange-stop-user-code-kisstomato

    return oResult

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato