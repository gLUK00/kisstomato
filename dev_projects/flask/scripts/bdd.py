# coding=utf-8
import argparse

# kisstomato-script-import-start-user-code-kisstomato
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules import configuration, bdd
# kisstomato-script-import-stop-user-code-kisstomato

"""
Traitements relatifs à la base de données
"""

# kisstomato-script-init-start-user-code-kisstomato
configuration.load()
# kisstomato-script-init-stop-user-code-kisstomato

print( "Traitements relatifs à la base de données" )

"""
Exportation de collections
"""
print( "\n>> EXPORTATION DE COLLECTIONS\n" )
# kisstomato-script-section-export-start-user-code-kisstomato

if input( 'Confirmez vous l\'exportation de collection (O/n) ? ' ).lower() in [ '', 'o' ]:

    # recupere les collections
    oCol = bdd.getBdd().list_collection_names()
    sQuery = "Quelle collection souhaitez-vous exporter ?"
    for sCol in oCol:
        sQuery += "\n- " + sCol
    sQuery += "\n- *, toutes les collections\n? "
    sColName = input( sQuery )
    if sColName not in oCol and sColName != "*":
        print( "Collection introuvable" )
        exit()
    
    # exporte les collections
    if sColName == "*":
        for sCol in oCol:
            bdd.exportCollection( sCol )
    else:
        bdd.exportCollection( sColName )

# kisstomato-script-section-export-stop-user-code-kisstomato
"""
Importation d'une collection
"""
print( "\n>> IMPORTATION D'UNE COLLECTION\n" )
# kisstomato-script-section-import-start-user-code-kisstomato

if input( 'Confirmez vous l\'importation de collection (O/n) ? ' ).lower() in [ '', 'o' ]:

    # recupere les collections
    oCol = bdd.getBdd().list_collection_names()
    sQuery = "Quelle collection souhaitez-vous importer ?"
    for sCol in oCol:
        sQuery += "\n- " + sCol
    sColName = input( sQuery + "\n? " )
    if sColName not in oCol:
        print( "Collection introuvable" )
        exit()
    
    # importe la collection
    bdd.importCollection( sColName )

# kisstomato-script-section-import-stop-user-code-kisstomato
# kisstomato-script-end-start-user-code-kisstomato
# kisstomato-script-end-stop-user-code-kisstomato