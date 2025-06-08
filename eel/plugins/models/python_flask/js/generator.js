
//click sur la generation de code
$( document ).on( "click", "#gen-code", function() {

	var oFormItemTemp = { 'name': 'dir-temp', 'type': 'set-dir', 'title': 'Répertoire temporaire' };
	var oFormItemOut = { 'name': 'dir-out', 'type': 'set-dir', 'title': 'Répertoire de sortie' };
	var oFormItemCheckbox = { 'name': 'save-params', 'type': 'checkbox', 'title': 'Mémorisation des paramètres de génération' };
	if( localStorage.getItem( 'flask-generator-dir-temp' ) !== null ){
		oFormItemTemp[ 'value' ] = localStorage.getItem( 'flask-generator-dir-temp' );
	}
	if( localStorage.getItem( 'flask-generator-dir-out' ) !== null ){
		oFormItemOut[ 'value' ] = localStorage.getItem( 'flask-generator-dir-out' );
	}
	oFormItemCheckbox[ 'value' ] = localStorage.getItem( 'flask-generator-save-params' ) !== null && localStorage.getItem( 'flask-generator-save-params' );

	modalShowForm( 'Génération de code', 'Générer', function( oData ){

		if( oData[ 'dir-temp' ].trim() == '' ){
			return 'Le répertoire temporaire ne peut être vide !';
		}
		if( oData[ 'dir-out' ].trim() == '' ){
			return 'Le répertoire de sortie ne peut être vide !';
		}

		// memorisation des chemins
		if( oData[ 'save-params' ] ){
			localStorage.setItem( 'flask-generator-dir-temp', oData[ 'dir-temp' ].trim() );
			localStorage.setItem( 'flask-generator-dir-out', oData[ 'dir-out' ].trim() );
			localStorage.setItem( 'flask-generator-save-params', true );
		}else{
			localStorage.setItem( 'flask-generator-dir-temp', '' );
			localStorage.setItem( 'flask-generator-dir-out', '' );
			localStorage.setItem( 'flask-generator-save-params', false );
		}

		oData[ 'file' ] = getUrlParameter( 'project' );
		fetch('/api/plugin/exec_method_model', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				model: oInfoProject['model'],
				module: 'generation',
				method: 'generateFlaskCode',
				data: oData
			})
		})
		.then(response => response.json())
		.then(function(result) {

			// affichage du rapport de generation, asynchrone
			modalShowMessage( result );
		} );

		return true;
	}, 'Annuler', undefined, [
		oFormItemTemp,
		oFormItemOut,
		oFormItemCheckbox
	] );
} );