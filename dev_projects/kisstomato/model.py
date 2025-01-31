# kisstomato-imports-start-user-code-kisstomato
# kisstomato-imports-stop-user-code-kisstomato

# numero de version
_iCurrentVersion = 1

# kisstomato-init-a-start-user-code-kisstomato
# kisstomato-init-a-stop-user-code-kisstomato

# creation d'un projet
def getJsonCreateNewProject( data ):
    global _iCurrentVersion
    
    data[ 'version' ] = _iCurrentVersion
 
    # kisstomato-getJsonCreateNewProject-a-start-user-code-kisstomato
    # kisstomato-getJsonCreateNewProject-a-stop-user-code-kisstomato
    
    oRoots = []
    oRoots.append( { "id": "templates", "text": "Templates", "icon": "fa-solid fa-book", "color": "#56b6c2", "li_attr": { "readonly": True, "children-type": ["template", "directory-template"] } } )
    oRoots.append( { "id": "routes", "text": "Routes", "icon": "fa-brands fa-hubspot", "color": "#b366ff", "li_attr": { "readonly": True, "children-type": ["directory-route", "file-routes"] } } )
    oRoots.append( { "id": "modules", "text": "Modules", "icon": "fa-solid fa-cubes", "color": "#f77373", "li_attr": { "readonly": True, "children-type": ["module-package"] } } )
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
    # kisstomato-openProject-b-stop-user-code-kisstomato

    # mise a jour de la nouvelle version
    def rewrite( oNode ):

        # kisstomato-openProject-rewrite-a-start-user-code-kisstomato
        # kisstomato-openProject-rewrite-a-stop-user-code-kisstomato

        # si il y a des enfants
        if 'children' in oNode and len( oNode[ 'children' ] ) > 0:
            for oChild in oNode[ 'children' ]:
                rewrite( oChild )
        
        # kisstomato-openProject-rewrite-b-start-user-code-kisstomato
        # kisstomato-openProject-rewrite-b-stop-user-code-kisstomato
    
    # kisstomato-openProject-c-start-user-code-kisstomato
    # kisstomato-openProject-c-stop-user-code-kisstomato

    # pour tous les elements racines
    for oNode in oProject[ 'data' ]:
        rewrite( oNode )
    
    # kisstomato-openProject-a-start-user-code-kisstomato
    # kisstomato-openProject-a-stop-user-code-kisstomato

    # mise a jour de la version
    oProject[ 'version' ] = _iCurrentVersion
    return oProject, True
