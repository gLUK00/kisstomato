//$.jstree.defaults.core.themes.dir = "css/themes";
/*
https://fontawesome.com/search?o=r&m=free
https://www.jstree.com/docs/json/
*/

$( document ).ready( function(){
	//fullScreen();

	// liaison de l'evenement d'affichage du selecteur d'un objet
	tabSetShowSelectObject( nodeGetListIdHtml );
} );

// noeud selctionne
var oSelectNode = null;

// chargement da la navbar
var oInfoProject = {};
var oModel = {};
var oPropertiesProject = {};
eel.open_project( getUrlParameter( 'project' ) )( function( data ){

	// alimente le type
	oInfoProject = data[ 'info' ];
	$( 'title' ).html( data[ 'model' ][ 'title' ] + ' : ' + oInfoProject[ 'name' ] );
	$( '#project_title' ).html( data[ 'model' ][ 'title' ] + ' : ' + oInfoProject[ 'name' ] );

	// si le projet a des proprietes
	if( data[ 'properties' ] !== undefined ){
		oPropertiesProject = data[ 'properties' ];
	}

	// recupere le modele
	//oModel = data[ 'model' ][ 'elements' ];
	oModel = data[ 'model' ];

	// importation des fichiers javascript
	for( var i=0; i<data[ 'js' ].length; i++ ){
		eel.get_javascript( data[ 'info' ][ 'model' ], data[ 'js' ][ i ] )( function( sJsCode ){
			eval( sJsCode );
		} );
	}

	// creation des noeuds
	//oNodes = [];
	for( var i=0; i<data[ 'data' ].length; i++ ){
		var oItem = data[ 'data' ][ i ];


		oNodes.push( oItem );
	}

	$('#tree').jstree({
		"core" : {
			'data' : oNodes
		}
	});

	console.log( 'open_project' );
	console.log( data );
	console.log( oModel );
} );







/*


chargement factice


*/
/*window.setTimeout( function(){
	oTabs.push( { id: 's6d4fsd65f', text: 'Nouveau', state: 'new', form: [
		{ id: "4sf5sdff4_page_object", text: "un_objet", type: "object", "filter-type": "page" },
		{ id: '4sf5sdff4', type: 'icon', text: 'Une Icone', icon: 'android', color: '#11ccc0' },
		{ id: '4sf5sd4', type: 'string', text: 'Nom', value: 'un truc' },
		{ id: '4sfsss5sd4switch', type: 'switch', text: 'Un switch', value: true },
		{ id: '4sfsss5sd4', type: 'string', text: 'Nom 2' },
		{ id: '4sfsss5sdaa4', type: 'range', text: 'Un range', min:0, max:15, value:3 },
		{ id: '4sfsss5sdss4', type: 'int', text: 'Un nombre' },
		{ id: '4sfsss5sd4ddd', type: 'text', text: 'Un texte' },
		{ id: 'utut', type: 'list', text: 'Une liste', value:'b', items:[
				{ text: 'valeur a', value: 'a' },
				{ text: 'valeur b', value: 'b' },
				{ text: 'valeur c', value: 'c' }
			]
		},
		{ id: 'ututss', type: 'checkbox', text: 'Une liste de CAC', values:[ 'a', 'c' ], items:[
				{ text: 'valeur a', value: 'a' },
				{ text: 'valeur b', value: 'b' },
				{ text: 'valeur c', value: 'c' }
			]
		},
		{ id: 'yytyt', type: 'radio', text: 'Une liste radio', value:'c', items:[
				{ text: 'valeur a', value: 'a' },
				{ text: 'valeur b', value: 'b' },
				{ text: 'valeur c', value: 'c' }
			]
		},
		{ id: 'uuu465fd4g', type: 'color', text: 'Une couleur', value:'#cccccc' },
		], focus: true } );
	oTabs.push( { id: '7aed063d-8fa5-47c7-b824-fd5b7ab49055', text: 'Edition', state: 'edit', form: [] } );
	oTabs.push( { id: '7aed063d-8fa5-47c7-b824-fd5b7ab49888', text: 'un autre', state: 'view', form: [
		{ id: '4sf5sd422', type: 'string', text: 'Nom', value: 'un truc' },
		{ id: "4sf5sdff4_page_objectssss", text: "un_objet", type: "object" },
		{ id: '4sfsss5sssd4switch', type: 'switch', text: 'Un switch' },
		{ id: 'sdsdsrrrrr', type: 'range', text: 'Un range', min:0, max:15 },
		{ id: 'uaatut', type: 'list', text: 'Une liste', value:'b', items:[
				{ text: 'valeur a', value: 'a' },
				{ text: 'valeur b', value: 'b' },
				{ text: 'valeur c', value: 'c' }
			]
		},
		{ id: 'uaatutss', type: 'checkbox', text: 'Une liste de CAC', values:[ 'a', 'c' ], items:[
				{ text: 'valeur a', value: 'a' },
				{ text: 'valeur b', value: 'b' },
				{ text: 'valeur c', value: 'c' }
			]
		},
		{ id: 'yytytaa', type: 'radio', text: 'Une liste radio', items:[
				{ text: 'valeur a', value: 'a' },
				{ text: 'valeur b', value: 'b' },
				{ text: 'valeur c', value: 'c' }
			]
		},
		{ id: 'auuu465fd4g', type: 'color', text: 'Une couleur' },
	] } );
	refreshTabs();
}, 500 );*/

// affichage des proprietes d'un projet
$( document ).on( "click", "#properties_project", function( e ) {

	// creation du formulaire
	let oData = [ { 'name': 'name', 'title': 'Titre', 'value': oInfoProject[ 'name' ], 'type': 'string' },
		{ 'name': 'desc', 'title': 'Description', 'value': oInfoProject[ 'desc' ], 'type': 'text' }
	];

	// pour les proprietes du modele
	for( var i=0; i<oModel[ "properties" ].length; i++ ){
		let oProperty = oModel[ "properties" ][ i ];
		oProperty[ 'name' ] = 'prop-' + oProperty[ 'id' ];
		oProperty[ 'title' ] = oProperty[ 'text' ];

		// determine si il y a une valeur enregistree sur ce modele
		if( oPropertiesProject[ oProperty[ 'id' ] ] !== undefined ){
			oProperty[ 'value' ] = oPropertiesProject[ oProperty[ 'id' ] ];
		}

		oData.push( oProperty );
	}

	modalShowForm( 'Propriétés du projet', 'Valider les modifications', function( oResults ){

		// recuperation de proprietes
		oInfoProject[ 'name' ] = oResults[ 'name' ];
		oInfoProject[ 'desc' ] = oResults[ 'desc' ];
		for( var i=0; i<oModel[ "properties" ].length; i++ ){
			let oProperty = oModel[ "properties" ][ i ];
			oPropertiesProject[ oProperty[ 'id' ] ] = oResults[ 'prop-' + oProperty[ 'id' ] ];
		}

		modelSaveProjectModel( getUrlParameter( 'project' ), { 'name': oInfoProject[ 'name' ], 'desc': oInfoProject[ 'desc' ], 'properties': oPropertiesProject }, oNodes );
		return true;


	}, 'Annuler', null, oData );
} );



// mise a jour d'un onglet
function updateTab( tab ){

	console.log( 'updateTab' );
	console.log( tab );

}

// fonction d'ajout sur le menu contextuel
function contextMenuAdd( oMenu ){
	console.log( 'contextMenuAdd iiiiiiiiiiiiiiiiiiiiiiiii' );
	console.log( oMenu );

	// saisie du nom
	modalShowInput( 'Nouvel élément : ' + oMenu[ 'item' ][ 'text' ], 'Oui', function( sResult ){

		// si pas de contenu
		if( oMenu[ 'item' ][ 'items' ] == undefined ){

			// ajout de l'element
			nodeAddNode( oMenu[ 'parent' ][ 'id' ], sResult, oMenu[ 'item' ], null );

			// enregistrement du projet
			modelSaveProjectModel( getUrlParameter( 'project' ), { 'name': oInfoProject[ 'name' ], 'desc': oInfoProject[ 'desc' ], 'properties': oPropertiesProject }, oNodes );

			return;
		}

		// saisie du contenu de l'element
		var oTab = { id: generate_uuidv4(), text: sResult, state: 'new', form: oMenu[ 'item' ][ 'items' ], options: { parent: oMenu[ 'parent' ] }, eOnSave: function( tab ){

			var oData = [];
			for( var i=0; i<tab.form.length; i++ ){
				oData.push( { id: tab.form[ i ].id, value: tab.form[ i ].value } )
			}

			// ajout de l'element
			nodeAddNode( oMenu[ 'parent' ][ 'id' ], sResult, oMenu[ 'item' ], oData );

			// enregistrement du projet
			modelSaveProjectModel( getUrlParameter( 'project' ), { 'name': oInfoProject[ 'name' ], 'desc': oInfoProject[ 'desc' ], 'properties': oPropertiesProject }, oNodes );

			// remplace l'evenement eOnSave de l'onglet pour celui de la mise a jour
			tab.eOnSave = updateTab;
			
		}, eOnCancel: function( tab ){

		} };

		tabAddTab( oTab );


		console.log( oMenu );
		console.log( sResult );
	}, 'Non' );
}

// renommer un element
function contextMenuRename( oItem ){

	// saisie du nouveau nom
	modalShowInput( 'Nouveau nom', 'Renommer', function( sResult ){

		if( sResult.trim() == '' ){
			return;
		}
		let oNode = nodeGetNode( oItem[ 'id' ] );
		oNode.text = sResult.trim();
		nodeUpdateNode( oNode );

		// enregistrement du projet
		modelSaveProjectModel( getUrlParameter( 'project' ), { 'name': oInfoProject[ 'name' ], 'desc': oInfoProject[ 'desc' ], 'properties': oPropertiesProject }, oNodes );

	}, 'Annuler', undefined , oItem[ 'text' ] );
}

// suppression d'un noeud
function contextMenuDel( oItem ){
	modalShowQuery( 'Supprimer un élément', 'Voulez vous vraiment supprimer l\' élément <b>' + oItem[ 'text' ] + '</b> ainsi que ses enfants ?', 'Oui', function(){
		
		// supprime le noeud
		nodeDeleteNode( oItem[ 'id' ] );

		// enregistrement du projet
		modelSaveProjectModel( getUrlParameter( 'project' ), { 'name': oInfoProject[ 'name' ], 'desc': oInfoProject[ 'desc' ], 'properties': oPropertiesProject }, oNodes );

	}, 'Non' );
}

$.contextMenu({
	selector: '.jstree-node', 
	callback: function(key, options) {
		var m = "clicked: " + key;
		console.log( '---------------------------------' );
		console.log( key );
		console.log( options );
		window.console && console.log(m) || alert(m);
	},
	//items: {
	//	"edit": {name: "Edit", icon: "edit"}
		/*"cut": {name: "Cut", icon: "cut"},
		"copy": {name: "Copy", icon: "copy",
			items: {
				mySubmenu: {
					name:"Command 1",
					callback:function(key, opt){
						alert("Clicked on " + key);
					}
				}
			}
		},
		"paste": {name: "Paste", icon: "paste"},
		"delete": {name: "Delete", icon: "delete"},
		"sep1": "---------",
		"quit": {name: "Quit", icon: function(){
			return 'context-menu-icon context-menu-icon-quit';
		}}*/
	//},
	build: function($triggerElement, e){

		// determine le menu
		var oItems = {};

		// recupere le noeud concerne
		var id = $( $triggerElement ).attr( 'id' );
		var oNode = nodeGetNode( id );

		// determine les types d'enfants du noeud
		var oChildsType = [];
		do{
			if( oNode.li_attr[ 'type' ] != undefined ){

				// recupere l'element du modele correspondant
				var oModelItem = modelGetElementById( oNode.li_attr[ 'type' ] );
				if( oModelItem != null && oModelItem[ 'children-type' ] != undefined && oModelItem[ 'children-type' ].length > 0 ){
					oChildsType = oModelItem[ 'children-type' ];
					break;
				}
			}

			if( oNode.li_attr[ 'children-type' ] != undefined && oNode.li_attr[ 'children-type' ].length > 0 ){
				oChildsType = oNode.li_attr[ 'children-type' ];
			}

		}while( false );

		// si il y a possibilite de creer des enfants
		if( oChildsType.length > 0 ){

			var oSubItems = {};

			for( var i=0; i<oChildsType.length; i++ ){

				var sIdChildModel = oChildsType[ i ];
				var oModelItem = modelGetElementById( sIdChildModel );
				if( oModelItem == null ){
					console.error( 'Erreur sur le chargement d\'un element du modele' );
					console.error( sIdChildModel );
					return;
				}

				var oResultAdd = {}
				oResultAdd[ 'parent' ] = Object.assign( {}, oNode );

				// mise en place du click-droit "ajouter" avec le parent et l'element cible a creer
				oSubItems[ oModelItem[ 'id' ] ] = { name: oModelItem[ 'text' ], callback: function( key, options ){

					oResultAdd[ 'item' ] = modelGetElementById( key );
					contextMenuAdd( oResultAdd ) }
				};

				// si il y a une icone
				if( oModelItem[ 'icon' ] != undefined ){
					oSubItems[ oModelItem[ 'id' ] ][ 'icon' ] = 'fas ' + oModelItem[ 'icon' ];
				}

			}
			oItems[ 'add-element ' ] =  {name: "Ajouter", icon: "fas fa-solid fa-plus-circle", items: oSubItems, state: { disabled: oSubItems.length == 0 } };
		}

		// si l'element peut etre supprime
		if( oNode.li_attr[ 'readonly' ] == undefined || !oNode.li_attr[ 'readonly' ] ){
			oItems[ 'rename-element ' ] =  {name: "Renommer", callback: function(){ contextMenuRename( oNode ) }, icon: "fas a-solid fa-pen" };
			oItems[ 'del-element ' ] =  {name: "Supprimer", callback: function(){ contextMenuDel( oNode ) }, icon: "fas fa-solid fa-eraser" };
		}

		/*console.log( oNode );
		console.log( oItems );*/

		return {
			callback: function(){},
			items: oItems
		};
	}
});

// selection d'un noeud
$( document ).on( "click", ".jstree-node", function( e ) {
	var sIdNode = $( this ).attr( 'id' );
	var oNode = nodeGetNode( sIdNode );
	var oParent = nodeGetParent( sIdNode );
	oSelectNode = oNode;

	// ne pas propager l'evenement vers le parent
	e.stopPropagation();
	
	// determine si il y a des elements au dessus et au dessous
	// si il y a plusieurs noeud du meme type au niveau du parent
	var iCountUp = 0;
	var iCountDown = 0;
	var bIdPass = false;
	if( oParent != null ){
		for( var i=0; i<oParent.children.length; i++){
			if( oParent.children[ i ].li_attr[ 'type' ] != oNode.li_attr[ 'type' ] ){
				continue;
			}
			if( oParent.children[ i ].id == sIdNode ){
				bIdPass = true;
			}else if( bIdPass ){
				iCountDown++;
			}else{
				iCountUp++;
			}
		}
	}

	var oModelItem = modelGetElementById( oNode.li_attr[ 'type' ] );
	var bMove = oModelItem != null && oModelItem[ 'move-on-parent' ] != undefined && oModelItem[ 'move-on-parent' ];

	// activation/desactivation des boutons
	if( bMove && iCountDown > 0 ){
		$( '#btn-down' ).removeClass( "disabled" );
	}else{
		$( '#btn-down' ).addClass( "disabled" );
	}
	if( bMove && iCountUp > 0 ){
		$( '#btn-up' ).removeClass( "disabled" );
	}else{
		$( '#btn-up' ).addClass( "disabled" );
	}
} );

// deplacement d'un noeud vers le haut
$( document ).on( "click", "#btn-up", function( e ) {
	

	var oParent = nodeGetParent( oSelectNode.id );
	for( var i=0; i<oParent.children.length; i++){

	}

} );

// deplacement d'un noeud vers le bas
$( document ).on( "click", "#btn-down", function( e ) {

} );

// ouverture d'un noeud sur au double click
$( document ).on( "dblclick", ".jstree-node", function( e ) {
	var sIdNode = $( this ).attr( 'id' );
	var oNode = nodeGetNode( sIdNode );

	// ne pas propager l'evenement vers le parent
	e.stopPropagation();

	// determine si l'element a des proprietes
	if( oNode[ 'li_attr' ][ 'items' ] == undefined || oNode[ 'li_attr' ][ 'items' ].length == 0 ){
		return;
	}

	// determine si un tab existe deja
	if( tabFocusIfExist( sIdNode ) ){
		return;
	}

	// determine le formulaire
	var oForm = nodeNode2Form( oNode );

	// nouvelle onglet en mode "view"
	tabAddTab( { id: sIdNode, text: oNode.text, state: 'view', form: oForm, focus: true, eOnSave: function( tab ){

		var oData = [];
		for( var i=0; i<tab.form.length; i++ ){
			oData.push( { id: tab.form[ i ].id, value: tab.form[ i ].value } )
		}

		// mise a jour des informations du noeud
		oNode[ 'li_attr' ][ 'items' ] = oData;

		// enregistrement du projet
		modelSaveProjectModel( getUrlParameter( 'project' ), { 'name': oInfoProject[ 'name' ], 'desc': oInfoProject[ 'desc' ], 'properties': oPropertiesProject }, oNodes );
		
	}, eOnCancel: function( tab ){

	} } );

} );

$(document).on("contextmenu", ".jstree-node", function(e) {
	e.preventDefault();
  
  // Mise à jour du contenu du menu
  $.contextMenu("update", {
	"copier": {name: "Copier", icon: "fa-copy"},
	"coller": {name: "Coller", icon: "fa-paste"},
	"sep1": "---------",
	"sousmenu": {
	  name: "Sous-menu",
	  icon: "fa-cut",
	  items: {
		"sousmenu1": {name: "Sous-menu 1 modifié", icon: "fa-file"},
		"sousmenu2": {name: "Sous-menu 2 modifié", icon: "fa-folder"}
	  }
	},
	"nouveau": {name: "Nouveau", icon: "fa-plus"}
  });

  // Affichage du menu contextuel
  $(this).trigger("mousedown");
});

// fermeture du projet
$('#close_project').on('click', function(e){
	modalShowQuery( 'Fermeture du projet', 'Voulez vous fermer ce projet ?', 'Oui', function(){
		window.location.href = 'index.html';
	}, 'Non' );
});