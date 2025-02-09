
// reference vers les noeuds
var oNodes = [];

// reference des parents
var _oParents = {};

// recupere la liste des noeuds sous la forme d'un tableau id/html
function nodeGetListIdHtml( oField ){

	// recupere l'ensemble des noeuds
	var oAllNodes = nodeGetAllNodes();

	// filtre les elements
	var oResults = [];
	for( var i=0; i<oAllNodes.length; i++ ){

		// ejection pour les lectures seule et les elements sans proprietes
		if( oAllNodes[ i ][ 'li_attr' ] == undefined ||
			( oAllNodes[ i ][ 'li_attr' ][ 'readonly' ] != undefined && oAllNodes[ i ][ 'li_attr' ][ 'readonly' ] ) ){
			continue;
		}

		// si il y a un filtre sur le type
		if( oField[ 'filter-type' ] != undefined && oAllNodes[ i ][ 'li_attr' ][ 'type' ] != oField[ 'filter-type' ] ){
			continue;
		}

		// recupere le nom au format HTML
		let oNode = Object.assign( {}, oAllNodes[ i ] );
		oNode[ 'html' ] = nodeGetHtmlName( oNode );

		// recupere l'element
		oResults.push( oNode );
	}


	/*var oItems = [ { id: '12sd1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '12sdd1f', html: '<b>sdfsfsdf</b> df <b>dsfsdfds</b>' },
		{ id: '12sdf1f', html: '<b>sdfsfsdf</b> aadfaa <b>dsfsdfds</b>' },
		{ id: '1h2sd1f', html: '<b>sdfsfsdf</b> aaaddfa <b>dsfsdfds</b>' },
		{ id: '12jsd1f', html: '<b>sdfsfsdf</b> aaaasdf <b>dsfsdfds</b>' },
		{ id: '12skd1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '12sdl1f', html: '<b>sdfsfsdf</b> aaaasss <b>dsfsdfds</b>' },
		{ id: '12sd1mf', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '12sd1fo', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: 'q12sd1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '1s2sd1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '12dsd1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '12sfd1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: 'q12sdd1f', html: '<b>sdfsfsdf</b> df <b>dsfsdfds</b>' },
		{ id: '1q2sdf1f', html: '<b>sdfsfsdf</b> aadfaa <b>dsfsdfds</b>' },
		{ id: '1hq2sd1f', html: '<b>sdfsfsdf</b> aaaddfa <b>dsfsdfds</b>' },
		{ id: '12jqsd1f', html: '<b>sdfsfsdf</b> aaaasdf <b>dsfsdfds</b>' },
		{ id: '12skqd1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '12sdlq1f', html: '<b>sdfsfsdf</b> aaaasss <b>dsfsdfds</b>' },
		{ id: '12sd1mqf', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '12sd1foq', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: 'wq12sd1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '1ws2sd1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '12wdsd1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '12swfd1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' },
		{ id: '12sdwgh1f', html: '<b>sdfsfsdf</b> aaaa <b>dsfsdfds</b>' }
	];*/

	return { oItems: oResults, sKey: 'html' };
}

// retourne le nom d'un noeud au format HTML
function nodeGetHtmlName( oNode ){
	if( oNode == null ){
		return '';
	}
	let sHtml = oNode[ 'text' ];
	if( oNode[ 'icon' ] != undefined ){
		sHtml = '<i class="' + oNode[ 'icon' ] + '"></i>&nbsp' + sHtml;
	}
	if( _oParents[ oNode[ 'id' ] ] != undefined ){
		sHtml = nodeGetHtmlName( _oParents[ oNode[ 'id' ] ] ) + '&nbsp;/&nbsp;' + sHtml;
	}
	return sHtml;
}

// retourne la liste de tous les noeuds
function nodeGetAllNodes(){
	var fGetAll = function( oNodesFind, oParent ){
		let oAll = [];
		for( var i=0; i<oNodesFind.length; i++ ){
			if( oParent != undefined ){
				//oNodesFind[ i ][ 'parent' ] = oParent;
				_oParents[ oNodesFind[ i ][ 'id' ] ] = oParent;
			}
			oAll.push( oNodesFind[ i ] );
			if( oNodesFind[ i ].children != undefined && oNodesFind[ i ].children.length > 0 ){
				oAll = oAll.concat( fGetAll( oNodesFind[ i ].children, oNodesFind[ i ] ) );
			}
		}
		return oAll;
	};

	return fGetAll( oNodes );
}

// recherche un noeud en fonction de son id
// avec option de retour du parent
function nodeGetNode( id, _nodes, oParent ){
	if( _nodes == undefined ){
		_nodes = oNodes;
	}
	for( var i=0; i<_nodes.length; i++ ){
		//_nodes[ i ].parent = oParent;
		if( oParent != undefined ){
			//_nodes[ i ][ 'parent' ] = oParent;
			_oParents[ _nodes[ i ][ 'id' ] ] = oParent;
		}
		if( _nodes[ i ].id == id ){
			return _nodes[ i ]
		}else if( _nodes[ i ].children != undefined && _nodes[ i ].children.length > 0 ){
			var oNode = nodeGetNode( id, _nodes[ i ].children, _nodes[ i ] );
			if( oNode != null ){
				return oNode
			}
		}
	}
	return null;
}

// recherche un noeud parent
function nodeGetParent( id ){
	var oParent = _oParents[ id ]
	return oParent !== undefined ? oParent : null;
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

	var sId = generate_uuidv4();
	var oNewNode = { 'id': sId, 'text': sText,
		"li_attr": {
			"type": oModelItem[ 'id' ]
			//"children-type": oModelItem[ 'children-type' ]
		} };

	// si il y a des attributs sur le modele, fusion
	if( oModelItem[ "li_attr" ] != undefined ){
		for( var sKey in oModelItem[ "li_attr" ] ){
			oNewNode[ "li_attr" ][ sKey ] = oModelItem[ "li_attr" ][ sKey ];
		}
	}

	// si il a une couleur
	if( oModelItem[ 'color' ] != undefined ){
		oNewNode[ 'color' ] = oModelItem[ 'color' ];
	}

	// si il y a un icon sur le modele
	if( oModelItem[ 'icon' ] != undefined ){
		oNewNode[ 'icon' ] = oModelItem[ 'icon' ];
	}else{

		// recherche l'icone sur le modele
		var oFindModelItem = modelGetElementById( oModelItem[ 'id' ] );
		if( oFindModelItem[ 'icon' ] != undefined ){
			oNewNode[ 'icon' ] = oFindModelItem[ 'icon' ];
		}
	}

	// si il y a des donnees
	if( oData != null ){
		oNewNode[ 'li_attr' ][ 'items' ] = oData;
	}

	// ajout au treeview du projet
	oNodeParent[ 'children' ].push( oNewNode );

	// ouvre le parent
	//oNodeParent[ 'state' ] = { "opened": true };

	// si il y a des actions a effectuer sur la creation du nouvelle element
	if( oModelItem[ 'on-create' ] != undefined ){

		// si il y a des ajouts automatiques
		if( oModelItem[ 'on-create' ][ 'add' ] != undefined ){

			// pour tous les elements a ajouter
			for( var i=0; i<oModelItem[ 'on-create' ][ 'add' ].length; i++ ){
				let oAddItem = oModelItem[ 'on-create' ][ 'add' ][ i ];
				let oNewNodeItem = { "id": oAddItem[ 'id' ], "li_attr": {} }

				// si il a une couleur
				let oAddModelItem = modelGetElementById( oAddItem[ 'id' ] );
				if( oAddModelItem[ 'color' ] != undefined ){
					oNewNodeItem[ 'color' ] = oAddModelItem[ 'color' ];
				}

				// si c'est un mode en lecture seul
				if( oAddItem[ 'readonly' ] != undefined ){
					oNewNodeItem[ 'li_attr' ][ 'readonly' ] = oAddItem[ 'readonly' ];
				}

				// si il y a des donnees
				var oNewData = null;
				if( oAddItem[ 'data' ] != undefined ){
					oNewData = oAddItem[ 'data' ];
				}

				nodeAddNode( sId, oAddItem[ 'text' ], oNewNodeItem, oNewData );
			}
		}
	}

	nodeRefreshTreeview();
}

// affichage du treeview
function nodeRefreshTreeview(){
	$('#tree').jstree(true).settings.core.data = oNodes;
	$('#tree').jstree(true).refresh();
	//nodeRefreshColor( oNodes );
}

// mise a jour des couleurs des noeuds
var _bFirstResfreshColor = [];
async function nodeRefreshColor( oNodes, bFirst ){
	let bItsFirst = false;
	if( bFirst === undefined ){
		_bFirstResfreshColor = [];
		bItsFirst = true;
	}
	if( Array.isArray( oNodes ) ){
		for( var i=0; i<oNodes.length; i++ ){
			_bFirstResfreshColor.push.apply( _bFirstResfreshColor, nodeRefreshColor( oNodes[ i ], true ) );
		}
	}

	// si il y a des enfants
	if( oNodes[ 'children' ] !== undefined && oNodes[ 'children' ].length > 0 ){
		_bFirstResfreshColor.push.apply( _bFirstResfreshColor, nodeRefreshColor( oNodes[ 'children' ], true ) );
	}

	// si l'element a une propriete de couleur
	if( oNodes[ 'color' ] !== undefined && oNodes[ 'color' ] != '' ){
		_bFirstResfreshColor.push( { id: oNodes[ 'id' ], color: oNodes[ 'color' ] })
	}

	if( !bItsFirst ){
		return;
	}

	// application des couleurs
	window.setTimeout( function(){
		for( var i=0; i<_bFirstResfreshColor.length; i++ ){
			$( '#' + _bFirstResfreshColor[ i ][ 'id' ] ).find( 'svg:first' ).css( 'color', _bFirstResfreshColor[ i ][ 'color' ] );
		}
	}, 10 );
}

// memorisation des etats des noeuds
async function nodeOpenClose( e, oNode ){

	// enregistrement de l'etat du noeud
	if( localStorage.getItem( 'kisstomato-state-treeview' ) == null ){
		localStorage.setItem( 'kisstomato-state-treeview', JSON.stringify( {} ) );
	}
	let oStates = JSON.parse( localStorage.getItem( 'kisstomato-state-treeview' ) );
	oStates[ oNode.node.id ] = oNode.node.state.opened;
	localStorage.setItem( 'kisstomato-state-treeview', JSON.stringify( oStates ) );
}

// mise a jour des etats des noeuds
function setStateOpenClode( oNodes ){
	if( Array.isArray( oNodes ) ){
		for( var i=0; i<oNodes.length; i++ ){
			setStateOpenClode( oNodes[ i ] )
		}
		return;
	}

	// si il y a des enfants
	if( oNodes[ 'children' ] !== undefined && oNodes[ 'children' ].length > 0 ){
		setStateOpenClode( oNodes[ 'children' ] );
	}

	// controle de l'etat
	if( localStorage.getItem( 'kisstomato-state-treeview' ) == null ){
		return;
	}
	let oStates = JSON.parse( localStorage.getItem( 'kisstomato-state-treeview' ) );
	let oState =  oStates[ oNodes.id ];
	if( oState == undefined ){
		return;
	}

	// application de l'etat du noeud
	if( oNodes[ 'state' ] == undefined ){
		oNodes[ 'state' ] = {};
	}
	if( oNodes[ 'state' ][ 'opened' ] == undefined ){
		oNodes[ 'state' ][ 'opened' ] = false;
	}
	oNodes[ 'state' ][ 'opened' ] = oState;
}

// recupere un formulaire a partir d'un noeud et son type
function nodeNode2Form( oRefNode ){
	var oForm = [];
	var oNode = JSON.parse(JSON.stringify( oRefNode ));

	// recherche de l'element dans le modele
	var oElement = null;
	for( var i=0; i<oModel[ 'elements' ].length; i++ ){
		if( oNode[ 'li_attr' ][ 'type' ] == oModel[ 'elements' ][ i ].id ){
			oElement = JSON.parse(JSON.stringify( oModel[ 'elements' ][ i ] ));
			break;
		}
	}

	for( var i=0; i<oElement.items.length; i++ ){

		// recupere l'element du noeud
		var oItem = null;
		for( var a=0; a<oNode[ 'li_attr' ][ 'items' ].length; a++ ){
			if( oNode[ 'li_attr' ][ 'items' ][ a ].id == oElement.items[ i ].id ){
				oItem = JSON.parse(JSON.stringify( oNode[ 'li_attr' ][ 'items' ][ a ] ));
				break;
			}
		}

		if( oItem != null ){
			oElement.items[ i ].value = oItem.value;
		}
		oForm.push( oElement.items[ i ] );
	}

	return oForm;
}