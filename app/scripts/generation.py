import sys, os, json

# referencement du repertoire parent
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# importation du CORE
from core import plugin

# gestion des erreurs
def showError( sMessage ):
	print( sMessage + '\n' )
	print( 'python generation.py [CHEMIN DU PROJET.json] [MODULE DE GENERATION] [METHODE DE GENERATION]\n' )
	print( 'Exemple : python generation.py /home/myname/myprojectflask/kisstomato.json generation generateFlaskCode' )
	exit( -1 )

# recupere le nom du fichier Json du projet
if len( sys.argv ) < 4:
	showError( 'Les nombres d\'arguments n\'est pas correct' )
sFileProject = sys.argv[ 1 ]
if not os.path.isfile( sFileProject ):
	showError( 'Le fichier du projet est introuvable : ' + sFileProject )

# lecture du projet
oProject = {}
with open( sFileProject, 'r', encoding="utf-8" ) as j:
    oProject = json.loads(j.read())

# determine l'existance du plugin
sPathPlugin = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) + os.sep + 'plugins' + os.sep + 'models' + os.sep + oProject[ 'model' ]
if not os.path.isdir( sPathPlugin ):
	showError( 'Le plugin est introuvable : ' + oProject[ 'model' ] + '\n' + 'Depuis le répertoire suivant : ' + sPathPlugin )

# determine l'existance du module
sPathModule = sPathPlugin + os.sep + sys.argv[ 2 ] + '.py'
if not os.path.isfile( sPathModule ):
	showError( 'Le module est introuvable : ' + sys.argv[ 2 ] + '\n' + 'Depuis le fichier suivant : ' + sPathModule )

# si il y a des donnees
oData = {}
if len( sys.argv ) > 4:
	oData = json.loads( sys.argv[ 4 ].replace( "'", '"' ) )

# execution du plugin
sResult = plugin.exeMethodModel( oProject[ 'model' ], sys.argv[ 2 ], sys.argv[ 3 ], oData )

print( sResult )


"""

"""
