//$.jstree.defaults.core.themes.dir = "css/themes";
/*
https://fontawesome.com/search?o=r&m=free
https://www.jstree.com/docs/json/
*/

// modeles de donnees
var oModel = [];

// reference vers les noeuds
var oNodes = [];

// reference des onglets
var oTabs = [];

// recherche un noeud en fonction de son id
function getNode( id, _nodes ){
	if( _nodes == undefined ){
		_nodes = oNodes;
	}
	for( var i=0; i<oNodes.length; i++ ){
		if( oNodes[ i ].id == id ){
			return oNodes[ i ];
		}else if( oNodes[ i ].children > 0 ){
			var oNode = getNode( id, oNodes[ i ].children );
			if( oNode != null ){
				return oNode;
			}
		}
	}
	return null;
}

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





function refreshTabs(){
	$( '#col_right' ).modTab( { tabs: oTabs } );
}

/*





*/

oTabs.push( { id: 's6d4fsd65f', text: 'Nouveau', state: 'new', form: [
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
oTabs.push( { id: 's6d4fsd65fd', text: 'Edition', state: 'edit', form: [] } );
oTabs.push( { id: 's6d4fsd65fcccd', text: 'un autre', state: 'view', form: [
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

$.contextMenu({
	selector: '.jstree-node', 
	callback: function(key, options) {
		var m = "clicked: " + key;
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
		var oNode = getNode( id );

		// si il y a possibilite de creer des enfants
		if( oNode.li_attr[ 'children-type' ] != undefined && oNode.li_attr[ 'children-type' ].length > 0 ){
			var oSubItems = {};

			for( var i=0; i<oNode.li_attr[ 'children-type' ].length; i++ ){

				var sIdChildModel = oNode.li_attr[ 'children-type' ][ i ];
				for( var a=0; a<oModel.length; a++ ){
					if( oModel[ a ][ 'id' ] == sIdChildModel ){
						oSubItems[ oModel[ a ][ 'id' ] ] = { name: oModel[ a ][ 'text' ], li_attr: { action: 'add-element', 'element': oModel[ a ][ 'id' ] } }
					}
				}

				//var sKeyAdd = oNode.li_attr[ 'childre-type' ]
			}
			oItems[ 'add-element ' ] =  {name: "Ajouter", icon: "paste", items: oSubItems, state: { disabled: oSubItems.length == 0 } };
		}

		// si l'element peut etre supprime
		if( oNode.li_attr[ 'readonly' ] == undefined || !oNode.li_attr[ 'readonly' ] ){
			oItems[ 'del-element ' ] =  {name: "Supprimer", icon: "paste", li_attr: { action: 'del-element' } };
		}

		console.log( oNode );
		console.log( oItems );

        return {
            callback: function(){},
            items: oItems
        };
    }
});


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
})


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