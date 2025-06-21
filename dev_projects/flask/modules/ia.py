# kisstomato-module-import-start-user-code-kisstomato
import os, gl
from classes import iaAgentMM, iaEnvironnementMM
from modules import bdd
# kisstomato-module-import-stop-user-code-kisstomato

"""
Module dédié à l'IA
"""

# kisstomato-module-properties-start-user-code-kisstomato
_stopPratice = False
# kisstomato-module-properties-stop-user-code-kisstomato

"""
Stop l'apprentissage en cours
"""
def stopPratice():
    # kisstomato-methode-stopPratice-start-user-code-kisstomato
    global _stopPratice
    _stopPratice = True
    # kisstomato-methode-stopPratice-stop-user-code-kisstomato

"""
Apprentissage d'une paire
"""
# Arguments :
# - pair : string : (obligatoire) Paire associée à l'historique des images
# - modeleFile : string : (obligatoire) Nom du modèle à sauvegarder
def pratice(pair, modeleFile):
    # kisstomato-methode-pratice-start-user-code-kisstomato
    global _stopPratice
    _stopPratice = False

    # determine la taille du vecteur
    oColImage = bdd.getBdd()[ gl.config[ "mongo" ][ "cols" ][ "images_pair" ].replace( "{pair}", pair.lower() ) ]
    oImage = oColImage.find_one()
    taille_vecteur_entre = len(oImage['image']) + len(oImage['orderbook']) + 2# ajouter les 2 positions, la jauge de perte/gain et la jauge temporelle

    agent = iaAgentMM(etat_taille=taille_vecteur_entre,actions_taille=3)
    env = iaEnvironnementMM(pair=pair,environnement_taille=taille_vecteur_entre)

    # boucle d'apprentissage
    for episode in range(1000):
        if _stopPratice:
            break
        etat = env.reset()
        done = False
        rewards = 0.0
        while not done:
            if _stopPratice:
                break
            action = agent.choisir_action(etat)
            etat_suivant, reward, done = env.step(action)
            agent.apprendre(etat, action, reward, etat_suivant, done)
            etat = etat_suivant
            rewards += reward
        print(f'Épisode: {episode+1}, Récompense totale: {rewards:.2f}, Epsilon: {agent.epsilon:.2f}')

    # si le repertoire de sauvegarde n'existe pas
    if not os.path.exists( gl.config[ "paths" ][ "modeles" ] ):
        os.makedirs( gl.config[ "paths" ][ "modeles" ] )

    # enregistrement du modèles
    sModeleFile = gl.config[ "paths" ][ "modeles" ] + os.sep + modeleFile
    print( "Enregistrement du modèles : " + sModeleFile )
    agent.save(sModeleFile)
    
    # kisstomato-methode-pratice-stop-user-code-kisstomato

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato