
def getJsonCreateNewProject( data ):

	data[ 'data' ] = [
		{ 'id': 'pages', 'text': 'Pages', 'icon': 'fa-solid fa-tree', 'li_attr': { 'readonly': True, 'children-type': [ 'page' ] } },
		{ 'id': 'contents', 'text': 'Contenus', 'li_attr': { 'readonly': True, 'children-type': [ 'content' ] } }
	]

	return data



"""
https://mdbootstrap.com/freebies/admin/
"""