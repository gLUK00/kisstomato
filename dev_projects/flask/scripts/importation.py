# coding=utf-8
import argparse

# kisstomato-script-import-start-user-code-kisstomato
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import gl
from modules import configuration, bdd, cache, services
# kisstomato-script-import-stop-user-code-kisstomato

"""
Batch d'importation de l'historique des transactions
"""

# kisstomato-script-init-start-user-code-kisstomato
configuration.load()
# kisstomato-script-init-stop-user-code-kisstomato

print( "Batch d'importation de l'historique des transactions" )

# recuperation des arguments
oParser = argparse.ArgumentParser( prog="importation", description="Batch d'importation de l'historique des transactions" )

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
Procédure d'importation
"""
print( "\n>> PROCÉDURE D'IMPORTATION\n" )
# kisstomato-script-section-importation-start-user-code-kisstomato

if input( 'Confirmez vous l\'importation de ' + sInPair.upper() + ' (O/n) ? ' ).lower() in [ '', 'o' ]:

    # recuperation de l'historique des trades
    services.getTradesFiles( sInPair )

# kisstomato-script-section-importation-stop-user-code-kisstomato
"""
Enregistrement en BDD
"""
print( "\n>> ENREGISTREMENT EN BDD\n" )
# kisstomato-script-section-enregistrement-start-user-code-kisstomato

cColName = gl.config[ "mongo" ][ "cols" ][ "history_pair" ].replace( "{pair}", sInPair.lower() )
if input( 'Confirmez vous la création de la collection ' + cColName + ' (O/n) ? ' ).lower() in [ '', 'o' ]:

    bdd.dropCollection( cColName, createIndex='time' )
    bdd.importHistory( cColName, sInPair, cache.getAllFiles( 'trades_' + sInPair  ) )

# kisstomato-script-section-enregistrement-stop-user-code-kisstomato
# kisstomato-script-end-start-user-code-kisstomato
# kisstomato-script-end-stop-user-code-kisstomato