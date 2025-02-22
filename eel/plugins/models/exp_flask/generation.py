# kisstomato-module-a-start-user-code-kisstomato
# kisstomato-module-a-stop-user-code-kisstomato

import json, os, sys, shutil

from core import generator

# referencement du repertoire parent
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)

from classes import *

# kisstomato-module-b-start-user-code-kisstomato
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