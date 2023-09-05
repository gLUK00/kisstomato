import os, glob, shutil

from pathlib import Path

# recupere les informations des projets
def getNodeById( sId, oNode ):

    if isinstance( oNode, list ):
        for oChild in oNode:
            oChildSearch = getNodeById( sId, oChild )
            if oChildSearch != None:
                return oChildSearch
        return None

    if oNode[ 'id' ] == sId:
        return oNode
    if oNode[ 'children' ] != None and len( oNode[ 'children' ] ) > 0:
        oChildSearch = getNodeById( sId, oNode[ 'children' ] )
        if oChildSearch != None:
            return oChildSearch

    return None

# merge de repertoire
def mergeDirs( sDirSource, sDirTarget, oConfig=None ):
    sRapport = ''

    # recupere l'ensemble des fichiers et repertoires source et cible
    oAllSrc = glob.glob( sDirSource + os.sep + '**', recursive=True )
    oAllTar = glob.glob( sDirTarget + os.sep + '**', recursive=True )

    # pour tous les elements sources
    for sElement in oAllSrc:

        # deduction du nom cible
        sElementTarget = sDirTarget + sElement[ len( sDirSource ) : ]

        # si c'est un repertoire et qu'il n'est pas present en cible
        if os.path.isdir( sElement ):

            # le repertoire existe deja en cible
            if sElementTarget in oAllTar:
                continue

            sRapport += 'Creation du repertoire : ' + sElementTarget + '\n'
            os.makedirs( sElementTarget, mode = 0o777 )
            continue

        # determine l'extension du fichier
        sExt = ''
        iPosPoint = sElement.rfind( '.' )
        if iPosPoint != -1:
            sExt = sElement[ iPosPoint + 1 : ].lower()

        # si le fichier n'existe pas en cible ou n'est pas a prendre en compte dans la configuration
        if not sElementTarget in oAllTar or oConfig == None or not sExt in oConfig.keys():

            # copie du fichier
            sRapport += 'Copie du fichier : ' + sElementTarget + '\n'
            shutil.copyfile( sElement, sElementTarget )
            continue
        
        # recuperation du contenu source et cible
        sContentSrc = Path( sElement ).read_text()
        sContentTar = Path( sElementTarget ).read_text()

        print( 'ext' )
        print( sExt )
        print( sContentSrc )
        print( sContentTar )



    print( sDirSource )
    print( sDirTarget )
    print( oConfig )
    #print( oAllSrc )
    #print( oAllTar )

    return sRapport