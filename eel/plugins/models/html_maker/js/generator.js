
//click sur la generation de code
$( document ).on( "click", "#gen-code", function() {

	var oFormItemTemp = { 'name': 'dir-temp', 'type': 'set-dir', 'title': 'Répertoire temporaire' };
	var oFormItemOut = { 'name': 'dir-out', 'type': 'set-dir', 'title': 'Répertoire de sortie' };
	var oFormItemCheckbox = { 'name': 'save-params', 'type': 'checkbox', 'title': 'Mémorisation des paramètres de génération' };
	if( localStorage.getItem( 'html-generator-dir-temp' ) !== null ){
		oFormItemTemp[ 'value' ] = localStorage.getItem( 'html-generator-dir-temp' );
	}
	if( localStorage.getItem( 'html-generator-dir-out' ) !== null ){
		oFormItemOut[ 'value' ] = localStorage.getItem( 'html-generator-dir-out' );
	}
	oFormItemCheckbox[ 'value' ] = localStorage.getItem( 'html-generator-save-params' ) !== null && localStorage.getItem( 'html-generator-save-params' );

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
			localStorage.setItem( 'html-generator-dir-temp', oData[ 'dir-temp' ].trim() );
			localStorage.setItem( 'html-generator-dir-out', oData[ 'dir-out' ].trim() );
			localStorage.setItem( 'html-generator-save-params', true );
		}else{
			localStorage.setItem( 'html-generator-dir-temp', '' );
			localStorage.setItem( 'html-generator-dir-out', '' );
			localStorage.setItem( 'html-generator-save-params', false );
		}

		oData[ 'file' ] = getUrlParameter( 'project' );
		eel.plugin_exec_method_model( oInfoProject[ 'model' ], 'generation', 'generateHtmlCode', oData )( function( result ){

			// affichage du rapport de generation, asynchrone
			console.log( 'js generateHtmlCode aaaa' );
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