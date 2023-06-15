
// reference vers les noeuds
var oNodes = [];

// recherche un noeud en fonction de son id
function nodeGetNode( id, _nodes ){
	if( _nodes == undefined ){
		_nodes = oNodes;
	}
	for( var i=0; i<_nodes.length; i++ ){
		if( _nodes[ i ].id == id ){
			return _nodes[ i ];
		}else if( _nodes[ i ].children != undefined && _nodes[ i ].children.length > 0 ){
			var oNode = nodeGetNode( id, _nodes[ i ].children );
			if( oNode != null ){
				return oNode;
			}
		}
	}
	return null;
}

// mise a jour d'un noeud
function nodeUpdateNode(){
	
}

// ajout d'un noeud
function nodeAddNode( idParent, sText, oModelItem, oData ){

	var oNodeParent = nodeGetNode( idParent );
	if( oNodeParent[ 'children' ] == undefined ){
		oNodeParent[ 'children' ] = [];
	}

	var oNewNode = { 'id': generate_uuidv4(), 'text': sText,
		"li_attr": {
			"type": oModelItem[ 'id' ]
			//"children-type": oModelItem[ 'children-type' ]
		} };

	// si il y a des donnees
	if( oData != null ){
		oNewNode[ 'li_attr' ][ 'items' ] = oData;
	}

	// ajout au treeview du projet
	oNodeParent[ 'children' ].push( oNewNode );

	// ouvre le parent
	oNodeParent[ 'state' ] = { "opened": true };

	console.log( 'yyyyyyyyyyyyyyyyyyyyyy' );
	console.log( oNewNode );
	console.log( oNodeParent );

	nodeRefreshTreeview();
}

// affichage du treeview
function nodeRefreshTreeview(){
	
	$('#tree').jstree(true).settings.core.data = oNodes;
	$('#tree').jstree(true).refresh();

	console.log( 'nodeRefreshTreeview' );
	console.log( oNodes );
}