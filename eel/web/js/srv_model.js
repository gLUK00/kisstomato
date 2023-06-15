// modeles de donnees
var oModel = [];

// recupere un element du modele par ID
function modelGetElementById( sId ){
	for( var a=0; a<oModel.length; a++ ){
		if( oModel[ a ][ 'id' ] == sId ){
			return oModel[ a ];
		}
	}
	return null;
}

// enregistrement du modele du projet
function modelSaveProjectModel( filename, data, eOnSave ){
	eel.update_project( filename, data )( function( result ){

		console.log( 'js update_project' );
		console.log( result );

		if( eOnSave != undefined ){
			eOnSave();
		}
	} );
}