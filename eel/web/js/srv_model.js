// modeles de donnees
var oModel = [];

// recupere un element du modele par ID
function modelGetElementById( sId ){
	for( var a=0; a<oModel[ 'elements' ].length; a++ ){
		if( oModel[ 'elements' ][ a ][ 'id' ] == sId ){
			return oModel[ 'elements' ][ a ];
		}
	}
	return null;
}

// enregistrement du modele du projet
function modelSaveProjectModel( filename, properties, data, eOnSave ){
	eel.update_project( filename, properties, data )( function( result ){

		console.log( 'js update_project' );
		console.log( result );

		if( eOnSave != undefined ){
			eOnSave();
		}
	} );
}