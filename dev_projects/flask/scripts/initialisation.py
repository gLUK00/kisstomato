# coding=utf-8
import argparse

# kisstomato-script-import-start-user-code-kisstomato
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import gl
from modules import configuration, bdd, cache, services
# kisstomato-script-import-stop-user-code-kisstomato

"""
script d'initialisation :
- création et mise à jour de la BDD,
- vérification des connexions.
"""

# kisstomato-script-init-start-user-code-kisstomato
configuration.load()
# kisstomato-script-init-stop-user-code-kisstomato

print( "script d'initialisation :\n- création et mise à jour de la BDD,\n- vérification des connexions." )

# Création de la base de données
# Argument :
# - conf : string : (obligatoire) configuration de la BDD
def initBdd(conf):
    oResult = None

    # kisstomato-methode-initBdd-start-user-code-kisstomato
    oBdd = bdd.getBdd()
    # kisstomato-methode-initBdd-stop-user-code-kisstomato

    return oResult

"""
Initialisation de la base de données
"""
print( "\n>> INITIALISATION DE LA BASE DE DONNÉES\n" )
# kisstomato-script-section-initBdd-start-user-code-kisstomato
oBdd = initBdd( gl.config[ "mongo" ] )

if input( 'Initialisation de la BDD (O/n) ? ' ).lower() in [ '', 'o' ]:

    print( 'rrrrrrrrrrrrr' )

# kisstomato-script-section-initBdd-stop-user-code-kisstomato

"""
Initialisation du cache
"""
print( "\n>> INITIALISATION DU CACHE\n" )
# kisstomato-script-section-cache-start-user-code-kisstomato

if input( 'Initialisation du cache (O/n) ? ' ).lower() in [ '', 'o' ]:
    cache.initCache( gl.config[ "paths" ][ "cache" ] )

# kisstomato-script-section-cache-stop-user-code-kisstomato

"""
recuperation des paires
"""
print( "\n>> RECUPERATION DES PAIRES\n" )
# kisstomato-script-section-recuperation-paires-start-user-code-kisstomato

if input( 'Récupèration des paires (O/n) ? ' ).lower() in [ '', 'o' ]:
    services.getPairs()

# kisstomato-script-section-recuperation-paires-stop-user-code-kisstomato

# kisstomato-script-end-start-user-code-kisstomato
# kisstomato-script-end-stop-user-code-kisstomato