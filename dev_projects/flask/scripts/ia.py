# coding=utf-8
import argparse

# kisstomato-script-import-start-user-code-kisstomato
import signal
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules import services, ia, configuration
# kisstomato-script-import-stop-user-code-kisstomato

"""
Script dédié aux modèles d'IA
"""

# kisstomato-script-init-start-user-code-kisstomato
configuration.load()
# kisstomato-script-init-stop-user-code-kisstomato

print( "Script dédié aux modèles d'IA" )

# recuperation des arguments
oParser = argparse.ArgumentParser( prog="ia", description="Script dédié aux modèles d'IA" )

# kisstomato-script-arg-start-start-user-code-kisstomato
# kisstomato-script-arg-start-stop-user-code-kisstomato

# kisstomato-script-arg-pair-a-start-user-code-kisstomato
# kisstomato-script-arg-pair-a-stop-user-code-kisstomato
oParser.add_argument( "--pair", required=True )
# kisstomato-script-arg-pair-b-start-user-code-kisstomato
# kisstomato-script-arg-pair-b-stop-user-code-kisstomato

sSwitchSection = None
oParser.add_argument("--goto", required=False, help="Label de section vers laquelle sauter directement")
oArgs = oParser.parse_args()

# Gestion de l'argument facultatif --goto
oSection = []
oSection.append( "controle" )
oSection.append( "pratice" )
if hasattr(oArgs, "goto") and oArgs.goto:
    if oArgs.goto not in oSection:
        print(f"Erreur: le label '{oArgs.goto}' n'existe pas. Labels valides : {oSection}")
        exit(1)
    else:
        sSwitchSection = oArgs.goto

# kisstomato-script-arg-end-start-user-code-kisstomato

# detection du CTRL+C
def signal_handler(sig, frame):
    print("\nInterruption détectée ! Le programme a été arrêté par l'utilisateur avec CTRL+C.")
    ia.stopPratice()
    print("Au revoir !")
    exit(0)

# Associer le gestionnaire au signal SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

sInPair = oArgs.pair.lower()

# kisstomato-script-arg-end-stop-user-code-kisstomato

if sSwitchSection is None or sSwitchSection == "controle":
    
    """
    Contrôle de la paire
    """
    print( "\n>> CONTRÔLE DE LA PAIRE\n" )
    # kisstomato-script-section-controle-start-user-code-kisstomato

    # recherche si la paire existe
    bExist = False
    oOthersChoices = []
    for sPair in services.getPairs()[ 'result' ]:
        if sPair.lower() == sInPair:
            bExist = True
            break
        if sPair.lower().find( sInPair ) != -1:
            oOthersChoices.append( sPair.lower() )

    # si il n'y a pas de correspondance
    if not bExist and len( oOthersChoices ) == 0:
        print( "Paire introuvable" )
        exit()

    # si la paire n'est pas trouve et qu'il y a des alternatives
    if not bExist:
        print( "Paire introuvable" )
        print( "Proposition alternative(s)" )
        for i in range( len( oOthersChoices ) ):
            print( str( i + 1 ) + ' - ' + oOthersChoices[ i ] + ' >> ' + services.getPairs()[ 'result' ][ oOthersChoices[ i ].upper() ][ 'wsname' ] )

        try:
            iChoise = int( input( '>> ? ' ) )
            if iChoise < 1 or iChoise > len( oOthersChoices ):
                raise()
            sInPair = oOthersChoices[ iChoise - 1 ]

        except Exception as e:
            print( "Paire introuvable" )
            exit()

    # kisstomato-script-section-controle-stop-user-code-kisstomato
    sSwitchSection = None

if sSwitchSection is None or sSwitchSection == "pratice":
    
    """
    Processus d'apprentissage d'un modèle
    """
    print( "\n>> PROCESSUS D'APPRENTISSAGE D'UN MODÈLE\n" )
    # kisstomato-script-section-pratice-start-user-code-kisstomato

    # demande du nom du fichier de sauvegarde
    sModeleFile = input( 'Nom du fichier de sauvegarde du modèle ? (modele_' + sInPair + '.data) ' )
    if sModeleFile == "":
        sModeleFile = "modele_" + sInPair + ".data"

    # demarrage de l'apprentissage
    ia.pratice( sInPair, sModeleFile )

    # kisstomato-script-section-pratice-stop-user-code-kisstomato
    sSwitchSection = None

# kisstomato-script-end-start-user-code-kisstomato
# kisstomato-script-end-stop-user-code-kisstomato