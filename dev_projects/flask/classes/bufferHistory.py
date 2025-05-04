# kisstomato-class-import-start-user-code-kisstomato
import gl, pymongo, datetime
import pandas as pd
from pymongo import MongoClient
from modules import bdd
# kisstomato-class-import-stop-user-code-kisstomato

"""
Buffer d'historique d'une paire
"""

class bufferHistory:

    # kisstomato-class-properties-start-user-code-kisstomato
    # kisstomato-class-properties-stop-user-code-kisstomato

    def __init__(self, pair, sizeBuffer=None, sizeImage=None):
        # kisstomato-class-init-start-user-code-kisstomato
        self.pair = pair
        self.sizeBuffer = 12000000 # nombre de secondes du buffer
        if sizeBuffer != None:
            self.sizeBuffer = sizeBuffer
        self.sizeImage = 9849620 # pour 114j 4:20
        if sizeImage != None:
            self.sizeImage = sizeImage

        sColHistory = gl.config[ "mongo" ][ "cols" ][ "history_pair" ].replace( "{pair}", pair )

        self.colHistory = bdd.getBdd()[ sColHistory ]

        # recherche de l'index
        oFirst = self.colHistory.find_one( { "time": { "$gte": 0 } }, sort=[("time", pymongo.ASCENDING)] )
        #self.indexTime = int( oFirst[ 'time' ] )

        # positionnement a la minute
        date = pd.to_datetime( datetime.datetime.strptime( str( datetime.datetime.fromtimestamp( int( oFirst[ 'time' ] ) ) ), '%Y-%m-%d %H:%M:%S' ) )
        self.indexTime = int( date.round('T').timestamp() ) + 60

        """print( 'tttttttttttttttt' )

        print( datetime.datetime.strptime( str( datetime.datetime.fromtimestamp( int( oFirst[ 'time' ] ) ) ), '%Y-%m-%d %H:%M:%S' ) )

        
        print("Original:", date)
        print("Rounded to minute:", date.round('T'))
        print( int( date.round('T').timestamp() ) )

        exit()
        """

        # premier chargement du buffer
        self.buffer = list( self.colHistory.find( { "time": {"$gte": self.indexTime, "$lt": ( self.indexTime + self.sizeBuffer ) } } ).sort( "time", pymongo.ASCENDING ) )

        # kisstomato-class-init-stop-user-code-kisstomato

    """
    Iterateur
    """
    def __iter__(self):
        oResult = None

        # kisstomato-class-methode-__iter__-start-user-code-kisstomato
        oResult = self
        # kisstomato-class-methode-__iter__-stop-user-code-kisstomato

        return oResult
    """
    Retourne la plage suivante
    """
    def __next__(self):
        oResult = None

        # kisstomato-class-methode-__next__-start-user-code-kisstomato

        # si le buffer est trop petit
        iMaxTime = self.indexTime + self.sizeImage

        #print( len( self.buffer ) )
        #exit()
        if int( self.buffer[ -1 ][ 'time' ] ) < iMaxTime:

            # alimentation du buffer
            self.buffer += list( self.colHistory.find( { "time": {"$gt": ( self.buffer[ -1 ][ 'time' ] ), "$lt": ( self.buffer[ -1 ][ 'time' ] + self.sizeBuffer ) } } ).sort( "time", pymongo.ASCENDING ) )

            # si c'est le dernier enregitrement
            if int( self.buffer[ -1 ][ 'time' ] ) < iMaxTime:
                raise StopIteration

        # recupere la plage depuis le buffer
        iIndexStart = 0
        iIndexStop = 0
        for oEle in self.buffer:
            iTimeRef = int( oEle[ 'time' ] )
            if iTimeRef < self.indexTime:
                iIndexStart += 1
            if iTimeRef > iMaxTime:
                break
            iIndexStop += 1


        #print( iIndexStart )
        #print( iIndexStop )

        #exit()

        print( 'AA ' + str( iIndexStart ) )
        print( 'BB ' + str( iIndexStop ) )



        # recupere la plage
        oResult = self.buffer[ iIndexStart : iIndexStop ]

        # avancement d'une minute
        self.indexTime += 60

        # reduction memoire du buffer
        if iIndexStart > 0:
            self.buffer = self.buffer[ iIndexStart : ]
        
        # kisstomato-class-methode-__next__-stop-user-code-kisstomato

        return oResult
