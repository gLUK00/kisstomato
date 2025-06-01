# kisstomato-class-import-start-user-code-kisstomato
import threading, os ,sys
from modules import converter, debug
# kisstomato-class-import-stop-user-code-kisstomato

"""
Classe de compilation des moyennes mobiles
"""

class buildMM(threading.Thread):
    """
    Classe de compilation des moyennes mobiles
    """

    # kisstomato-class-properties-start-user-code-kisstomato
    # kisstomato-class-properties-stop-user-code-kisstomato

    def __init__(self, indexTime, sizeRange, minutes):
        # kisstomato-class-init-start-user-code-kisstomato
        self.disponible = True
        self.indexTime = indexTime
        self.sizeRange = sizeRange
        self.minutes = minutes
        self.results = []
        # kisstomato-class-init-stop-user-code-kisstomato

    """
    compilation des moyennes mobiles
    """
    def start(self):
        try:
            # kisstomato-class-methode-start-start-user-code-kisstomato
            
            self.disponible = False
            if len( self.minutes ) == 0:
                self.disponible = True
                return

            # determine la position de fin de la premier tranche
            iPosStart = iPosStop = iIndexLine = 0
            for iIndexLine in range( len( self.minutes ) ):
            #for oLine in self.minutes:

                if self.minutes[ iIndexLine ][ 'time' ] >= ( self.minutes[ 0 ][ 'time' ] + self.sizeRange ):
                #if oLine[ 'time' ] >= ( self.minutes[ 0 ][ 'time'] + self.sizeRange ):
                    iPosStop = iIndexLine
                    break
                #iPosStop += 1
            
            # pour toutes les plages
            while True:
                # Vérifier que nous avons assez de données pour la plage
                if iPosStop >= len(self.minutes):
                    break

                # Vérifier la continuité des données
                current_time = self.minutes[iPosStart]['time']
                next_time = self.minutes[iPosStop]['time']
                expected_time = current_time + self.sizeRange
                
                '''if next_time != expected_time:
                    print(f"Attention : trou détecté entre {debug.printShowTime(current_time)} et {debug.printShowTime(next_time)}")
                    print(f"Temps attendu : {debug.printShowTime(expected_time)}")
                '''
                    
                # compilation de la plage
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
                    "count": 0 }
                
                # pour la plage concernee
                for iIndexLine in range( iPosStart, iPosStop ):
                    oItem[ 'volume' ] += self.minutes[ iIndexLine ][ '1m' ][ 'volume' ]
                    oItem[ 'price' ] += self.minutes[ iIndexLine ][ '1m' ][ 'price' ]
                    oItem[ 'vp' ] += self.minutes[ iIndexLine ][ '1m' ][ 'vp' ]
                    oItem[ 'progress_up' ] += self.minutes[ iIndexLine ][ '1m' ][ 'progress_up' ]
                    oItem[ 'progress_down' ] += self.minutes[ iIndexLine ][ '1m' ][ 'progress_down' ]
                    oItem[ 'nbr_buy_limit' ] += self.minutes[ iIndexLine ][ '1m' ][ 'nbr_buy_limit' ]
                    oItem[ 'nbr_buy_market' ] += self.minutes[ iIndexLine ][ '1m' ][ 'nbr_buy_market' ]
                    oItem[ 'nbr_sell_limit' ] += self.minutes[ iIndexLine ][ '1m' ][ 'nbr_sell_limit' ]
                    oItem[ 'nbr_sell_market' ] += self.minutes[ iIndexLine ][ '1m' ][ 'nbr_sell_market' ]
                    oItem[ 'nbr_price_similar' ] += self.minutes[ iIndexLine ][ '1m' ][ 'nbr_price_similar' ]
                    oItem[ 'nbr_volume_similar' ] += self.minutes[ iIndexLine ][ '1m' ][ 'nbr_volume_similar' ]
                    oItem[ 'nbr_buy_round_price' ] += self.minutes[ iIndexLine ][ '1m' ][ 'nbr_buy_round_price' ]
                    oItem[ 'nbr_sell_round_price' ] += self.minutes[ iIndexLine ][ '1m' ][ 'nbr_sell_round_price' ]
                    oItem[ 'nbr_buy_round_qte' ] += self.minutes[ iIndexLine ][ '1m' ][ 'nbr_buy_round_qte' ]
                    oItem[ 'nbr_sell_round_qte' ] += self.minutes[ iIndexLine ][ '1m' ][ 'nbr_sell_round_qte' ]
                    oItem[ 'count' ] += self.minutes[ iIndexLine ][ '1m' ][ 'count' ]
                
                if oItem[ 'count' ] > 0:
                    oItem[ 'price' ] /= oItem[ 'count' ]
                
                # enregistrement de la plage
                self.results.append( { "id": str( self.minutes[ iPosStop ][ '_id' ] ), "data": oItem } )
                #print(f"Traitement plage : {debug.printShowTime(self.minutes[iPosStop]['time'])}")
                
                # calcul des nouvelles positions de debut et de fin
                #iPosStart = iPosStop
                iPosStop += 1
                
                # Vérifier que nous avons encore assez de données
                if iPosStop >= len(self.minutes):
                    break
                
                # Vérifier que la prochaine plage aura assez de données
                next_time = self.minutes[iPosStop]['time']
                #if next_time - self.minutes[iPosStart]['time'] < self.sizeRange:
                #    print(f"Attention : pas assez de données pour la prochaine plage")
                #    #break #print( "Sortie sur : " + str( self.minutes[ iPosStop - 1 ][ 'time' ] ) + ' : ' + debug.printShowTime( self.minutes[ iPosStop - 1 ][ 'time' ] ) )
                #    #print( "dernier ID : " + str( self.minutes[ iPosStop - 1 ][ '_id' ] ) )
                
                #print( str(  self.minutes[ iPosStop ][ 'time' ] - self.minutes[ iPosStart ][ 'time' ] ) + ' <= ' + str( self.sizeRange ) )
                while ( self.minutes[ iPosStop ][ 'time' ] - self.minutes[ iPosStart ][ 'time' ] ) > self.sizeRange:
                    """print( "sizeRange : " + str( self.sizeRange ) )
                    print( "iPosStart : " + str( self.minutes[ iPosStart ][ 'time' ] ) )
                    print( "<=" )
                    print( str( self.minutes[ iPosStop ][ 'time' ] - self.sizeRange ) )
                    print( "diff : " + str( self.minutes[ iPosStop ][ 'time' ] - self.minutes[ iPosStart ][ 'time' ] ) )
                    print( "-----------------------------------")
                    """
                    iPosStart += 1
            
            # kisstomato-class-methode-start-stop-user-code-kisstomato
        except Exception as e:
            # kisstomato-class-exception-start-start-user-code-kisstomato
            print( "Erreur dans la compilation des moyennes mobiles" )
            print( e )
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(str( e ))
            print((exc_type, fname, exc_tb.tb_lineno))
            # kisstomato-class-exception-start-stop-user-code-kisstomato
            
        # kisstomato-class-finally-start-start-user-code-kisstomato
        self.disponible = True
        # kisstomato-class-finally-start-stop-user-code-kisstomato 
