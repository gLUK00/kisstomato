import json, os, sys, shutil

from jinja2 import Environment, PackageLoader, select_autoescape, BaseLoader, FileSystemLoader

# importation du CORE
from core import generator

# classe de generation des pages HTML
class GenHTML:
    def __init__(self, oNode):
        self.node = oNode

        # map les items
        self.values = {}
        for oItem in oNode[ 'li_attr' ][ 'items' ]:
            self.values[ oItem[ 'id' ] ] = oItem[ 'value' ]

    def getTitle(self):

        return self.values[ 'title' ]

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
        # les assets de kisstomato : bootstrap, fontawesome, jquery

        #env = Environment(loader=BaseLoader)
        sPathPlugin = os.path.dirname( os.path.abspath(__file__) )
        env = Environment( loader=FileSystemLoader( sPathPlugin + os.sep + 'templates' ) )

        #print( sDirTemp )
        #print( env )

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

                    # determine le nom du fichier cible
                    sTargetHtml = sPath + os.sep + oNode[ 'text' ] + '.html'

                    # creation d'une page
                    sPageHtml = sPath + os.sep + oNode[ 'text' ] + '.html'
                    sResult += 'creation page : ' + sPageHtml + '\n'

                    #rtemplate = Environment(loader=BaseLoader).from_file(sPageHtml)
                    #rtemplate = Environment(loader=BaseLoader).from_string(myString)
                    template = env.get_template("page.html")
                    sCodeHtml = template.render( page=GenHTML(oNode) )

                    with open( sPageHtml, "w", encoding="utf-8" ) as oFile:
                        oFile.write( sCodeHtml )

                    #print( sCodeHtml )
                    #print( sTargetHtml )

                    #template = env.get_template( sPageHtml )

                    #print( template )

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

        # creation des pages
        sRapport += 'Creation temporaire :\n' + fCreate( oPages, sDirTemp ) + '\n\n'

        # deplacement des assets
        sRapport += 'Copie des assets :\n' + generator.mergeDirs( sPathPlugin + os.sep + 'assets', sDirTemp )

        # merge avec le repertoire cible
        sRapport += 'Fusion avec l\'existant :\n' + generator.mergeDirs( sDirTemp, oData[ 'dir-out' ], { 'html': { 'start': '<!-- kisstomato-', 'stop': ' -->' } } )


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