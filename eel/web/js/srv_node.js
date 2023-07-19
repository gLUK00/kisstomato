
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

// supprime un noeud en fonction de son id
function nodeDeleteNode( id, _nodes ){
	let bFirstCall = false;
	if( _nodes == undefined ){
		_nodes = oNodes;
		bFirstCall = true;
	}
	var oNewNodes = [];
	for( var i=0; i<_nodes.length; i++ ){

		if( _nodes[ i ].id == id ){
			continue;
		}

		oNewNodes.push( Object.assign( {}, _nodes[ i ] ) );

		// si il y a des enfants
		if( oNewNodes[ oNewNodes.length - 1 ].children != undefined && oNewNodes[ oNewNodes.length - 1 ].children.length > 0 ){
			oNewNodes[ oNewNodes.length - 1 ].children = nodeDeleteNode( id, oNewNodes[ oNewNodes.length - 1 ].children );
		}
	}

	if( bFirstCall ){
		oNodes = oNewNodes;
		nodeRefreshTreeview();
	}else{
		return oNewNodes;
	}
}

// mise a jour d'un noeud
function nodeUpdateNode( oNode, _nodes ){
	if( _nodes == undefined ){
		_nodes = oNodes;
	}
	for( var i=0; i<_nodes.length; i++ ){
		if( _nodes[ i ].id == oNode.id ){
			_nodes[ i ] = oNode;
			nodeRefreshTreeview();
			return true;
		}else if( _nodes[ i ].children != undefined && _nodes[ i ].children.length > 0 ){
			if( nodeUpdateNode( oNode, _nodes[ i ].children ) ){
				return true;
			}
		}
	}
	return false;
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

	// si il y a un icon sur le modele
	if( oModelItem[ 'icon' ] != undefined ){
		oNewNode[ 'icon' ] = oModelItem[ 'icon' ];
	}

	// si il y a des donnees
	if( oData != null ){
		oNewNode[ 'li_attr' ][ 'items' ] = oData;
	}

	// ajout au treeview du projet
	oNodeParent[ 'children' ].push( oNewNode );

	// ouvre le parent
	oNodeParent[ 'state' ] = { "opened": true };

	nodeRefreshTreeview();
}

// affichage du treeview
function nodeRefreshTreeview(){
	$('#tree').jstree(true).settings.core.data = oNodes;
	$('#tree').jstree(true).refresh();
}

// recupere un formulaire a partir d'un noeud et son type
function nodeNode2Form( oNode ){
	var oForm = [];

	// recherche de l'element dans le modele
	var oElement = null;
	for( var i=0; i<oModel.length; i++ ){
		if( oNode[ 'li_attr' ][ 'type' ] == oModel[ i ].id ){
			oElement = Object.assign( {}, oModel[ i ] );
			break;
		}
	}

	for( var i=0; i<oElement.items.length; i++ ){

		// recupere l'element du noeud
		var oItem = null;
		for( var a=0; a<oNode[ 'li_attr' ][ 'items' ].length; a++ ){
			if( oNode[ 'li_attr' ][ 'items' ][ a ].id == oElement.items[ i ].id ){
				oItem = oNode[ 'li_attr' ][ 'items' ][ a ];
				break;
			}
		}

		oElement.items[ i ].value = oItem.value;
		oForm.push( oElement.items[ i ] );
	}

	return oForm;
}