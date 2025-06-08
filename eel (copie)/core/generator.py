import os, glob, shutil, sys
from jinja2 import Environment, FileSystemLoader

from pathlib import Path

# recupere une propriete d'un projet
def getPropertyById( sId, oProject ):
    if not 'properties' in oProject:
        return None
    for sKey in oProject[ 'properties' ]:
        if sKey == sId:
            return oProject[ 'properties' ][ sKey ]
    return None

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
    if 'children' in oNode and len( oNode[ 'children' ] ) > 0:
        oChildSearch = getNodeById( sId, oNode[ 'children' ] )
        if oChildSearch != None:
            return oChildSearch

    return None

# recupere une liste de node en fonction du type
def getNodesByTypes( oNodes, sTypes ):
    if not type( oNodes ) is list:
        oNodes = [ oNodes ]

    oTypes = sTypes.split( '/' )
    #if not 'children' in oNode:
    #    return []
    #oNodes = oNode[ 'children' ]

    oResults = []
    

    #if len( oTypes ) == 1:
    #oNodes = oNode

    for sType in oTypes:

        # si c'est le derniers noeud
        if len( oTypes ) == 1:
            for oNode in oNodes:
                if oNode[ 'li_attr' ][ 'type' ] == sType:
                    oResults += [ oNode ]
            return oResults
        
        for oNode in oNodes:
            if ( ( 'type' not in oNode[ 'li_attr' ] and oNode[ 'id' ] == sType ) or ( 'type' in oNode[ 'li_attr' ] and oNode[ 'li_attr' ][ 'type' ] == sType ) ) and 'children' in oNode:
                oResults += oNode[ 'children' ]
        
        if len( oResults ) == 0:
            return []

        return getNodesByTypes( oResults, '/'.join( oTypes[ 1 : ] ) )

    return oResults


# merge de fichiers
def mergeFiles( sFileSource, sFileTarget, oTags ):
    sRapport = ''

    # recuperation du contenu source et cible
    sContentSrc = Path( sFileSource ).read_text()
    sContentTar = Path( sFileTarget ).read_text()

    # determine les sections de la source
    oSectionSrc = {}
    sTagStart = oTags[ 'start' ]
    sTagStop = oTags[ 'stop' ]
    iPosStart = sContentSrc.find( sTagStart )
    while iPosStart != -1:
        iPosStop = sContentSrc.find( sTagStop, iPosStart )

        # determine le nom de la section
        sSection = sContentSrc[ iPosStart + len( sTagStart ) : iPosStop ].replace( '-start-user-code', '' ).strip()

        # determine les positions de la portion
        sTagSectionEnd = sTagStart + sSection + '-stop-user-code' + sTagStop
        iPosPortionStart = iPosStop + len( sTagStop )
        iPosPortionStop = sContentSrc.find( sTagSectionEnd, iPosPortionStart )
        if iPosPortionStop == -1:
            sRapport += 'Erreur de merge sur recherche de position de fin dans source : [' + sTagSectionEnd + '] à partir de ' + str( iPosPortionStart ) +  '\n'
            return sRapport

        # recupere la section
        oSectionSrc[ sSection ] = { 'start': iPosPortionStart, 'stop': iPosPortionStop }

        # determine si il y a une autre occurence
        iPosStart = sContentSrc.find( sTagStart, iPosPortionStop + len( sTagSectionEnd ) )

    # determine les sections et le contenu de la cible
    oContentTarget = {}
    iPosStart = sContentTar.find( sTagStart )
    while iPosStart != -1:
        iPosStop = sContentTar.find( sTagStop, iPosStart )

        # determine le nom de la section
        sSection = sContentTar[ iPosStart + len( sTagStart ) : iPosStop ].replace( '-start-user-code', '' ).strip()

        # determine les positions de la portion
        sTagSectionEnd = sTagStart + sSection + '-stop-user-code' + sTagStop
        iPosPortionStart = iPosStop + len( sTagStop )
        iPosPortionStop = sContentTar.find( sTagSectionEnd, iPosPortionStart )
        if iPosPortionStop == -1:
            sRapport += 'Erreur de merge sur recherche de position de fin dans cible : [' + sTagSectionEnd + '] à partir de ' + str( iPosPortionStart ) +  '\n'
            return sRapport

        # recupere la section
        oContentTarget[ sSection ] = { 'content': sContentTar[ iPosPortionStart : iPosPortionStop ] }

        # determine si il y a une autre occurence
        iPosStart = sContentTar.find( sTagStart, iPosPortionStop + len( sTagSectionEnd ) )

    # tri les sections de la source pour mettre la plus lointaine au debut du traitement
    oNewSectionSrc = {}
    iPosMax = -1
    while len( oNewSectionSrc ) != len( oSectionSrc ):
        sSectionImport = ''
        for sKey in oSectionSrc.keys():
            if sKey in oNewSectionSrc:
                continue
            if oSectionSrc[ sKey ][ 'start' ] > iPosMax:
                iPosMax = oSectionSrc[ sKey ][ 'start' ]
                sSectionImport = sKey

        # recupere la section la plus lointaine
        oNewSectionSrc[ sSectionImport ] = oSectionSrc[ sSectionImport ]
        iPosMax = -1

    oSectionSrc = oNewSectionSrc

    # pour toutes les sources
    for sSection in oSectionSrc:
        if not sSection in oContentTarget:
            continue

        # insertion du code
        sContentSrc = sContentSrc[ : oSectionSrc[ sSection ][ 'start' ] ] + oContentTarget[ sSection ][ 'content' ] + sContentSrc[ oSectionSrc[ sSection ][ 'stop' ] : ]

    # reecriture de la cible
    Path( sFileTarget ).write_text( sContentSrc )


# merge de repertoires
def mergeDirs( sDirSource, sDirTarget, oConfig=None, oExcludeFiles=None ):
    sRapport = ''
    try:

        # recupere l'ensemble des fichiers et repertoires source et cible
        oAllSrc = glob.glob( sDirSource + os.sep + '**', recursive=True )
        oAllTar = glob.glob( sDirTarget + os.sep + '**', recursive=True )

        # pour tous les elements sources
        for sElement in oAllSrc:

            # deduction du nom cible
            sPathNameElement = sElement[ len( sDirSource ) : ]
            sElementTarget = sDirTarget + sPathNameElement

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
            if not sElementTarget in oAllTar or oConfig == None or ( not sExt in oConfig.keys() and not '.' + sPathNameElement in oConfig.keys() ):

                # copie du fichier
                #sRapport += 'Copie du fichier : ' + sElementTarget + '\n'
                shutil.copyfile( sElement, sElementTarget )
                continue

            # determine si le fichier doit etre exclus
            if oExcludeFiles and sElement in oExcludeFiles:
                sRapport += 'Exclusion du fichier : ' + sPathNameElement + '\n'
                continue

            sRapport += 'Merge des fichiers : ' + sPathNameElement + ' et ' + sElementTarget + '\n'
            oConfigMerge = {}
            if '.' + sPathNameElement in oConfig.keys():
                oConfigMerge = oConfig[ '.' + sPathNameElement ]
            else:
                oConfigMerge = oConfig[ sExt ]
            mergeFiles( sElement, sElementTarget, oConfigMerge )

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("------ ERROR mergeDirs ------")
        print(str( e ))
        print((exc_type, fname, exc_tb.tb_lineno))

    return sRapport

# generation d'un fichier d'un plugin
def genFileFromTmpl( sPathPlugin, oNode, sFileTmpl, FileOut, cClass ):
    try:

        sPathTemplate = ''
        if sFileTmpl.find( os.sep ) != -1:
            sPathTemplate = os.sep + sFileTmpl[ : sFileTmpl.find( os.sep ) - 1 ]
        env = Environment( loader=FileSystemLoader( sPathPlugin + os.sep + 'templates' + sPathTemplate ), line_statement_prefix='&&' )

        template = env.get_template( sFileTmpl )
        sGenCode = template.render( o=cClass(oNode) )

        os.makedirs( os.path.dirname( FileOut ), exist_ok=True )
        with open( FileOut, "w", encoding="utf-8" ) as oFile:
            oFile.write( sGenCode )
        
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("------ ERROR genFileFromTmpl ------")
        print(str( e ))
        print((exc_type, fname, exc_tb.tb_lineno))
        
        raise 'genFileFromTmpl : ' + str(e) + ' : ' + str(exc_type) + ' : ' + str(fname) + ' : ' + str(exc_tb.tb_lineno)