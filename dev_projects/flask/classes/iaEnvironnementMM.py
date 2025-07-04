# kisstomato-class-import-start-user-code-kisstomato
from classes import imageHelper
from modules import bdd
import time, gl, pymongo
import numpy as np
# kisstomato-class-import-stop-user-code-kisstomato

"""
Environnement IA sur les MM
"""

class iaEnvironnementMM:
    """
    Environnement IA sur les MM
    """

    # kisstomato-class-properties-start-user-code-kisstomato
    # kisstomato-class-properties-stop-user-code-kisstomato

    def __init__(self, pair, environnement_taille):
        # kisstomato-class-init-start-user-code-kisstomato

        self.compteurActions = 0
        self.pair = pair

        # indicateurs temporels
        self.jaugeTemp = 0
        self.maxSansAction = 60 * 60 * 24 * 30 * 2 # 2 mois
        self.maxAvecAchat = 60 * 60 * 2 # 2 heures
       
        self.environnement_taille = environnement_taille
        self.currentId = None
        self.fees = 0.40 # pourcentage de fees
        """
        rentabilite global a 0.5, pour :
        - 0 = - 10000%
        - 0.5 = 0%
        - 1 = + 10000%  
        """
        self.rentabilite = 0.5 # valeur de rentabilite / 10.000, pout 0=-5000%, 0.5=0%, 1=5000%
        self.prixAchat = 0
        self.qteAchat = 0
        self.gain = 0.5 # 0=-50%, neutre: 0.5=0%, gain: 1=50%
        self.etat = self.reset()
        self.timeLast = time.time() # date de la derniere action
        self.achatEnCours = False

        # determine l'id de fin
        oColImage = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "images_pair" ].replace( "{pair}", self.pair.lower() ) ]
        oLastImage = oColImage.find_one(sort=[("_id", pymongo.DESCENDING)])

        # supprime 1 an
        iDate = int( oLastImage[ 'time' ] ) - 31536000
        oLastImage = oColImage.find_one({ "time": { "$gte": iDate } }, sort=[("_id", pymongo.DESCENDING)])
        self.lastId = oLastImage['_id']

        # kisstomato-class-init-stop-user-code-kisstomato

    """
    Reset de expérience
    """
    def reset(self):
        oResult = None

        # kisstomato-class-methode-reset-start-user-code-kisstomato

        """
        recupere l'id du premier enregistrement de l'image en bdd
        self.currentId = l'id
        recuperer l'image et y ajouter :
        - le portefeuille
        - la progression perte par rapport aux actions
            - perte de 50 % ou + => -0.5
            - gain de 50 % ou + => 0.5
        - une jauge temporelle, qui represente une sorte de sablier/compteur,
            - sur une heure, se decremente lors d'une action d'achat
            - revient à 0 si vente

        """
        
        # recupere l'id de la premiere image
        oColImage = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "images_pair" ].replace( "{pair}", self.pair.lower() ) ]
        oImage = oColImage.find_one()
        self.currentId = oImage['_id']

        # decalage de 1 mois et 1 jour
        #self.currentId = oColImage.find_one({ "time": { "$gte": oImage['time'] + 31536000 + 86400 } }, sort=[("_id", pymongo.ASCENDING)])

        # recupere l'image
        oImage = oColImage.find_one( { "_id": self.currentId } )
        self.rentabilite = 0
        self.prixAchat = 0
        self.qteAchat = 0
        self.gain = 0.5
        self.jaugeTemp = 0
        self.timeLast = oImage['time']
        self.achatEnCours = False
        self.etat = np.concatenate(([self.gain, self.jaugeTemp], oImage['image'], oImage['orderbook']))
        oResult = self.etat
        self.compteurActions = 0

        # kisstomato-class-methode-reset-stop-user-code-kisstomato
        return oResult

    """
    Méthode de passage à l'étape suivante
    """
    # Argument :
    # - action : number : (obligatoire) Action donnée
    def step(self, action):
        oResult = None

        # kisstomato-class-methode-step-start-user-code-kisstomato

        oImageHelper = imageHelper.get()

        """
        action :
            0 : hold
            1 : achete
            2 : vente
        """

        # recupere la prochaine image
        oColImage = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "images_pair" ].replace( "{pair}", self.pair.lower() ) ]
        oNextImage = oColImage.find_one({ "_id": { "$gt": self.currentId } }, sort=[("_id", 1)])
        iCurrentTime = int( oNextImage['time'] )
        self.currentId = oNextImage['_id']

        # determine si la plage et termine
        if self.currentId == self.lastId:
            done = True
        else:
            done = False

        # recupere l'orderbook
        oOrderBook = oImageHelper.vec2Orderbook( oNextImage['orderbook'] )

        # determine la recompense
        # si: etat=vide et (hold ou vente)
        # ou si: etat=achete et achete
        reward = 0
        if not self.achatEnCours and ( action == 0 or action == 2 ) or ( self.achatEnCours and action == 1 ):
            
            # determine la distance temporelle entre la derniere action
            iTimeDiff = iCurrentTime - self.timeLast

            # calcul de la penalite temporelle
            # entre -0.5 et 0
            reward = oImageHelper.normalize( iTimeDiff, 0, self.maxSansAction, iMinTarget=-0.5, iMaxTarget=0, bMin2Max=False )
            #print( 'reward : ' + str(reward))
            #reward = ( oImageHelper.normalize( iTimeDiff, 0, self.maxSansAction ) / 2 ) * -1

            # avance la jauge temporelle
            self.jaugeTemp = oImageHelper.normalize( iTimeDiff, 0, self.maxSansAction )

        #  ou si: etat=achete et hold
        elif self.achatEnCours and action == 0:

            # determine la distance temporelle entre la derniere action
            iTimeDiff = iCurrentTime - self.timeLast

            # calcul de la penalite temporelle
            # entre -0.5 et 0
            reward = oImageHelper.normalize( iTimeDiff, 0, self.maxAvecAchat, iMinTarget=-0.5, iMaxTarget=0, bMin2Max=False )
            #print( 'reward : ' + str(reward))
            #reward = ( oImageHelper.normalize( iTimeDiff, 0, self.maxAvecAchat ) / 2 ) * -1

            # avance la jauge temporelle
            self.jaugeTemp = oImageHelper.normalize( iTimeDiff, 0, self.maxAvecAchat )
        
        # ou si: etat=vide et achete
        elif not self.achatEnCours and action == 1:

            self.achatEnCours = True
            self.timeLast = iCurrentTime

            # la partie de la premiere vente
            #print( 'prix achat : ' + str(oOrderBook[ 'ventes' ][ -1 ][ 'price' ]))
            #print( 'frais : ' + str(self.fees))
            #print( 'prix reel : ' + str(oOrderBook[ 'ventes' ][ -1 ][ 'price' ] + ( oOrderBook[ 'ventes' ][ -1 ][ 'price' ] * (self.fees / 100) )))
            self.prixAchat = oOrderBook[ 'ventes' ][ -1 ][ 'price' ] + ( oOrderBook[ 'ventes' ][ -1 ][ 'price' ] * (self.fees / 100) ) # ajoute les frais
            self.qteAchat = oOrderBook[ 'ventes' ][ -1 ][ 'volume' ] * 0.9 # recupere 90% de la quantite

            # modifier l'image de l'orderbook
            oOrderBook[ 'ventes' ][ -1 ][ 'volume' ] = oOrderBook[ 'ventes' ][ -1 ][ 'volume' ] * 0.1

            # ajuster le gain/perte global a 0.5, mois les frais pour :
            # - 0 = -50%
            # - 0.5 = 0%
            # - 1 = + 50%
            # TODO : normaliser sur la rentabilite
            self.gain = oImageHelper.normalize( self.fees / 2, 0, 100, iMinTarget=-0.5, iMaxTarget=0, bMin2Max=False )
            #print( 'gain : ' + str(self.gain))
            #self.gain = 0.5 - ( oImageHelper.normalize( self.fees, 0, 100 ) / 2 )

            # initialisation de la jauge temporelle
            self.jaugeTemp = 0

        # etat=achete et vendre
        elif self.achatEnCours and action == 2:

            # mise a jour de l'etat
            self.achatEnCours = False
            self.timeLast = iCurrentTime
            self.jaugeTemp = 0

            # determine le prix de vente
            iPrixVente = 0
            iQteVente = 0
            iPosition = 0
            while iQteVente < self.qteAchat and iPosition < len(oOrderBook[ 'achats' ]):
                iQteVente += oOrderBook[ 'achats' ][ iPosition ][ 'volume' ]
                iPrixVente = oOrderBook[ 'achats' ][ iPosition ][ 'price' ]
                iPosition += 1

            # ajout des frais
            iPrixVente += ( iPrixVente * (self.fees / 100) )

            # determine le % de gain/perte
            #print( 'prix vente : ' + str(iPrixVente))
            #print( 'prix achat : ' + str(self.prixAchat))

            # determine le gain
            iGain = ( iPrixVente - self.prixAchat ) / self.prixAchat
            #print( 'gain : ' + str(iGain))

            # determine la recompense
            if iGain < 0:
                reward = oImageHelper.normalize( abs( iGain ), 0, 100, iMinTarget=-0.5, iMaxTarget=0, bMin2Max=False )
                print( 'reward -- : ' + str(reward))
            else:
                reward = oImageHelper.normalize( iGain, 0, 100, iMinTarget=0, iMaxTarget=0.5 )
                print( 'reward ++ : ' + str(reward))

            # actualise la rentabilite
            self.rentabilite += iGain/500
            self.compteurActions += 1

        else:
            print( "action non reconnue : " + str(action) )

        # Simuler l'effet de l'action sur l'environnement
        # Ici, on simule simplement une récompense aléatoire et un nouvel état
        #reward = np.random.rand() - 0.5  # Récompense entre -0.5 et 0.5

        """
        si il reste 20% du portefeuille initial
        si achat depuis plus de 1h30m
        """
        #print( self.achatEnCours and ( iCurrentTime - self.timeLast ) > 60*60*1.5 )
        #print( iCurrentTime - self.timeLast )

        # determine si la rentabilite est trop faible
        bNotRentabilite = self.rentabilite < -0.3
        if bNotRentabilite:
            print( "Rentabilite trop faible : " + str(self.rentabilite) )

        # determine si l'achat est trop ancien
        bNotTime = self.achatEnCours and ( iCurrentTime - self.timeLast ) > 60*60*1.5
        if bNotTime:
            print( "Achat trop ancien : " + str(iCurrentTime - self.timeLast) )

        done = bNotRentabilite or bNotTime or done

        if done:
            print( "Fin avec " + str(self.compteurActions) + " action, rentabilite : " + str(self.rentabilite) )

        # construction du nouvel etat
        self.etat = np.concatenate(([self.gain, self.jaugeTemp], oNextImage['image'], oNextImage['orderbook']))
        
        oResult = self.etat, reward, done

        # kisstomato-class-methode-step-stop-user-code-kisstomato
        return oResult

