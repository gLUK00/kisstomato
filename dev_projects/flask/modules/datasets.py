# kisstomato-module-import-start-user-code-kisstomato
import gl, json, pymongo, datetime, pandas as pd, threading, time
from pymongo import MongoClient
from bson import ObjectId
from modules import bdd, converter, debug
from classes import bufferHistory, threadMM, buildMM as classBuildMM, imageHelper
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
Création des moyennes mobiles sur 1 minute
"""
# Arguments :
# - pair : string : (obligatoire) Paire associée à l'historique des transactions
# - startTime : number : (facultatif) Temps de référence du début
def createMM(pair, startTime=None):
    # kisstomato-methode-createMM-start-user-code-kisstomato
    
    oColHistory = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "history_pair" ].replace( "{pair}", pair ) ]
    oColMM = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "mm_pair" ].replace( "{pair}", pair ) ]
    
    if startTime is None or startTime == 0:
        startTime = converter.time2minutes( oColHistory.find_one( sort=[("time", pymongo.ASCENDING)] )[ 'time' ] )
    else:
        startTime = converter.time2minutes( startTime )

    # recherche des dernieres minutes
    oColHistory = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "history_pair" ].replace( "{pair}", pair ) ]
    iLastMinuteHistory = converter.time2minutes( oColHistory.find_one( sort=[("time", pymongo.DESCENDING)] )[ 'time' ] )
    
    # detemine la plage temporelle de chaque thread
    iStepTime = 18000 # 18000s = 5 hours

    # initialisation de la liste des threads
    oThreads = []
    for i in range( gl.config[ 'nbr_threads_max' ] ):
        
        # recupere la plage d'historique
        iTimeRef = startTime + ( i * iStepTime )
        oHisto = list( oColHistory.find( { "time": {"$gte": iTimeRef, "$lt": ( iTimeRef + iStepTime ) } } ).sort( "time", pymongo.ASCENDING ) )
        oThread = threadMM( indexTime=iTimeRef, history=oHisto )
        oThreads.append( oThread )
        oThread.start()

    # progression temporelle
    iIndexTimeRef = startTime
    iTimeLastIndex = startTime + ( gl.config[ 'nbr_threads_max' ] * iStepTime )
    while True:
        
        # determine si plus de donnees
        bLastData = False
        
        # pour tous les threads termines
        for oThread in oThreads:
            if oThread.disponible and oThread.indexTime == iIndexTimeRef:
                
                print( "MM : " + debug.printShowTime( oThread.indexTime) )
                
                # recupere les donnees
                if len( oThread.results ) > 0:
                    oColMM.insert_many( oThread.results, ordered=True )

                # remplacement du thread
                oHisto = list( oColHistory.find( { "time": {"$gte": iTimeLastIndex, "$lt": ( iTimeLastIndex + iStepTime ) } } ).sort( "time", pymongo.ASCENDING ) )
                if len( oHisto ) == 0 and ( iTimeLastIndex + iStepTime ) > iLastMinuteHistory:
                    bLastData = True
                    break
                oThreads.remove(oThread)
                oThread = threadMM( indexTime=iTimeLastIndex, history=oHisto )
                oThreads.append(oThread)
                oThread.start()
                
                # determine le prochain index
                iTimeLastIndex += iStepTime
                iIndexTimeRef += iStepTime

        # determine si il n'y a plus de donnees d'historique
        if bLastData:
            break
        
        # pause de 5 secondes
        time.sleep( 0.1 )

    # kisstomato-methode-createMM-stop-user-code-kisstomato

"""
Calcul le reste des moyennes mobiles
"""
# Argument :
# - pair : string : (obligatoire) Paire associée à l'historique des minutes
def buildMM(pair):
    # kisstomato-methode-buildMM-start-user-code-kisstomato
    
    # detemine la plage temporelle de chaque thread
    iStepTime = 18000 # 18000s = 5 hours
    iBackTime = 86400 # 86400s = 1 day
    
    # recupere le premier enregistrement
    oColMM = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "mm_pair" ].replace( "{pair}", pair ) ]
    iFirstMinuteMM = converter.time2minutes( oColMM.find_one( sort=[("time", pymongo.ASCENDING)] )[ 'time' ] )
    
    # pour toutes les moyennes mobiles
    oMMs = {  "5m": 300, "15m": 900, "30m": 1800, "1h": 3600, "2h": 7200, "4h": 14400, "8h": 28800, "12h": 43200,
        "1j": 86400, "2j": 172800, "5j": 432000, "15j": 1296000 }
    for sField, iSeconds in oMMs.items():
        
        print( "Compilation MM : " + sField )

        # determine si il y a deja eu des calculs
        iStartTime = 0

        oElement = oColMM.find_one( { "$or": [
            { sField: { "$eq": None } },
            { sField: "" }
        ], "time": { "$gte": iFirstMinuteMM + iSeconds + iBackTime } }, sort=[("time", pymongo.ASCENDING)] )

        # determine si il y a des calculs
        if oElement is not None:
            iStartTime = converter.time2minutes( oElement[ "time" ] )
        else:
            print( 'Compilation MM ; déjà effectuée : ' + sField )
            continue
        
        # si c'est la premier minute
        if iStartTime == iFirstMinuteMM:
            iStartTime += iSeconds

        iStopTime = iStartTime + iSeconds + iStepTime
        
        # initialisation de la liste des threads
        oThreads = []
        for i in range( gl.config[ 'nbr_threads_max' ] ):
        
            # recupere la plage des MM
            oMM = list( oColMM.find( { "time": {"$gte": iStartTime - iSeconds - iBackTime, "$lt": iStopTime } } ).sort( "time", pymongo.ASCENDING ) )

            # si pas assez de données
            iDiffTime = oMM[ -1 ][ 'time' ] - oMM[ 0 ][ 'time' ]
            while iDiffTime < ( iSeconds + iStepTime ):
                
                iStartTime -= 60
                oMM = list( oColMM.find( { "time": {"$gte": iStartTime - iSeconds - iBackTime, "$lt": iStopTime } } ).sort( "time", pymongo.ASCENDING ) )
                iDiffTime = oMM[ -1 ][ 'time' ] - oMM[ 0 ][ 'time' ]

            oThread = classBuildMM( indexTime=iStartTime, sizeRange=iSeconds, minutes=oMM )
            oThreads.append( oThread )
            oThread.start()

            # determine si il y a d'autres enregistrements
            oElement = oColMM.find_one( { "$or": [
                { sField: { "$eq": None } },
                { sField: "" }
            ], "time": { "$gte": iStopTime } }, sort=[("time", pymongo.ASCENDING)] )
            if oElement is None:
                break
            
            iStartTime = converter.time2minutes( oElement[ "time" ] )
            iStopTime = iStartTime + iSeconds + iStepTime
            
        
        # progression temporelle
        iCmpShow = 0
        while True:
            
            # pour tous les threads termines
            for oThread in oThreads:
                if oThread.disponible:
                    
                    if iCmpShow % 100 == 0:
                        print( "MM : " + sField + ' : ' +str( datetime.datetime.strptime( str( datetime.datetime.fromtimestamp( int( oThread.indexTime ) ) ), '%Y-%m-%d %H:%M:%S' ) ) )
                        iCmpShow = 0
                    iCmpShow += 1

                    # enregistrement des resultats
                    for oUpdate in oThread.results:
                        doc_id = ObjectId(oUpdate["id"])
                        oColMM.update_one(
                            {"_id": doc_id},
                            {"$set": {sField: oUpdate['data']}},
                            upsert=False  # Ne crée pas de nouveau document si non trouvé
                        )
                    
                    # determine si il y a d'autres enregistrements
                    oElement = oColMM.find_one( { sField: None, "time": { "$gte": iStopTime } }, sort=[("time", pymongo.ASCENDING)] )
                    if oElement is None:
                        oThreads.remove(oThread)
                        continue
                    
                    iStartTime = converter.time2minutes( oElement[ "time" ] )
                    iStopTime = iStartTime + iSeconds + iStepTime

                    # recupere la plage des MM
                    oMM = list( oColMM.find( { "time": {"$gte": iStartTime - iSeconds - iBackTime, "$lt": iStopTime } } ).sort( "time", pymongo.ASCENDING ) )

                    # si pas assez de données
                    iDiffTime = oMM[ -1 ][ 'time' ] - oMM[ 0 ][ 'time' ]
                    while iDiffTime < ( iSeconds + iStepTime ):
                        
                        iStartTime -= 60
                        oMM = list( oColMM.find( { "time": {"$gte": iStartTime - iSeconds - iBackTime, "$lt": iStopTime } } ).sort( "time", pymongo.ASCENDING ) )
                        iDiffTime = oMM[ -1 ][ 'time' ] - oMM[ 0 ][ 'time' ]
                    
                    # remplacement du thread
                    oThreads.remove(oThread)
                    oThread = classBuildMM( indexTime=iStartTime, sizeRange=iSeconds, minutes=oMM )
                    oThreads.append(oThread)
                    oThread.start()

            # determine si il n'y a plus de donnees d'historique
            if len(oThreads) == 0:
                break
            
            # pause de 5 secondes
            time.sleep( 0.1 )

    # kisstomato-methode-buildMM-stop-user-code-kisstomato

"""
Génération de la carte du ciel pour une paire
"""
# Argument :
# - pair : string : (obligatoire) Paire associée à l'historique des minutes
def createSkymap(pair):
    # kisstomato-methode-createSkymap-start-user-code-kisstomato
    
    # recupere le premier enregistrement
    oColMM = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "mm_pair" ].replace( "{pair}", pair ) ]
    oElements = list( oColMM.find( { "skymap": None } ).limit( 100 ) )

    oImageHelper = imageHelper.get()

    # pour toutes les minutes
    iCmpShow = 0
    while oElements is not None and len(oElements) > 0:

        if iCmpShow % 10 == 0:
            print( "Skymap : " + oImageHelper.date2str( oElements[ 0 ][ 'time' ] ) )
            iCmpShow = 0
        iCmpShow += 1
        
        # calcul de la carte du ciel
        for oElement in oElements:
            oColMM.update_one( { "_id": oElement[ "_id" ] }, { "$set": { "skymap": oImageHelper.skymap2time( oElement[ 'time' ] ) } } )

        # recherche d'un enregistrement
        oElements = list( oColMM.find( { "skymap": None } ).limit( 100 ) )

    # kisstomato-methode-createSkymap-stop-user-code-kisstomato

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
        { "time": 1296000 } # 15j
    ]
    iTimeRef = buffer[ 0 ][ "time" ]
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
    
    # pour toutes les plages sans la derniere
    for i in range( len( oResult ) ):
        
        # si la plage est vide
        if oResult[ i ][ "count" ] == 0:
            continue
        
        # recherche de l'index de la plage precedente
        iIndexPrec = i + 1
        while oResult[ iIndexPrec ][ "count" ] == 0:
            iIndexPrec += 1
        
        # calcul de la progression
        iDiff = oResult[ i ][ "price" ] - oResult[ iIndexPrec ][ "price" ]
        if iDiff > 0:
            oResult[ i ][ "progress_up" ] = abs( iDiff / ( oResult[ iIndexPrec ][ "price" ] / 100 ) )
            oResult[ i ][ "progress_down" ] = 0
        elif iDiff < 0:
            oResult[ i ][ "progress_up" ] = 0
            oResult[ i ][ "progress_down" ] = abs( iDiff / ( oResult[ iIndexPrec ][ "price" ] / 100 ) )
    
    # suppression de la derniere plage
    oResult = oResult[ : -1 ]
    
    # kisstomato-methode-genImage-stop-user-code-kisstomato

    return oResult

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato