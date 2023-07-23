
//click sur la generation de code
$( document ).on( "click", "#gen-code", function() {

	modalShowForm( 'Génération de code', 'Générer', function( oData ){
		console.log( '--> generation' );




		// affichage du rapport de generation, asynchrone



		return true;
	}, 'Annuler', undefined, [
		{ 'name': 'dir-src', 'type': 'set-dir', 'title': 'Répertoire à fusionner' },
		{ 'name': 'dir-out', 'type': 'set-dir', 'title': 'Répertoire de sortie' },
		{ 'name': 'save-params', 'type': 'checkbox', 'title': 'Mémorisation des paramètres de génération' },
	] );
	console.log( 'yyyyy' );
} );