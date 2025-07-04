# kisstomato-module-import-start-user-code-kisstomato
import gl, pymongo, datetime
from modules import bdd
# kisstomato-module-import-stop-user-code-kisstomato

"""
Module de debug
"""

# kisstomato-module-properties-start-user-code-kisstomato
# kisstomato-module-properties-stop-user-code-kisstomato

"""
Affichage d'un timestamp sous la forme d'une date
"""
# Argument :
# - timestamp : number : (obligatoire) timestamp à convertir
def printShowTime(timestamp):
    oResult = None

    # kisstomato-methode-printShowTime-start-user-code-kisstomato
    dt = datetime.datetime.fromtimestamp(timestamp)
    oResult = dt.strftime("%d/%m/%Y %H:%M:%S")
    # kisstomato-methode-printShowTime-stop-user-code-kisstomato

    return oResult

"""
Recherche les trous la la composition des MM
"""
# Argument :
# - pair : string : (obligatoire) Paire associée aux MM
def inspectMM(pair):
    # kisstomato-methode-inspectMM-start-user-code-kisstomato

    # recupere les collections
    oColMM = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "mm_pair" ].replace( "{pair}", pair ) ]

    # recupere le premier enregistrement
    oFirstMM = oColMM.find_one(sort=[("time", pymongo.ASCENDING)])
    iFirstTimeMM = int( oFirstMM[ 'time' ] )

    print( "premiere date : " + printShowTime( iFirstTimeMM ) )

    # pour toutes les moyennes mobiles
    oMMs = { "1m":0, "5m": 300, "15m": 900, "30m": 1800, "1h": 3600, "2h": 7200, "4h": 14400, "8h": 28800, "12h": 43200,
        "1j": 86400, "2j": 172800, "5j": 432000, "15j": 1296000 }
    
    # pour tous les champs, recherche les trous en appliquant un decalage
    for sField, iSeconds in oMMs.items():
        # recherche du premier élément où le champ sField est vide ou None
        iDecalage = iSeconds + iFirstTimeMM
        oElem = oColMM.find_one({ sField: {'$in': [None, '']}, 'time': {'$gte': iDecalage} }, sort=[('time', 1)])
        print( "recherche sur : " + sField + " depuis : " + printShowTime( iDecalage ) )
        if oElem:
            # ajoute le timestamp avec décalage
            print( sField + " : " + printShowTime( oElem['time'] + iSeconds ) )

    # kisstomato-methode-inspectMM-stop-user-code-kisstomato

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato