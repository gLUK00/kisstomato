# kisstomato-imports-start-user-code-kisstomato

import uuid

# importation du CORE
from core import model

# kisstomato-imports-stop-user-code-kisstomato

# numero de version
_iCurrentVersion = 1

# kisstomato-init-a-start-user-code-kisstomato
_iCurrentVersion = 5
# kisstomato-init-a-stop-user-code-kisstomato

# creation d'un projet
def getJsonCreateNewProject( data ):
    global _iCurrentVersion
    
    data[ 'version' ] = _iCurrentVersion
 
    # kisstomato-getJsonCreateNewProject-a-start-user-code-kisstomato
    # kisstomato-getJsonCreateNewProject-a-stop-user-code-kisstomato
    
    oRoots = []
    oRoots.append( { "id": "classes", "text": "Classes", "icon": "fa-solid fa-boxes", "color": "#37c347", "li_attr": { "readonly": True, "children-type": ["classe"] } } )
    oRoots.append( { "id": "templates", "text": "Templates", "icon": "fa-solid fa-book", "color": "#56b6c2", "li_attr": { "readonly": True, "children-type": ["template", "directory-template"] } } )
    oRoots.append( { "id": "routes", "text": "Routes", "icon": "fa-brands fa-hubspot", "color": "#b366ff", "li_attr": { "readonly": True, "children-type": ["directory-route", "file-routes"] } } )
    oRoots.append( { "id": "modules", "text": "Modules", "icon": "fa-solid fa-cubes", "color": "#f77373", "li_attr": { "readonly": True, "children-type": ["module"] } } )
    oRoots.append( { "id": "decorators", "text": "Décorateurs", "icon": "fa-solid fa-photo-video", "color": "#ec4b4b", "li_attr": { "readonly": True, "children-type": ["decorator"] } } )
    oRoots.append( { "id": "scripts", "text": "Scripts", "icon": "fa-solid fa-scroll", "color": "#263ef2", "li_attr": { "readonly": True, "children-type": ["script"] } } )
    data[ 'data' ] = oRoots

    # kisstomato-getJsonCreateNewProject-b-start-user-code-kisstomato
    # kisstomato-getJsonCreateNewProject-b-stop-user-code-kisstomato

    return data

# ouverture d'un projet
def openProject( oProject ):
    global _iCurrentVersion

    # kisstomato-openProject-a-start-user-code-kisstomato
    # kisstomato-openProject-a-stop-user-code-kisstomato

    if 'version' in oProject and oProject[ 'version' ] == _iCurrentVersion:
        return oProject, False
    
    # kisstomato-openProject-b-start-user-code-kisstomato
    global oModel
    oModel = model.getOne( oProject[ 'model' ] )
    # kisstomato-openProject-b-stop-user-code-kisstomato

    # mise a jour de la nouvelle version
    def rewrite( oNode ):

        # kisstomato-openProject-rewrite-a-start-user-code-kisstomato
        """
        
        """
        global oModel
        if 'type' in oNode[ 'li_attr' ]:
            sType = oNode[ 'li_attr' ][ 'type' ]
            
            # determine si il y a des enfants en mode on-create > add
            oEle = model.getElementById( sType, oModel )
            if 'on-create' in oEle and 'add' in oEle[ 'on-create' ]:
                
                # pour tous les sous elements
                for oSubEle in oEle[ 'on-create' ][ 'add' ]:
                    
                    # determine la presence dans le noeud
                    bExist = False
                    for oChild in oNode[ 'children' ]:
                        if oChild[ 'li_attr' ][ 'type' ] == oSubEle[ 'id' ]:
                            bExist = True
                            break
                    
                    # creation du sous element
                    if not bExist:
                    
                        bReadonly = oSubEle[ 'readonly' ]
                        sText = oSubEle[ 'text' ]
                        oSubEleA = model.getElementById( oSubEle[ 'id' ], oModel )
                        oNewNode = {
                            'id': str( uuid.uuid4() ),
                            'text': sText,
                            'li_attr': { 'type': oSubEle[ 'id' ] }
                        }
                        if 'color' in oSubEleA:
                            oNewNode[ 'color' ] = oSubEleA[ 'color' ]
                        if 'icon' in oSubEleA:
                            oNewNode[ 'icon' ] = oSubEleA[ 'icon' ]
                        if bReadonly:
                            oNewNode[ 'li_attr' ][ 'readonly' ] = bReadonly
                        oNode[ 'children' ].append( oNewNode )

        # kisstomato-openProject-rewrite-a-stop-user-code-kisstomato

        # si il y a des enfants
        if 'children' in oNode and len( oNode[ 'children' ] ) > 0:
            for oChild in oNode[ 'children' ]:
                rewrite( oChild )
        
        # kisstomato-openProject-rewrite-b-start-user-code-kisstomato
        # kisstomato-openProject-rewrite-b-stop-user-code-kisstomato
    
    # kisstomato-openProject-c-start-user-code-kisstomato
    
    # controle des elements racines
    oNewRoot = []
    oRootElements = getJsonCreateNewProject( {} )
    for oRootEle in oRootElements[ 'data' ]:
        bExist = False
        for oNode in oProject[ 'data' ]:
            if oNode[ 'id' ] == oRootEle[ 'id' ]:
                bExist = True
                oNewRoot.append( oNode )
                break
        if not bExist:
            oNewRoot.append( oRootEle )
    
    # remplacement des noeuds racines
    if len( oNewRoot ) != len( oProject[ 'data' ] ):
        oProject[ 'data' ] = oNewRoot
    
    # kisstomato-openProject-c-stop-user-code-kisstomato

    # pour tous les elements racines
    for oNode in oProject[ 'data' ]:
        rewrite( oNode )
    
    # kisstomato-openProject-a-start-user-code-kisstomato
    # kisstomato-openProject-a-stop-user-code-kisstomato

    # mise a jour de la version
    oProject[ 'version' ] = _iCurrentVersion
    return oProject, True
