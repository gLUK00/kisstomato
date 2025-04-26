# kisstomato-module-import-start-user-code-kisstomato
import gl, json, pymongo, datetime
from pymongo import MongoClient
from modules import bdd
from classes import bufferHistory
# kisstomato-module-import-stop-user-code-kisstomato

"""
Module de gestion des Datasets
"""

# kisstomato-module-properties-start-user-code-kisstomato
# kisstomato-module-properties-stop-user-code-kisstomato

"""
Initialisation d'un Dataset
"""
# Argument :
# - pair : string : (obligatoire) Paire associée à l'historique des transactions
def init(pair):
    # kisstomato-methode-init-start-user-code-kisstomato

    sColImages = gl.config[ "mongo" ][ "cols" ][ "images_pair" ].replace( "{pair}", pair )
    bdd.dropCollection( sColImages, createIndex='time' )

    # kisstomato-methode-init-stop-user-code-kisstomato

"""
Création d'un dataset à partir de l'historique des transactions
"""
# Argument :
# - pair : string : (obligatoire) Paire associée à l'historique des transactions
def create(pair):
    # kisstomato-methode-create-start-user-code-kisstomato

    # initialisation du buffer
    oBuffer = bufferHistory( pair )

    iDebug = 0

    # pour toutes les tranches
    for oRange in oBuffer:

        print( '-----------------------' )
        print( len( oRange ) )

        print( oRange[ 0 ] )
        print( oRange[ -1 ] )



        print( datetime.datetime.strptime( str( datetime.datetime.fromtimestamp( int( oRange[ 0 ][ 'time' ] ) ) ), '%Y-%m-%d %H:%M:%S' ) )
        print( datetime.datetime.strptime( str( datetime.datetime.fromtimestamp( int( oRange[ -1 ][ 'time' ] ) ) ), '%Y-%m-%d %H:%M:%S' ) )
        
        """iDiffTime = int( oRange[ -1 ][ 'time' ] ) - int( oRange[ 0 ][ 'time' ] )
        print( iDiffTime )

        print( '-------------------------- simu' )
        iDiffTime = 9849620 - int( oRange[ 0 ][ 'time' ] )
        
        print( datetime.datetime.strptime( str( datetime.datetime.fromtimestamp( int( oRange[ 0 ][ 'time' ] ) ) ), '%Y-%m-%d %H:%M:%S' ) )
        print( datetime.datetime.strptime( str( datetime.datetime.fromtimestamp( int( oRange[ 0][ 'time' ] ) + 9849620 ) ), '%Y-%m-%d %H:%M:%S' ) )
        
        iDiffTime = int( oRange[ -1 ][ 'time' ] ) - 9849620
        print( iDiffTime )
        """
        iDebug += 1

        if iDebug == 10:
            exit()

    exit()
    

    sColHistory = gl.config[ "mongo" ][ "cols" ][ "history_pair" ].replace( "{pair}", pair )
    sColImages = gl.config[ "mongo" ][ "cols" ][ "images_pair" ].replace( "{pair}", pair )
    oColHistory = bdd.getBdd()[ sColHistory ]

    # pour toutes les plages de donnees
    iIndexTime = 0
    while True:
        bExist = True
        oLines = oColHistory.find( { "time": { "$gte": iIndexTime } } ).sort( "time", pymongo.ASCENDING ).limit( 100 )
        for oLine in oLines:
            bExist = False
            iIndexTime = oLine[ "time" ]



            print( oLine )

            #exit()


        if bExist:
            break



        exit()



    # kisstomato-methode-create-stop-user-code-kisstomato

"""
Normalise une valeur sur un place de 0 à 1
"""
# Arguments :
# - iVal : number : (obligatoire) Valeur d'entrée
# - iMin : number : (obligatoire) Valeur minimum
# - iMax : number : (obligatoire) Valeur maximum
def normalize(iVal, iMin, iMax):
    oResult = None

    # kisstomato-methode-normalize-start-user-code-kisstomato
    iRange = iMax - iMin
    iDiffMin = abs( iVal - iMin )
    iStep = iRange / 100
    oResult = ( iDiffMin / iStep ) * 0.01
    # kisstomato-methode-normalize-stop-user-code-kisstomato

    return oResult

"""
Retourne un vecteur de carte du ciel à partir d'un timestamp
"""
# Argument :
# - iTime : number : (obligatoire) Timestamp de référence
def skymap2time(iTime):
    oResult = None

    # kisstomato-methode-skymap2time-start-user-code-kisstomato
    oResult = []

    # conversion de la date
    date_time = datetime.datetime.fromtimestamp(iTime)
    sDate = datetime.datetime.strptime( str(date_time), '%Y-%m-%d %H:%M:%S' )

    # pour toutes les planetes
    for p in [ ephem.Mercury( sDate ), ephem.Venus( sDate ), ephem.Mars( sDate ), ephem.Jupiter( sDate ), ephem.Saturn( sDate ), ephem.Uranus( sDate ), ephem.Neptune( sDate ), ephem.Pluto( sDate ), ephem.Sun( sDate ), ephem.Moon( sDate ), ephem.Phobos( sDate ), ephem.Deimos( sDate ), ephem.Io( sDate ), ephem.Europa( sDate ), ephem.Ganymede( sDate ), ephem.Callisto( sDate ), ephem.Mimas( sDate ), ephem.Enceladus( sDate ), ephem.Tethys( sDate ), ephem.Dione( sDate ), ephem.Rhea( sDate ), ephem.Titan( sDate ), ephem.Hyperion( sDate ), ephem.Iapetus( sDate ), ephem.Ariel( sDate ), ephem.Umbriel( sDate ), ephem.Titania( sDate ), ephem.Oberon( sDate ), ephem.Miranda( sDate ) ]:
        oResult.append( normalize( p.a_ra + 0.0, 0, 6.5 ) )
        oResult.append( normalize( p.a_dec + 0.0, -0.5, +0.5 ) )
        if 'earth_distance' in dir(p):
            oResult.append( normalize( p.earth_distance + 0.0, 0, 50 ) )
        if 'phase' in dir(p):
            oResult.append( normalize( p.phase + 0.0, 0, 100 ) )
        if 'mag' in dir(p):
            oResult.append( normalize( p.mag + 0.0, -27, 15 ) )
    # kisstomato-methode-skymap2time-stop-user-code-kisstomato

    return oResult

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato