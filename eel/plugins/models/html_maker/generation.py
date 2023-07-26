import json, os, sys, shutil

# importation du CORE
from core import generator

# generation du code HTML
def generateHtmlCode( oData ):
    sRapport = 'Le rapport de génération\n\n'
    try:

        # supprime et creer le repertoire temporaire
        sDirTemp = oData[ 'dir-temp' ]
        if os.path.isdir( sDirTemp ):
            shutil.rmtree( sDirTemp )
        os.makedirs( sDirTemp, mode = 0o777 )

        # todo : copie des fichiers de bases

        print( sDirTemp )

        # recuperation du projet
        oProject = None
        with open( oData[ 'file' ], 'r' ) as j:
            oProject = json.loads(j.read())

        def fCreate( oNodes, sPath ):
            sResult = ''
            if 'children' in oNodes and len( oNodes[ 'children' ] ) == 0:
                return
            for oNode in oNodes[ 'children' ]:
                if oNode[ 'li_attr' ][ 'type' ] == 'page':

                    # creation d'un page
                    sPageHtml = sPath + os.sep + oNode[ 'text' ] + '.html'
                    sResult += 'creation page : ' + sPageHtml + '\n'
                    continue

                if oNode[ 'li_attr' ][ 'type' ] != 'directory':
                    continue

                # creation du repertoire
                sDirCreate = sPath + os.sep + oNode[ 'text' ]
                sResult += 'creation rep : ' + sDirCreate + '\n'
                os.makedirs( sDirCreate, mode = 0o777 )

                # si il y a des sous repertoire
                if 'children' in oNode and len( oNode[ 'children' ] ) > 0:
                    sResult += fCreate( oNode, sDirCreate )

            return sResult

        #print( 'rrrrrrrrrrrrrrrrr' )
        #print( type( oProject[ 'data' ] ) )

        # recupere le noeud "Pages"
        oPages = generator.getNodeById( 'pages', oProject[ 'data' ] )

        # creation des repertoires
        sRapport += 'Creation temporaire :\n' + fCreate( oPages, sDirTemp )


        #print( oProject )
        #print( oPages )

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("------ ERROR ------")
        print(str( e ))
        print((exc_type, fname, exc_tb.tb_lineno))

    return sRapport


"""
{dir-src: '', dir-out: '', save-params: false, file: '/home/hidalgo/Documents/projects/kisstomato/eel/../example/kisstomato.json'}
dir-out
: 
""
dir-src
: 
""
file
: 
"/home/hidalgo/Documents/projects/kisstomato/eel/../example/kisstomato.json"
save-params
: 
false
"""