import os, glob

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

    # recupere l'ensemble des fichiers et repertoires de la source
    oAllSrc = glob.glob( sDirSource + os.sep + '**' )

    print( sDirSource )
    print( sDirTarget )
    print( oConfig )
    print( oAllSrc )

    return 'in mergeDirs'