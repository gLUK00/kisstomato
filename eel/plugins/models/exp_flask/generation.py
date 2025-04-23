# kisstomato-module-a-start-user-code-kisstomato
# kisstomato-module-a-stop-user-code-kisstomato

import json, os, sys, shutil

from core import generator

# referencement du repertoire parent
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)

from classes import *

# kisstomato-module-b-start-user-code-kisstomato
from helpers import io
# kisstomato-module-b-stop-user-code-kisstomato

# Génération du code

# Génération de l'application Flask
# Argument :
# - data : object : (obligatoire) Données du formulaire JS
def generateFlaskCode(data):
    oResult = None

    # kisstomato-fonction-generateFlaskCode-init-start-user-code-kisstomato
    sPathPlugin = os.path.dirname( os.path.abspath(__file__) )
    oResult = 'Le rapport de génération\n\n'
    # kisstomato-fonction-generateFlaskCode-init-stop-user-code-kisstomato

    try:
        # kisstomato-fonction-generateFlaskCode-try-start-user-code-kisstomato
        
        # si les parametres doivent etre sauvegardes
        if "save-params" in data and data[ "save-params" ]:

            print( 'enregistrement des parametres' )

        # supprime et creer le repertoire temporaire
        sDirTemp = data[ 'dir-temp' ]
        if os.path.isdir( sDirTemp ):
            shutil.rmtree( sDirTemp )
        os.makedirs( sDirTemp, mode = 0o777 )

        # si le repertoire de sortie n'existe pas
        sDirOut = data[ 'dir-out' ]
        if not os.path.isdir( sDirOut ):
            os.makedirs( sDirOut, mode = 0o777 )
        
        # recuperation du projet
        oProject = None
        with open( data[ 'file' ], 'r' ) as j:
            oProject = json.loads(j.read())
        
        # generation des scripts
        oScripts = generator.getNodesByTypes( oProject[ 'data' ], 'scripts/script' )
        if len( oScripts ) > 0:
            os.makedirs( sDirTemp + os.sep + 'scripts', mode = 0o777 )
            
            # pour tous les scripts
            for oScript in oScripts:
                
                # pour le fichier model.py
                oResult += 'Generation du fichier script.py\n'
                generator.genFileFromTmpl( sPathPlugin, oScript, 'script.py', sDirTemp + os.sep + 'scripts' + os.sep + oScript[ 'text' ] + '.py', nodeScript )
        
        # generation des classes
        oClasses = generator.getNodesByTypes( oProject[ 'data' ], 'classes/classe' )
        if len( oClasses ) > 0:
            os.makedirs( sDirTemp + os.sep + 'classes', mode = 0o777 )
        
        # generation des modules
        oModules = generator.getNodesByTypes( oProject[ 'data' ], 'modules/module' )
        if len( oModules ) > 0:
            os.makedirs( sDirTemp + os.sep + 'modules', mode = 0o777 )
            
            # pour tous les modules
            oClasses = []
            for oModule in oModules:
                
                # pour le fichier model.py
                oResult += 'Generation du fichier module.py\n'
                generator.genFileFromTmpl( sPathPlugin, oModule, 'module.py', sDirTemp + os.sep + 'modules' + os.sep + oModule[ 'text' ] + '.py', module )
                oClasses.append( oModule[ 'text' ] )
            
            # creation du fichier de package
            oResult += 'Generation du fichier __init__.py des modules\n'
            generator.genFileFromTmpl( sPathPlugin, oClasses, 'initPackage.py', sDirTemp + os.sep + 'modules' + os.sep + '__init__.py', initPackage )
        
        # creation d'un fichier de configuration de base
        oConf = {
            'port': 8080,
            'host': '0.0.0.0',
            'debug': True
        }
        
        # si il y a un fichier de configuration existant
        if os.path.isfile( sDirOut + os.sep + 'configuration.json' ):
            
            # recupere les valeurs de l'existant
            oConfEXist = json.load( open( sDirOut + os.sep + 'configuration.json' ) )
            for sKey in oConf:
                if sKey not in oConfEXist:
                    oConfEXist[ sKey ] = oConf[ sKey ]
            oConf = oConfEXist
        
        # creation du fichier de configuration
        io.createJsonFile( sDirTemp + os.sep + 'configuration.json', oConf )
        
        # copie des fichiers de base
        oResult += 'Copie des fichiers de base :\n' + generator.mergeDirs( sPathPlugin + os.sep + 'templates' + os.sep + 'base', sDirTemp )
        
        # merge avec le repertoire cible
        oResult += 'Fusion avec l\'existant :\n' + generator.mergeDirs( sDirTemp, sDirOut,
            oConfig={
                'html': { 'start': '<!-- kisstomato-', 'stop': ' -->' },
                'js': { 'start': '// kisstomato-', 'stop': '-kisstomato' },
                'py': { 'start': '# kisstomato-', 'stop': '-kisstomato' },
                'sh': { 'start': '# kisstomato-', 'stop': '-kisstomato' },
                'bat': { 'start': 'rem kisstomato-', 'stop': '-kisstomato' },
                './requirements.txt': { 'start': '# kisstomato-', 'stop': '-kisstomato' }
            }
        )
        
        
        
        # kisstomato-fonction-generateFlaskCode-try-stop-user-code-kisstomato

    except Exception as e:
        # kisstomato-exception-generateFlaskCode-a-start-user-code-kisstomato
        # kisstomato-exception-generateFlaskCode-a-stop-user-code-kisstomato
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        # kisstomato-exception-generateFlaskCode-b-start-user-code-kisstomato
        print("------ ERROR ------")
        print(str( e ))
        print((exc_type, fname, exc_tb.tb_lineno))
        oResult += '\nError : ' + str( e ) + '\n' + str(exc_type) + ' : ' + str(fname) + ' : ' + str(exc_tb.tb_lineno)
        # kisstomato-exception-generateFlaskCode-b-stop-user-code-kisstomato

    # kisstomato-return-generateFlaskCode-return-start-user-code-kisstomato
    # kisstomato-return-generateFlaskCode-return-stop-user-code-kisstomato
    return oResult

# kisstomato-module-c-start-user-code-kisstomato
# kisstomato-module-c-stop-user-code-kisstomato