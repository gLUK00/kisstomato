# coding=utf-8
import argparse

# kisstomato-script-import-start-user-code-kisstomato
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import gl
from modules import configuration, bdd, services, datasets
# kisstomato-script-import-stop-user-code-kisstomato

"""
Script de création d'un dataset
"""

# kisstomato-script-init-start-user-code-kisstomato
configuration.load()
# kisstomato-script-init-stop-user-code-kisstomato

print( "Script de création d'un dataset" )

# recuperation des arguments
oParser = argparse.ArgumentParser( prog="dataset", description="Script de création d'un dataset" )

# kisstomato-script-arg-start-start-user-code-kisstomato
# kisstomato-script-arg-start-stop-user-code-kisstomato

# kisstomato-script-arg-pair-a-start-user-code-kisstomato
# kisstomato-script-arg-pair-a-stop-user-code-kisstomato
oParser.add_argument( "--pair", required=True )
# kisstomato-script-arg-pair-b-start-user-code-kisstomato
# kisstomato-script-arg-pair-b-stop-user-code-kisstomato

oArgs = oParser.parse_args()

# kisstomato-script-arg-end-start-user-code-kisstomato
# kisstomato-script-arg-end-stop-user-code-kisstomato

"""
Contrôle de la paire
"""
print( "\n>> CONTRÔLE DE LA PAIRE\n" )
# kisstomato-script-section-controle-start-user-code-kisstomato

# recherche si la paire existe
sInPair = oArgs.pair.lower()
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

    #if input( '>> ? ' ):
    try:
        iChoise = int( input( '>> ? ' ) )
        if iChoise < 1 or iChoise > len( oOthersChoices ):
            raise()
        sInPair = oOthersChoices[ iChoise - 1 ]

    except Exception as e:
        print( "Paire introuvable" )
        exit()

# kisstomato-script-section-controle-stop-user-code-kisstomato

"""
Contrôle la présence des données d'historiques
"""
print( "\n>> CONTRÔLE LA PRÉSENCE DES DONNÉES D'HISTORIQUES\n" )
# kisstomato-script-section-collection-exist-start-user-code-kisstomato

# determine si la collection existe
cColName = gl.config[ "mongo" ][ "cols" ][ "history_pair" ].replace( "{pair}", sInPair.lower() )
if not bdd.collectionExist( cColName ):
    print( "Collection introuvable" )
    exit()

# kisstomato-script-section-collection-exist-stop-user-code-kisstomato

"""
Construction des images d'entrées
"""
print( "\n>> CONSTRUCTION DES IMAGES D'ENTRÉES\n" )
# kisstomato-script-section-create-image-start-user-code-kisstomato

if input( 'Construction des images d\'enttrées (O/n) ? ' ).lower() in [ '', 'o' ]:
    datasets.init( sInPair.lower() )
    datasets.create( sInPair.lower() )

# kisstomato-script-section-create-image-stop-user-code-kisstomato

# kisstomato-script-end-start-user-code-kisstomato
# kisstomato-script-end-stop-user-code-kisstomato