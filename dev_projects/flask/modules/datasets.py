# kisstomato-module-import-start-user-code-kisstomato
import gl, json, pymongo, datetime, pandas as pd, threading, time, sys, os
from pymongo import MongoClient
from bson import ObjectId
from modules import bdd, converter, debug, cache
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

    # recupere les collections
    oColMM = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "mm_pair" ].replace( "{pair}", pair ) ]
    oColImages = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "images_pair" ].replace( "{pair}", pair ) ]
    oImageHelper = imageHelper.get()

    # recupere le cache des normales
    oNormalisation = cache.getDataCache( 'normalisation/' + pair + '.json' )

    # ajustement de la normalisation
    for sField in oNormalisation:
        for sKey in oNormalisation[ sField ]:

            # ajout de 10% de marge
            oNormalisation[ sField ][ sKey ] *= 1.1


    # calcule du decalage
    #iDecalage = ( 5 * 60 * 3 ) + ( 15 * 60 * 2 ) + ( 30 * 60 ) + 3600 + ( 3600 * 2 ) + ( 3600 * 4 ) + ( 3600 * 8 ) + ( 3600 * 12 ) + 86400 + ( 86400 * 2 ) + ( 86400 * 5 ) + ( 86400 * 15 )
    iDecalage = ( 60 * 5 ) + ( 5 * 60 * 3 ) + ( 15 * 60 * 2 ) + ( 30 * 60 ) + 3600 + ( 3600 * 2 ) + ( 3600 * 4 ) + ( 3600 * 8 ) + ( 3600 * 12 ) + 86400 + ( 86400 * 2 ) + ( 86400 * 5 ) + ( 86400 * 15 )

    # recherche du premier enregistrement où la colonne 15j n'est pas vide
    # (champ existe, différent de None et de la chaîne vide)
    oFirstWith15j = oColMM.find_one({ "15j": { "$exists": True, "$ne": None, "$ne": "" } }, sort=[("time", pymongo.ASCENDING)])
    iFirstTimeMM = int( oFirstWith15j[ 'time' ] ) + iDecalage + ( 86400 * 15 )

    # recherche la position de fin
    oLastMM = oColMM.find_one(sort=[("time", pymongo.DESCENDING)])
    iLastTimeMM = int( oLastMM[ 'time' ] ) - 3600

    # calcul de 1%
    iMax = iLastTimeMM - iFirstTimeMM
    iOnePercent = float( iMax ) / 100

    # pour toutes les tranches temporelles, sans la premiere
    oSteps = [
        { "time": 0, "field": "1m" }, # 1m
        { "time": 60, "field": "1m" }, # 1m
        { "time": 60, "field": "1m" }, # 1m
        { "time": 60, "field": "1m" }, # 1m
        { "time": 60, "field": "1m" }, # 1m
        { "time": 300, "field": "5m" }, # 5m
        { "time": 300, "field": "5m" }, # 5m
        { "time": 300, "field": "5m" }, # 5m
        { "time": 900, "field": "15m" }, # 15m
        { "time": 900, "field": "15m" }, # 15m
        { "time": 1800, "field": "30m" }, # 30m
        { "time": 3600, "field": "1h" }, # 1h
        { "time": 7200, "field": "2h" }, # 2h
        { "time": 14400, "field": "4h" }, # 4h
        { "time": 28800, "field": "8h" }, # 8h
        { "time": 43200, "field": "12h" }, #12h
        { "time": 86400, "field": "1j" }, # 1j
        { "time": 172800, "field": "2j" }, # 2j
        { "time": 432000, "field": "5j" }, # 5j
        { "time": 1296000, "field": "15j" } # 15j
    ]

    # pour tous les enregistrements
    iCmpShow = 0
    for oMM in oColMM.find({ "time": { "$gte": iFirstTimeMM, "$lte": iLastTimeMM } }, sort=[("time", pymongo.ASCENDING)]):
        
        # progression
        if iCmpShow % 100 == 0:
            iProgress = ( oMM[ 'time' ] - iFirstTimeMM ) / iOnePercent
            sys.stdout.write('\r[{0:100s}] {1:.1f}%'.format('#' * int(iProgress), iProgress))
            sys.stdout.flush()
            iCmpShow = 0
        iCmpShow += 1
        
        # generation de l'image
        oImage = []
        iDecalage = 0
        for oStep in oSteps:

            iDecalage -= oStep[ 'time' ]
            oItem = oColMM.find_one({ "time": { "$lt": oMM[ 'time' ] + iDecalage } }, sort=[("time", pymongo.DESCENDING)])            

            # recupere la partie de l'image
            for sField in oNormalisation:
                for sKey in oNormalisation[ sField ]:
                    oImage.append( oImageHelper.normalize( oItem[ sField ][ sKey ], 0, oNormalisation[ sField ][ sKey ] ) )
        
        # ajout de la carte du ciel
        oImage += oMM[ 'skymap' ]
        
        # ajout de la date
        oImage += oMM[ 'date' ]

        # ajout du halving
        oImage.append( oMM[ 'halving' ] )

        # enregistrement de l'image
        oColImages.insert_one( { "time": oMM[ 'time' ], "image": oImage } )

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
Permet la vectorisation de la date et de la position du prochain Halving
"""
# Argument :
# - pair : string : (obligatoire) Paire associée à l'historique des transactions
def createDates(pair):
    # kisstomato-methode-createDates-start-user-code-kisstomato
    
    # recupere le premier enregistrement
    oColMM = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "mm_pair" ].replace( "{pair}", pair ) ]
    oElements = list( oColMM.find( { "date": None } ).limit( 100 ) )

    oImageHelper = imageHelper.get()

    # pour toutes les minutes
    iCmpShow = 0
    while oElements is not None and len(oElements) > 0:

        if iCmpShow % 10 == 0:
            print( "Dates : " + oImageHelper.date2str( oElements[ 0 ][ 'time' ] ) )
            iCmpShow = 0
        iCmpShow += 1
        
        # calcul de la carte du ciel
        for oElement in oElements:
            oColMM.update_one( { "_id": oElement[ "_id" ] }, { "$set": { "date": oImageHelper.date2vec( oElement[ 'time' ] ), "halving": oImageHelper.halvingPosition( oElement[ 'time' ] ) } } )

        # recherche d'un enregistrement
        oElements = list( oColMM.find( { "date": None } ).limit( 100 ) )

    # kisstomato-methode-createDates-stop-user-code-kisstomato

"""
Création du fichier de normalisation des données d'une paire
"""
# Argument :
# - pair : string : (obligatoire) Paire associée à l'historique des transactions
def normalisation(pair):
    # kisstomato-methode-normalisation-start-user-code-kisstomato
    
    # calcul des plages de normalisation
    oFields = [ "1m", "5m", "15m", "1h", "2h", "4h", "8h", "12h", "1j", "2j", "5j", "15j" ]
    oNormalisation = {}
    for sField in oFields:
        oNormalisation[ sField ] = {
            "volume": -1,
            "price": -1,
            "vp": -1,
            "nbr_buy_limit": -1,
            "nbr_buy_market": -1,
            "nbr_sell_limit": -1,
            "nbr_sell_market": -1,
            "nbr_volume_similar": -1,
            "nbr_buy_round_qte": -1,
            "nbr_sell_round_qte": -1,
            "count": -1
        }

    sColMM = gl.config[ "mongo" ][ "cols" ][ "mm_pair" ].replace( "{pair}", pair.lower() )
    oColMM = bdd.getBdd()[ sColMM ]

    # calcule du decalage
    iDecalage = ( 60 * 5 ) + ( 5 * 60 * 3 ) + ( 15 * 60 * 2 ) + ( 30 * 60 ) + 3600 + ( 3600 * 2 ) + ( 3600 * 4 ) + ( 3600 * 8 ) + ( 3600 * 12 ) + 86400 + ( 86400 * 2 ) + ( 86400 * 5 ) + ( 86400 * 15 )

    # recherche du premier enregistrement où la colonne 15j n'est pas vide
    # (champ existe, différent de None et de la chaîne vide)
    oFirstWith15j = oColMM.find_one({ "15j": { "$exists": True, "$ne": None, "$ne": "" } }, sort=[("time", pymongo.ASCENDING)])
    iFirstTimeMM = int( oFirstWith15j[ 'time' ] ) + iDecalage + 3600

    # pour tous les enregistrements
    for oMM in oColMM.find({ "time": { "$gte": iFirstTimeMM } }):

        # pour tous les champs
        for sField in oFields:
            
            # pour tous les indicateurs
            for sKey in oNormalisation[ sField ].keys():
                
                if float( oMM[ sField ][ sKey ] ) > oNormalisation[ sField ][ sKey ]:
                    oNormalisation[ sField ][ sKey ] = float( oMM[ sField ][ sKey ] )

    # enregistrement du cache
    cache.setDataCache( 'normalisation/' + pair + '.json', json.dumps( oNormalisation ) )

    # kisstomato-methode-normalisation-stop-user-code-kisstomato

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
            "nbr_buy_limit": 0,
            "nbr_buy_market": 0,
            "nbr_sell_limit": 0,
            "nbr_sell_market": 0,
            "nbr_volume_similar": 0,
            "nbr_buy_round_qte": 0,
            "nbr_sell_round_qte": 0,
            "count": len( oSource),
            "time": oSource[ 0 ][ "time" ] }
        
        # pour tous les prix et les quantites similaires
        oQuantities = []
        
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
            
            # pour les quantites similaires
            if oLine[ "qte" ] not in oQuantities:
                oQuantities.append( oLine[ "qte" ] )
            else:
                oItem[ "nbr_volume_similar" ] += 1
            
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
    
    # suppression de la derniere plage
    oResult = oResult[ : -1 ]
    
    # kisstomato-methode-genImage-stop-user-code-kisstomato

    return oResult

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato