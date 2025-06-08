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
        
        # creation des repertoires de base
        oBaseDirs = [ 'classes', 'js', 'templates' ];
        for sDir in oBaseDirs:
            if not os.path.isdir( sDirTemp + os.sep + sDir ):
                os.makedirs( sDirTemp + os.sep + sDir, mode = 0o777 )

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

        # pour tous les modules
        sRapport += 'Generation des modules :\n<ul>'
        for oModule in generator.getNodesByTypes( oProject[ 'data' ], 'modules/module' ):
            sRapport += '<li>' + oModule[ 'text' ] + '</li>'
            generator.genFileFromTmpl( sPathPlugin, oModule, 'module.py', sDirTemp + os.sep + oModule[ 'text' ] + '.py', module )
        sRapport += '</ul>'

        # pour toutes les classes
        sRapport += 'Generation des classes :\n<ul>'
        for oClasse in generator.getNodesByTypes( oProject[ 'data' ], 'classes/classe' ):
            sRapport += '<li>' + oClasse[ 'text' ] + '</li>'
            generator.genFileFromTmpl( sPathPlugin, oClasse, 'classe.py', sDirTemp + os.sep + 'classes' + os.sep + oClasse[ 'text' ] + '.py', tmpClasse )
        sRapport += '</ul>'

        # pour le fichier __init__.py
        sRapport += 'Generation du fichier classes/__init__.py\n'
        generator.genFileFromTmpl( sPathPlugin, oProject, 'classe__init__.py', sDirTemp + os.sep + 'classes' + os.sep + '__init__.py', initClasse )

        # pour tous les fichiers javascript
        sRapport += 'Generation des javascripts :\n<ul>'
        for oJS in generator.getNodesByTypes( oProject[ 'data' ], 'javascripts/javascript' ):
            sRapport += '<li>' + oJS[ 'text' ] + '</li>\n'
            generator.genFileFromTmpl( sPathPlugin, oJS, 'javascript.js', sDirTemp + os.sep + 'js' + os.sep + oJS[ 'text' ] + '.js', javascript )
        sRapport += '</ul>\n'

        # pour tous les templates
        def genTmplInDir( oNode, sDirParent='' ):
            oEFiles = []
            sType = oNode[ 'id' ] if 'type' not in oNode[ 'li_attr' ] else oNode[ 'li_attr' ][ 'type' ]

            # pour tous les templates
            for oTempl in generator.getNodesByTypes( oNode, sType + '/template' ):
                open( sDirParent + os.sep + oTempl[ 'text' ], 'a' ).close()
                oEFiles.append( sDirParent + os.sep + oTempl[ 'text' ] )

            # pour tous les dossiers
            for oDir in generator.getNodesByTypes( oNode, sType + '/directory_tmpl' ):

                # creation du repertoire
                if not os.path.isdir( sDirParent + os.sep + oDir[ 'text' ] ):
                    os.makedirs( sDirParent + os.sep + oDir[ 'text' ], mode = 0o777 )

                # recherche recurcive
                oEFiles += genTmplInDir( oDir, sDirParent + os.sep + oDir[ 'text' ] )
            return oEFiles

        # liste des fichiers a exclures
        oExcludeFiles = genTmplInDir( generator.getNodeById( 'templates', oProject[ 'data' ] ), sDirTemp + os.sep + 'templates' )


        """"

        
            
"""

        # pour tous les scripts
        """oScripts = generator.getNodeById( 'scripts', oProject[ 'data' ] )
        if oScripts and len( oScripts[ 'children' ] ) > 0:

            # creation des scripts
            for oScript in oScripts[ 'children' ]:

                generator.genFileFromTmpl( sPathPlugin, oScript, 'script.py', sDirTemp + os.sep + 'scripts' + os.sep + oScript[ 'text' ] + '.py', nodeScript )
        """

        # merge avec le repertoire cible
        sRapport += 'Fusion avec l\'existant :\n' + generator.mergeDirs( sDirTemp, sDirOut,
            oConfig={
                'html': { 'start': '<!-- kisstomato-', 'stop': ' -->' },
                'js': { 'start': '// kisstomato-', 'stop': '-kisstomato' },
                'py': { 'start': '# kisstomato-', 'stop': '-kisstomato' },
                'sh': { 'start': '# kisstomato-', 'stop': '-kisstomato' },
                './requirements.txt': { 'start': '# kisstomato-', 'stop': '-kisstomato' }
            },
            oExcludeFiles=oExcludeFiles
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