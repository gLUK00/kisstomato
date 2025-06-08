import os, sys, argparse

# commentaire de demarrage
print( "Batch d'importation de l'historique des transactions" )

# kisstomato-imports-start-user-code-kisstomato
# kisstomato-imports-stop-user-code-kisstomato

oParser = argparse.ArgumentParser( prog="importation", description="Batch d'importation de l'historique des transactions" )
oParser.add_argument( "--pair", required=True )
oArgs = oParser.parse_args()


print( oArgs )

# kisstomato-main-start-user-code-kisstomato
# kisstomato-main-stop-user-code-kisstomato