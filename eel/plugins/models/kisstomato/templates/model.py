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
&& if o.oRoots|length > 0
&&  for oRoot in o.oRoots
    oRoots.append( { 'id': "{{ oRoot[ 'id' ] }}", 'text': "{{ oRoot[ 'text' ] }}"{% if 'icon' in oRoot %}, 'icon': "{{ oRoot[ 'icon' ] }}"{% endif %}{% if 'color' in oRoot %}, 'color': "{{ oRoot[ 'color' ] }}"{% endif %}, 'li_attr': { 'readonly': True, 'children-type': [ {{ oRoot[ 'children-type' ] }} ] } } )
&&  endfor
&& endif

    data[ 'data' ] = oRoots
    """[
        { 'id': 'roots', 'text': 'Racines', 'icon': 'fa-solid fa-atom', 'color': '#9c2bf7', 'li_attr': { 'readonly': True, 'children-type': [ 'root' ] } },
        { 'id': 'elements', 'text': 'Eléments', 'icon': 'fa-brands fa-deezer', 'color': '#91ec36', 'li_attr': { 'readonly': True, 'children-type': [ 'element' ] } },
        { 'id': 'properties', 'text': 'Propriétés', 'icon': 'fa-solid fa-drafting-compass', 'color': '#58dfc4', 'li_attr': { 'readonly': True, 'children-type': [ 'property' ] } },
        { 'id': 'classes', 'text': 'Classes', 'icon': 'fa-solid fa-cubes', 'color': '#c47021', 'li_attr': { 'readonly': True, 'children-type': [ 'classe' ] } },
        { 'id': 'templates', 'text': 'Templates', 'icon': 'fa-solid fa-file-image', 'color': '#b9c421', 'li_attr': { 'readonly': True, 'children-type': [ 'template', 'directory_tmpl' ] } },
        { 'id': 'javascripts', 'text': 'Javascripts', 'icon': 'fa-brands fa-js-square', 'color': '#51bd94', 'li_attr': { 'readonly': True, 'children-type': [ 'javascript' ] } }
    ]
    
    { "id": "root", "text": "Racine", "icon": "fa-brands fa-html5", "color": "#e099e5", "children-type": [], "move-on-parent": true,
			"items":[
				{ "id": "ref_element", "text": "Elément", "type": "object", "filter-type": "element" },
				{ "id": "readonly", "text": "Lecture seul", "type": "switch", "value": true }
			],
			"on-create": {
				"add": [
					{ "id": "link_childs", "text": "Enfants", "readonly": true }
				]
			}
		},
    
    """
    
    # kisstomato-getJsonCreateNewProject-b-start-user-code-kisstomato
    # kisstomato-getJsonCreateNewProject-b-stop-user-code-kisstomato

    return data

# ouverture d'un projet
def openProject( oProject ):
    global _iCurrentVersion

    if 'version' in oProject and oProject[ 'version' ] == _iCurrentVersion:
        return oProject, False

    # mise a jour de la nouvelle version
    def rewrite( oNode ):

        # si il y a des items
        if 'li_attr' in oNode and 'items' in oNode[ 'li_attr' ] and len( oNode[ 'li_attr' ][ 'items' ] ) > 0:
            for oItem in oNode[ 'li_attr' ][ 'items' ]:
                if 'id' in oItem and oItem[ 'id' ] == 'icon' and 'value' in oItem and 'style' not in oItem[ 'value' ]:
                    oItem[ 'value' ][ 'style' ] = ''

        # si il y a des enfants
        if 'children' in oNode and len( oNode[ 'children' ] ) > 0:
            for oChild in oNode[ 'children' ]:
                rewrite( oChild )

    # pour tous les elements racines
    for oNode in oProject[ 'data' ]:
        rewrite( oNode )

    oProject[ 'version' ] = _iCurrentVersion
    return oProject, True