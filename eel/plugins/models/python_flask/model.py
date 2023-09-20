
def getJsonCreateNewProject( data ):

	data[ 'data' ] = [
		{ 'id': 'templates', 'text': 'Templates', 'icon': 'fa-solid fa-tree', 'li_attr': { 'readonly': True, 'children-type': [ 'template', 'directory' ] } },
		{ 'id': 'routes', 'text': 'Routes', 'li_attr': { 'readonly': True, 'children-type': [ 'route' ] } }
	]

	return data