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
        
        # liste des fichiers a exclure
        oExcludeFiles = []

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
        oClassesPrg = generator.getNodesByTypes( oProject[ 'data' ], 'classes/classe' )
        if len( oClassesPrg ) > 0:
            os.makedirs( sDirTemp + os.sep + 'classes', mode = 0o777 )
            
            # pour toutes les classes
            oClasses = []
            for oClass in oClassesPrg:

                # pour le fichier classe.py
                oResult += 'Generation du fichier classe.py\n'
                generator.genFileFromTmpl( sPathPlugin, oClass, 'classe.py', sDirTemp + os.sep + 'classes' + os.sep + oClass[ 'text' ] + '.py', classe )
                oClasses.append( oClass[ 'text' ] )

            # creation du fichier de package
            oResult += 'Generation du fichier __init__.py des classes\n'
            generator.genFileFromTmpl( sPathPlugin, oClasses, 'initPackage.py', sDirTemp + os.sep + 'classes' + os.sep + '__init__.py', initPackage )
        
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
        
        # copie des fichiers de base
        oResult += 'Copie des fichiers de base :\n' + generator.mergeDirs( sPathPlugin + os.sep + 'templates' + os.sep + 'base', sDirTemp )
        
        # generation des repertoires des templates
        oDirTemplates = generator.getNodesByTypes( oProject[ 'data' ], 'directory-template', subSearch=True )
        if len( oDirTemplates ) > 0:
            
            # pour tous les repertoires de templates
            for oDir in oDirTemplates:
                sDirTmpl = sDirTemp + os.sep + 'web' + os.sep + 'templates' + os.sep + oDir[ 'path' ][ len( '/Templates/' ) : ] + '/' + oDir[ 'text' ]
                sDirTmpl = sDirTmpl.replace( '//', os.sep ).replace( '/', os.sep )
                
                print( 'creation du repertoire de templates : ' + sDirTmpl )
                os.makedirs( sDirTmpl, mode = 0o777 )

        # generation des templates
        oTemplates = generator.getNodesByTypes( oProject[ 'data' ], 'template', subSearch=True )
        if len( oTemplates ) > 0:
            
            # pour tous les templates
            for oTemplate in oTemplates:
                
                # creation d'un fichier de template
                sHtml = sDirTemp + os.sep + 'web' + os.sep + 'templates' + os.sep + oTemplate[ 'path' ][ len( '/Templates/' ) : ] + '/' + oTemplate[ 'text' ] + '.html'
                sHtml = sHtml.replace( '//', os.sep ).replace( '/', os.sep )

                print( 'creation du fichier de template : ' + sHtml )
                open( sHtml, 'a' ).close()
                oExcludeFiles.append( sHtml )
        
        """
        "directory-route"
        "route"
        
        """
        
        # generation des repertoires des routes
        oDirRoutes = generator.getNodesByTypes( oProject[ 'data' ], 'directory-route', subSearch=True )
        if len( oDirRoutes ) > 0:

            # pour tous les repertoires de routes
            for oDir in oDirRoutes:
                sDirRoute = sDirTemp + os.sep + 'routes' + os.sep + oDir[ 'path' ][ len( '/Routes/' ) : ] + '/' + oDir[ 'text' ]
                sDirRoute = sDirRoute.replace( '//', os.sep ).replace( '/', os.sep )

                print( 'creation du repertoire de routes : ' + sDirRoute )
                os.makedirs( sDirRoute, mode = 0o777 )
        
        # generation des routes
        oRoutes = generator.getNodesByTypes( oProject[ 'data' ], 'route', subSearch=True )
        if len( oRoutes ) > 0:
            
            # pour toutes les routes
            oRouteImports = []
            for oRoute in oRoutes:
                
                # creation d'un fichier de route
                sRoutePath = oRoute[ 'path' ][ len( '/Routes/' ) : ]
                sRoute = sDirTemp + os.sep + 'fl_routes' + os.sep + sRoutePath + '/' + oRoute[ 'text' ] + '.py'
                sRoute = sRoute.replace( '//', os.sep ).replace( '/', os.sep )

                oRouteImports.append( 'from fl_routes.' + sRoutePath.replace( '/', '.' ) + ' import ' + oRoute[ 'text' ] )

                print( 'creation du fichier de route : ' + sRoute )
                #open( sRoute, 'a' ).close()
        
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
        
        # merge avec le repertoire cible
        oResult += 'Fusion avec l\'existant :\n' + generator.mergeDirs( sDirTemp, sDirOut,
            oConfig={
                #'html': { 'start': '<!-- kisstomato-', 'stop': ' -->' },
                'js': { 'start': '// kisstomato-', 'stop': '-kisstomato' },
                'py': { 'start': '# kisstomato-', 'stop': '-kisstomato' },
                'sh': { 'start': '# kisstomato-', 'stop': '-kisstomato' },
                'bat': { 'start': 'rem kisstomato-', 'stop': '-kisstomato' },
                './requirements.txt': { 'start': '# kisstomato-', 'stop': '-kisstomato' }
            },
            oExcludeFiles=oExcludeFiles
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