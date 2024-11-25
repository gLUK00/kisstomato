import json, os, sys, shutil

from jinja2 import Environment, PackageLoader, select_autoescape, BaseLoader, FileSystemLoader

# importation du CORE
from core import generator

# referencement du repertoire parent
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from python_flask.classes import *

#from ..python_flask.classes import *
#from python_flask.classes import *
#from .classes import *
# ImportError: attempted relative import with no known parent package

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

# generation du code Flask
def generateFlaskCode2( oData ):
    sRapport = 'Le rapport de génération 2\n\n'
    try:

        # supprime et creer le repertoire temporaire
        sDirTemp = oData[ 'dir-temp' ]
        if os.path.isdir( sDirTemp ):
            shutil.rmtree( sDirTemp )
        os.makedirs( sDirTemp, mode = 0o777 )

        # creation du repertoire de sortie, si inexistant

        # todo : copie des fichiers de bases
        # les assets de kisstomato : bootstrap, fontawesome, jquery


        # merge le repertoire temporaire avec la sortie
        # pour requirements.txt faire une fusion

        sRapport += ''

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("------ ERROR ------")
        print(str( e ))
        print((exc_type, fname, exc_tb.tb_lineno))

    return sRapport

# generation d'un fichier
def _genFileFromTmpl( oNode, sFileTmpl, FileOut, cClass ):
    sPathPlugin = os.path.dirname( os.path.abspath(__file__) )

    sPathTemplate = ''
    if sFileTmpl.find( os.sep ) != -1:
        sPathTemplate = os.sep + sFileTmpl[ : sFileTmpl.find( os.sep ) - 1 ]
    env = Environment( loader=FileSystemLoader( sPathPlugin + os.sep + 'templates' + sPathTemplate ) )

    template = env.get_template( sFileTmpl )
    sGenCode = template.render( o=cClass(oNode) )

    with open( FileOut, "w", encoding="utf-8" ) as oFile:
        oFile.write( sGenCode )

# generation du code Flask
def generateFlaskCode( oData ):
    sPathPlugin = os.path.dirname( os.path.abspath(__file__) )
    sRapport = 'Le rapport de génération\n\n'
    try:

        # si les parametres doivent etre sauvegardes
        if "save-params" in oData and oData[ "save-params" ]:

            print( 'enregistrement des parametres' )

        # supprime et creer le repertoire temporaire
        sDirTemp = oData[ 'dir-temp' ]
        if os.path.isdir( sDirTemp ):
            shutil.rmtree( sDirTemp )
        os.makedirs( sDirTemp, mode = 0o777 )

        # si le repertoire de sortie n'existe pas
        sDirOut = oData[ 'dir-out' ]
        if not os.path.isdir( sDirOut ):
            os.makedirs( sDirOut, mode = 0o777 )

        # copie des fichiers de bases
        # les assets de kisstomato : bootstrap, fontawesome, jquery
        generator.mergeDirs( sPathPlugin + os.sep + 'templates' + os.sep + 'base', sDirTemp )
        #shutil.copytree( sPathPlugin + os.sep + 'templates' + os.sep + 'base', sDirTemp )

        sRapport += 'enerator.mergeDirs( ' + sPathPlugin + os.sep + 'templates' + os.sep + 'base' + ', ' + sDirTemp + ' )\n'

        #env = Environment(loader=BaseLoader)
        
        env = Environment( loader=FileSystemLoader( sPathPlugin + os.sep + 'templates' + os.sep + 'html' ) )

        #print( sDirTemp )
        #print( env )

        # recuperation du projet
        oProject = None
        with open( oData[ 'file' ], 'r' ) as j:
            oProject = json.loads(j.read())

        def fCreate( oNodes, sPath ):
            sResult = ''
            if not 'children' in oNodes or len( oNodes[ 'children' ] ) == 0:
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

                if oNode[ 'li_attr' ][ 'type' ] == 'script':

                    _genFileFromTmpl( oNode, 'script.py', sPath + os.sep + 'scripts' + os.sep + oNode[ 'text' ] + '.py', nodeScript )

                    continue

                if oNode[ 'li_attr' ][ 'type' ] != 'directory':
                    continue

                # creation du repertoire
                sDirCreate = sPath + os.sep + oNode[ 'text' ]
                sResult += 'creation rep : ' + sDirCreate + '\n'
                os.makedirs( sDirCreate, mode = 0o777 )

                # si il y a des sous elements
                if 'children' in oNode and len( oNode[ 'children' ] ) > 0:
                    sResult += fCreate( oNode, sDirCreate )

            return sResult

        #print( 'rrrrrrrrrrrrrrrrr' )
        #print( type( oProject[ 'data' ] ) )

        # pour tous les scripts
        oScripts = generator.getNodeById( 'scripts', oProject[ 'data' ] )
        if oScripts and len( oScripts[ 'children' ] ) > 0:

            # creation des scripts
            for oScript in oScripts[ 'children' ]:

                _genFileFromTmpl( oScript, 'script.py', sDirTemp + os.sep + 'scripts' + os.sep + oScript[ 'text' ] + '.py', nodeScript )

        # recupere le noeud "Pages"
        oPages = generator.getNodeById( 'pages', oProject[ 'data' ] )
        if oPages:

            # creation des pages
            sRapport += 'Creation temporaire :\n' + fCreate( oPages, sDirTemp ) + '\n\n'

        

        # merge avec le repertoire cible
        sRapport += 'Fusion avec l\'existant :\n' + generator.mergeDirs( sDirTemp, sDirOut,
            {
                'html': { 'start': '<!-- kisstomato-', 'stop': ' -->' },
                './requirements.txt': { 'start': '# kisstomato-', 'stop': '-kisstomato' }
            }
        )

        # merge des fichiers particuliers
        #generator.mergeFiles( sDirTemp + os.sep + 'requirements.txt', sDirOut + os.sep + 'requirements.txt',
        #    { 'start': '# kisstomato-', 'stop': '-kisstomato' } )

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("------ ERROR ------")
        print(str( e ))
        print((exc_type, fname, exc_tb.tb_lineno))

    return sRapport