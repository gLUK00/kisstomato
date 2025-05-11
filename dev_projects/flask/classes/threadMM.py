# kisstomato-class-import-start-user-code-kisstomato
import threading
from modules import converter
# kisstomato-class-import-stop-user-code-kisstomato

"""
Classe de calcul des moyennes mobiles
"""

class threadMM(threading.Thread):
    """
    Classe de calcul des moyennes mobiles
    """

    # kisstomato-class-properties-start-user-code-kisstomato
    # kisstomato-class-properties-stop-user-code-kisstomato

    def __init__(self, indexTime, history):
        # kisstomato-class-init-start-user-code-kisstomato
        self.disponible = True
        self.indexTime = indexTime
        self.history = history
        self.results = []
        # kisstomato-class-init-stop-user-code-kisstomato

    """
    Calcul des moyennes mobiles
    """
    def start(self):
        try:
            # kisstomato-class-methode-start-start-user-code-kisstomato

            self.disponible = False
            if len( self.history ) == 0:
                self.disponible = True
                return
            
            # compilation des minutes
            oMinutes = []
            oIndexMinutes = []
            iIndexMinutes = self.history[ 0 ][ 'time']
            for oItem in self.history:
                
                # determine la minute
                iIndexLine = converter.time2minutes( oItem[ 'time' ] )
                if iIndexLine not in oIndexMinutes:
                    oIndexMinutes.append( iIndexLine )
                    oMinutes.append( [] )
                oMinutes[ -1 ].append( oItem )
                
            for oMinute in oMinutes:
                
                # compilation de la minute
                iIndexMinutes = converter.time2minutes( oMinute[ 0 ][ 'time' ] )
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
                    "count": len( oMinute ),
                    "time": iIndexMinutes }
                
                # pour tous les prix et les quantites similaires
                oPrices = oQuantities = []
                iOpen = iClose = iVolume = iLow = iHigh = 0
                
                # pour tous les elements de la plage
                for oLine in oMinute:
                    
                    # le volume total
                    oItem[ "volume" ] += float( oLine[ "qte" ] )
                    
                    # le montant
                    oItem[ "price" ] += float( oLine[ "val" ] )
                    
                    # min et max
                    if iLow == 0 or float( oLine[ "val" ] ) < iLow:
                        iLow = float( oLine[ "val" ] )
                    if iHigh == 0 or float( oLine[ "val" ] ) > iHigh:
                        iHigh = float( oLine[ "val" ] )
                    
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

                # si la minute est vide
                if oItem[ "count" ] == 0:
                    continue

                # compilation des resultats
                oItem[ "price" ] = oItem[ "price" ] / oItem[ "count" ]
                iOpen = oMinute[ 0 ][ "val" ]
                iClose = oMinute[ -1 ][ "val" ]
                iVolume = oItem[ "volume" ]
                #oItem[ "time" ] = iIndexMinutes
                
                # enregistrement de la minute
                #oColHistory.insert_one( { "time": iIndexMinutes, "open": iOpen, "close": iClose, "volume": iVolume, "low": iLow, "high": iHigh,
                #    "1m": oItem, "5m": None, "15m": None, "30m": None, "1h": None, "2h": None, "4h": None, "8h": None, "12h": None,
                #    "1j": None, "2j": None, "5j": None, "15j": None, "1M": None } )
                
                self.results.append( { "time": iIndexMinutes, "open": iOpen, "close": iClose, "volume": iVolume, "low": iLow, "high": iHigh,
                    "1m": oItem, "5m": None, "15m": None, "30m": None, "1h": None, "2h": None, "4h": None, "8h": None, "12h": None,
                    "1j": None, "2j": None, "5j": None, "15j": None, "1M": None } )
                
                # increment de la minute
                iIndexMinutes += 60
                oMinute = []
                iOpen = iClose = iVolume = iLow = iHigh = 0

            # kisstomato-class-methode-start-stop-user-code-kisstomato
        except Exception as e:
            # kisstomato-class-exception-start-start-user-code-kisstomato
            print( "Erreur dans le calcul des moyennes mobiles" )
            print( e )
            # kisstomato-class-exception-start-stop-user-code-kisstomato
            
        # kisstomato-class-finally-start-start-user-code-kisstomato
        self.disponible = True
        # kisstomato-class-finally-start-stop-user-code-kisstomato 
