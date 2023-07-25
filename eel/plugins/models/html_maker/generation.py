import json

# importation du CORE
from core import generator

# generation du code HTML
def generateHtmlCode( oData ):
    sRapport = 'Le rapport de génération'

    # recuperation du projet
    oProject = None
    with open( oData[ 'file' ], 'r' ) as j:
        oProject = json.loads(j.read())

    # lecture recursive d'un noeud
    def fReadNode( oNode, oParent, fValidNode ):
        oResults = []



        return oResults

    print( 'rrrrrrrrrrrrrrrrr' )
    print( type( oProject[ 'data' ] ) )

    # pour tous les noeuds
    oPages = generator.getNodeById( 'pages', oProject[ 'data' ] )




    print( oProject )
    print( oPages )

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