
def getJsonCreateNewProject( data ):

	data[ 'data' ] = [
		{ 'id': 'templates', 'text': 'Templates', 'icon': 'fa-solid fa-book', 'li_attr': { 'readonly': True, 'children-type': [ 'template', 'directory' ] } },
		{ 'id': 'routes', 'text': 'Routes', 'icon': 'fa-brands fa-hubspot', 'li_attr': { 'readonly': True, 'children-type': [ 'route', 'route-directory' ] } },
		{ 'id': 'modules', 'text': 'Modules', 'icon': 'fa-solid fa-cubes', 'li_attr': { 'readonly': True, 'children-type': [ 'module-package' ] } },
		{ 'id': 'decorators', 'text': 'Décorateurs', 'icon': 'fa-brands fa-stack-overflow', 'li_attr': { 'readonly': True, 'children-type': [ 'decorator' ] } }
	]
	"""
	{ 'id': 'parameters', 'text': 'Paramètres', 'li_attr': { 'readonly': True },
			"children": [
				{ 'id': 'modules', 'text': 'Modules', 'icon': 'fa-solid fa-tree', 'li_attr': { 'readonly': True, 'children-type': [ 'module-package' ] } },
				{ 'id': 'decorators', 'text': 'Décorateurs', 'icon': 'fa-solid fa-tree', 'li_attr': { 'readonly': True, 'children-type': [ 'decorator' ] } }
			]
		}
	
	data[ 'properties' ] = [
		{ "id": "token-validator", "value": False },
		{ "id": "secure-decorator", "value": "" }
	]
	"""

	return data