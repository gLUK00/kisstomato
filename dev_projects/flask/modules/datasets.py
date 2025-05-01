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
        
        # generation de l'image
        oImage = genImage( oRange )
        print( oImage )
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
Création d'un image à partir d'un échantillon de données
"""
# Argument :
# - buffer : array : (obligatoire) Plage mémoire de l'échantillon
def genImage(buffer):
    oResult = None

    # kisstomato-methode-genImage-start-user-code-kisstomato
    oResult = []
    
    # inverse le buffer
    buffer.reverse()
    
    # pour toutes les tranches temporelles
    oSteps = [ { "time": 60 }, # 1m
        { "time": 60 }, # 1m
        { "time": 60 }, # 1m
        { "time": 60 }, # 1m
        { "time": 60 }, # 1m
        { "time": 300 }, # 5m
        { "time": 300 }, # 5m
        { "time": 300 }, # 5m
        { "time": 900 }, # 15m
        { "time": 900 }, # 15m
        { "time": 1800 }, # 30m
        { "time": 3600 }, # 1h
        { "time": 7200 }, # 2h
        { "time": 14400 }, # 4h
        { "time": 28800 }, # 8h
        { "time": 43200 }, #12h
        { "time": 86400 }, # 1j
        { "time": 172800 }, # 2j
        { "time": 432000 }, # 5j
        { "time": 1296000 }, # 15j
        { "time": 2592000 }, # 1m
        { "time": 2592000 }, # 1m
        { "time": 2592000 } # 1m de décalage
    ]
    iTimeRef = buffer[ 0 ][ "time" ]
    #iPosStep = 0
    for oStep in oSteps:
        
        
        # recherche de l'index de rupture
        iIndexCut = 0
        for oBuffer in buffer:
            
            # si la date est inferieur à la date de reference
            if oBuffer[ "time" ] < iTimeRef - oStep[ "time" ]:
                iTimeRef = oBuffer[ "time" ]
                break
            
            iIndexCut += 1
        
        # ajustement du buffer et recuperation de la plage
        oSource = buffer[ : iIndexCut ]
        buffer = buffer[ iIndexCut : ]
        
        oItem = { "volume": 0,
            "price": 0,
            "vp": 0,
            "progress_up":0,
            "progress_down": 0,
            "nbr_buy_limit": 0,
            "nbr_buy_market": 0,
            "nbr_sell_limit": 0,
            "nbr_sell_market": 0,
            "nbr_price_similar": 0,
            "nbr_volume_similar": 0,
            "nbr_buy_round_price": 0,
            "nbr_sell_round_price": 0,
            "nbr_buy_round_qte": 0,
            "nbr_sell_round_qte": 0,
            "count": len( oSource),
            "time": oSource[ 0 ][ "time" ] }
        
        # pour tous les prix et les quantites similaires
        oPrices = oQuantities = []
        
        # pour tous les elements de la plage
        for oLine in oSource:
            
            # le volume total
            oItem[ "volume" ] += float( oLine[ "qte" ] )
            
            # le montant
            oItem[ "price" ] += float( oLine[ "val" ] )
            
            # le volume prix et quantite
            oItem[ "vp" ] += float( oLine[ "val" ] ) * float( oLine[ "qte" ] )
            
            # pour les actions
            if oLine[ "action" ] == 'b':
                if oLine[ "type" ] == 'l':
                    oItem[ "nbr_buy_limit" ] += 1
                else:
                    oItem[ "nbr_buy_market" ] += 1
            else:
                if oLine[ "type" ] == 'l':
                    oItem[ "nbr_sell_limit" ] += 1
                else:
                    oItem[ "nbr_sell_market" ] += 1
            
            # pour les tarifs similaires
            if oItem[ "price" ] not in oPrices:
                oPrices.append( oLine[ "val" ] )
            else:
                oItem[ "nbr_price_similar" ] += 1
            
            # pour les quantites similaires
            if oLine[ "qte" ] not in oQuantities:
                oQuantities.append( oLine[ "qte" ] )
            else:
                oItem[ "nbr_volume_similar" ] += 1
            
            # pour les prix ronds
            if float( oLine[ "val" ] ) == round( float( oLine[ "val" ] ) ):
                if oLine[ "action" ] == 'b':
                    oItem[ "nbr_buy_round_price" ] += 1
                else:
                    oItem[ "nbr_sell_round_price" ] += 1
                    
            # pour les quantites rondes
            if float( oLine[ "qte" ] ) == round( float( oLine[ "qte" ] ) ):
                if oLine[ "action" ] == 'b':
                    oItem[ "nbr_buy_round_qte" ] += 1
                else:
                    oItem[ "nbr_sell_round_qte" ] += 1

        # compilation des resultats
        oItem[ "price" ] = oItem[ "price" ] / oItem[ "count" ]
        oResult.append( oItem )
        
        
        # ne pas prendre le dernier item
        #iPosStep += 1
        #if iPosStep == len( oSteps ) - 1:
        #    break
        """
        
        le volume total,
le montant moyen,
progression positive,
progression negative,
le nombre d’achat limite,
le nombre d’achat market,
le nombre de vente limite,
le nombre de vente market,
le nombre de tarif similaire,
le nombre de volume similaire,
le nombre d’achat en compte rond (tarif),
le nombre de vente en compte rond (tarif),
le nombre d’achat en compte rond (quantité),
le nombre de vente en compte rond (quantité),

        """
    
    
    # suppression de la derniere plage
    oResult = oResult[ : -1 ]
    
    
    # kisstomato-methode-genImage-stop-user-code-kisstomato

    return oResult

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