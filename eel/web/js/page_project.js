//$.jstree.defaults.core.themes.dir = "css/themes";
/*
https://fontawesome.com/search?o=r&m=free
https://www.jstree.com/docs/json/
*/

$( document ).ready( function(){
	fullScreen();
} );

// chargement da la navbar
eel.open_project( getUrlParameter( 'project' ) )( function( data ){

	// alimente le type
	$( '#project_title' ).html( data[ 'model' ][ 'title' ] );

	// recupere le modeles de donnees
	oModel = data[ 'model' ][ 'elements' ];

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
window.setTimeout( function(){
	oTabs.push( { id: 's6d4fsd65f', text: 'Nouveau', state: 'new', form: [
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
}, 500 );



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
			modelSaveProjectModel( getUrlParameter( 'project' ), oNodes );

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
			modelSaveProjectModel( getUrlParameter( 'project' ), oNodes );

			// remplace l'evenement eOnSave de l'onglet pour celui de la mise a jour
			tab.eOnSave = updateTab;
			
		}, eOnCancel: function( tab ){

		} };

		tabAddTab( oTab );


		console.log( oMenu );
		console.log( sResult );
	}, 'Non' );
}

function contextMenuDel( oItem ){
	console.log( 'contextMenuDel iiiiiiiiiiiiiiiiiiiiiiiii' );
	console.log( oItem );
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
		if( oNode.li_attr[ 'type' ] != undefined ){

			// recupere l'element du modele correspondant
			var oModelItem = modelGetElementById( oNode.li_attr[ 'type' ] );
			if( oModelItem[ 'children-type' ] != undefined && oModelItem[ 'children-type' ].length > 0 ){
				oChildsType = oModelItem[ 'children-type' ];
			}


		}
		else if( oNode.li_attr[ 'children-type' ] != undefined && oNode.li_attr[ 'children-type' ].length > 0 ){
			oChildsType = oNode.li_attr[ 'children-type' ];
		}



		// si il y a possibilite de creer des enfants
		if( oChildsType.length > 0 ){

			var oSubItems = {};

			for( var i=0; i<oChildsType.length; i++ ){

				var sIdChildModel = oChildsType[ i ];
				var oModelItem = modelGetElementById( sIdChildModel );

				var oResultAdd = {}
				oResultAdd[ 'parent' ] = Object.assign( {}, oNode );

				// mise en place du click-droit "ajouter" avec le parent et l'element cible a creer
				oSubItems[ oModelItem[ 'id' ] ] = { name: oModelItem[ 'text' ], callback: function( key, options ){

					oResultAdd[ 'item' ] = modelGetElementById( key );
					contextMenuAdd( oResultAdd ) }
				};

			}
			oItems[ 'add-element ' ] =  {name: "Ajouter", icon: "paste", items: oSubItems, state: { disabled: oSubItems.length == 0 } };
		}

		// si l'element peut etre supprime
		if( oNode.li_attr[ 'readonly' ] == undefined || !oNode.li_attr[ 'readonly' ] ){
			oItems[ 'del-element ' ] =  {name: "Supprimer", callback: function(){ contextMenuDel( oNode ) }, icon: "paste" };
		}

		console.log( oNode );
		console.log( oItems );

		return {
			callback: function(){},
			items: oItems
		};
	}
});

// ouverture d'un noeud sur au double click
$( document ).on( "dblclick", ".jstree-node", function( e ) {
	var sIdNode = $( this ).attr( 'id' );
	var oNode = nodeGetNode( sIdNode );

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
		modelSaveProjectModel( getUrlParameter( 'project' ), oNodes );
		
	}, eOnCancel: function( tab ){

	} } );

	// ne pas propager l'evenement vers le parent
	e.stopPropagation();
} );

/*$( document ).on( "click", ".jstree-node", function() {
	console.log('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu');
	console.log('click', this);
} );*/


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



/*
$('#tree').jstree({
	"core" : {
		'data' : [
	   'Simple root node',
	   {
		 'text' : 'Root node 2',
		 'icon': 'fa-solid fa-tree',
		 'state' : {
		   'opened' : true,
		   'selected' : true
		 },
		 'children' : [
		   { 'text' : 'Child 1' },
		   'Child 2',
		   { 'text' : 'Child gsdfg dsfg sdfg' },
		 ]
	  }
	]
	}
});*/