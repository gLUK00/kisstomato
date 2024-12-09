
def getJsonCreateNewProject( data ):

	data[ 'data' ] = [
		{ 'id': 'roots', 'text': 'Racines', 'icon': 'fa-solid fa-cubes', 'li_attr': { 'readonly': True, 'children-type': [ 'root' ] } },
		{ 'id': 'elements', 'text': 'Eléments', 'icon': 'fa-solid fa-cubes', 'li_attr': { 'readonly': True, 'children-type': [ 'element' ] } },
		{ 'id': 'properties', 'text': 'Propriétés', 'icon': 'fa-solid fa-cubes', 'li_attr': { 'readonly': True, 'children-type': [ 'property' ] } },
		{ 'id': 'classes', 'text': 'Classe', 'icon': 'fa-solid fa-cubes', 'li_attr': { 'readonly': True, 'children-type': [ 'classe' ] } },
		{ 'id': 'templates', 'text': 'Templates', 'icon': 'fa-solid fa-book', 'li_attr': { 'readonly': True, 'children-type': [ 'template', 'directory_tmpl' ] } },
		{ 'id': 'javascripts', 'text': 'Javascripts', 'icon': 'fa-solid fa-book', 'li_attr': { 'readonly': True, 'children-type': [ 'javascript' ] } }
	]

	return data