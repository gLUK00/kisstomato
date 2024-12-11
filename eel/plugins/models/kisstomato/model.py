# numero de version
_iCurrentVersion = 2

# creation d'un projet
def getJsonCreateNewProject( data ):
	global _iCurrentVersion

	data[ 'version' ] = _iCurrentVersion

	data[ 'data' ] = [
		{ 'id': 'roots', 'text': 'Racines', 'icon': 'fa-solid fa-cubes', 'li_attr': { 'readonly': True, 'children-type': [ 'root' ] } },
		{ 'id': 'elements', 'text': 'Eléments', 'icon': 'fa-solid fa-cubes', 'li_attr': { 'readonly': True, 'children-type': [ 'element' ] } },
		{ 'id': 'properties', 'text': 'Propriétés', 'icon': 'fa-solid fa-cubes', 'li_attr': { 'readonly': True, 'children-type': [ 'property' ] } },
		{ 'id': 'classes', 'text': 'Classe', 'icon': 'fa-solid fa-cubes', 'li_attr': { 'readonly': True, 'children-type': [ 'classe' ] } },
		{ 'id': 'templates', 'text': 'Templates', 'icon': 'fa-solid fa-book', 'li_attr': { 'readonly': True, 'children-type': [ 'template', 'directory_tmpl' ] } },
		{ 'id': 'javascripts', 'text': 'Javascripts', 'icon': 'fa-solid fa-book', 'color': '"#ff1414', 'li_attr': { 'readonly': True, 'children-type': [ 'javascript' ] } }
	]

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