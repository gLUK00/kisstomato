
def getJsonCreateNewProject( data ):

	data[ 'data' ] = [
		{ 'id': 'templates', 'text': 'Templates', 'icon': 'fa-solid fa-tree', 'li_attr': { 'readonly': True, 'children-type': [ 'template', 'directory' ] } },
		{ 'id': 'routes', 'text': 'Routes', 'li_attr': { 'readonly': True, 'children-type': [ 'route' ] } },
		{ 'id': 'parameters', 'text': 'Paramètres', 'li_attr': { 'readonly': True },
			"children": [
				{ 'id': 'helpers', 'text': 'Helpers', 'icon': 'fa-solid fa-tree', 'li_attr': { 'readonly': True, 'children-type': [ 'helper' ] } },
				{ 'id': 'decorators', 'text': 'Décorateurs', 'icon': 'fa-solid fa-tree', 'li_attr': { 'readonly': True, 'children-type': [ 'decorator' ] } }
			]
		}
	]
	"""data[ 'properties' ] = [
		{ "id": "token-validator", "value": False },
		{ "id": "secure-decorator", "value": "" }
	]
	"""

	return data