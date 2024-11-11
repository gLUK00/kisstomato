
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
		console.log( '--> generation' );

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
		eel.plugin_exec_method_model( oInfoProject[ 'model' ], 'generation', 'generateFlaskCode', oData )( function( result ){

			// affichage du rapport de generation, asynchrone
			console.log( 'plugin_exec_method_model js generateFlaskCode aaaa' );
			console.log( oData );
			console.log( result );

			//alert( result );

			modalShowMessage( result );
		} );

		return true;
	}, 'Annuler', undefined, [
		oFormItemTemp,
		oFormItemOut,
		oFormItemCheckbox
	] );
	console.log( 'yyyyy' );
} );