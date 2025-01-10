import json, os, sys, shutil

from jinja2 import Environment, FileSystemLoader

# importation du CORE
from core import generator

# referencement du repertoire parent
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from kisstomato_model.classes import *

# generation du code
def generateKisstomatoCode( oData ):
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

        # recuperation du projet
        oProject = None
        with open( oData[ 'file' ], 'r' ) as j:
            oProject = json.loads(j.read())

        # pour le fichier model.py
        sRapport += 'Generation du fichier model.py\n'
        generator.genFileFromTmpl( sPathPlugin, oProject, 'model.py', sDirTemp + os.sep + 'model.py', model )

        # pour le fichier configuration.json
        sRapport += 'Generation du fichier configuration.json\n'
        generator.genFileFromTmpl( sPathPlugin, oProject, 'configuration.json', sDirTemp + os.sep + 'configuration.json', configJson )


        """"properties": [
		{ "id": "impl-getJsonCreateNewProject", "text": "Implémentation de la méthode getJsonCreateNewProject", "type": "switch" },
		{ "id": "impl-openProject", "text": "Implémentation de la méthode openProject", "type": "switch" }
	]"""

        # pour tous les scripts
        """oScripts = generator.getNodeById( 'scripts', oProject[ 'data' ] )
        if oScripts and len( oScripts[ 'children' ] ) > 0:

            # creation des scripts
            for oScript in oScripts[ 'children' ]:

                generator.genFileFromTmpl( sPathPlugin, oScript, 'script.py', sDirTemp + os.sep + 'scripts' + os.sep + oScript[ 'text' ] + '.py', nodeScript )
        """

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
        sRapport += '\nError : ' + str( e ) + '\n' + str(exc_type) + ' : ' + str(fname) + ' : ' + str(exc_tb.tb_lineno)

    return sRapport