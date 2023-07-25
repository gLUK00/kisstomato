
//click sur la generation de code
$( document ).on( "click", "#gen-code", function() {

	modalShowForm( 'Génération de code', 'Générer', function( oData ){
		console.log( '--> generation' );

		oData[ 'file' ] = getUrlParameter( 'project' );
		eel.plugin_exec_method_model( oInfoProject[ 'model' ], 'generation', 'generateHtmlCode', oData )( function( result ){

			// affichage du rapport de generation, asynchrone
			console.log( 'js generateHtmlCode aaaa' );
			console.log( oData );
			console.log( result );

			alert( result );
		} );

		return true;
	}, 'Annuler', undefined, [
		{ 'name': 'dir-src', 'type': 'set-dir', 'title': 'Répertoire à fusionner' },
		{ 'name': 'dir-out', 'type': 'set-dir', 'title': 'Répertoire de sortie' },
		{ 'name': 'save-params', 'type': 'checkbox', 'title': 'Mémorisation des paramètres de génération' },
	] );
	console.log( 'yyyyy' );
} );