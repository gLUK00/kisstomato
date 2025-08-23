// sur l'affichage d'un noeud de type "item"
window[ 'formShowItemTypeObject' ] = function( oForm ){

    for( var a=0; a<oForm.length; a++ ){
        if( oForm[ a ].id == 'type' ){

            return oForm[ a ].value == 'object';
        }
    }

    return false;
}

/* lors du chargement */
$( document ).ready( function(){
	// kisstomato-ready-chargement-start-user-code-kisstomato

	// ajout du bouton de generation de code
	$( '#navbar-options' ).append( '<li class="nav-item">' +
		'<button class="btn btn-outline-success" id="gen-code"><i class="fa-solid fa-certificate"></i>&nbsp; Générer le code de l\'application</button>' +
	'</li>' );

	// kisstomato-ready-chargement-stop-user-code-kisstomato
} );

/* click sur la génération de code */
$( document ).on( "click", "#gen-code", function() {
	// kisstomato-on-clickGenCode-start-user-code-kisstomato

	var oFormItemTemp = { 'name': 'dir-temp', 'type': 'set-dir', 'title': 'Répertoire temporaire' };
	var oFormItemOut = { 'name': 'dir-out', 'type': 'set-dir', 'title': 'Répertoire de sortie' };
	var oFormItemCheckbox = { 'name': 'save-params', 'type': 'checkbox', 'title': 'Mémorisation des paramètres de génération' };
	if( localStorage.getItem( 'plugin-kisstomato-generator-dir-temp' ) !== null ){
		oFormItemTemp[ 'value' ] = localStorage.getItem( 'plugin-kisstomato-generator-dir-temp' );
	}
	if( localStorage.getItem( 'plugin-kisstomato-generator-dir-out' ) !== null ){
		oFormItemOut[ 'value' ] = localStorage.getItem( 'plugin-kisstomato-generator-dir-out' );
	}
	oFormItemCheckbox[ 'value' ] = localStorage.getItem( 'plugin-kisstomato-generator-save-params' ) !== null && localStorage.getItem( 'kisstomato-generator-save-params' );

	modalShowForm( 'Génération du code de l\'application Flask', 'Générer', function( oData ){

		if( oData[ 'dir-temp' ].trim() == '' ){
			return 'Le répertoire temporaire ne peut être vide !';
		}
		if( oData[ 'dir-out' ].trim() == '' ){
			return 'Le répertoire de sortie ne peut être vide !';
		}

		// memorisation des chemins
		if( oData[ 'save-params' ] ){
			localStorage.setItem( 'plugin-kisstomato-generator-dir-temp', oData[ 'dir-temp' ].trim() );
			localStorage.setItem( 'plugin-kisstomato-generator-dir-out', oData[ 'dir-out' ].trim() );
			localStorage.setItem( 'plugin-kisstomato-generator-save-params', true );
		}else{
			localStorage.setItem( 'plugin-kisstomato-generator-dir-temp', '' );
			localStorage.setItem( 'plugin-kisstomato-generator-dir-out', '' );
			localStorage.setItem( 'plugin-kisstomato-generator-save-params', false );
		}

		oData[ 'file' ] = getUrlParameter( 'project' );
		fetch('/api/plugin/exec_method_model', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				model: oInfoProject['model'],
				module: 'generation',
				method: 'generateKisstomatoCode',
				data: oData
			})
		})
		.then(response => {
			if (!response.ok) {
				return response.json().then(err => { 
					throw new Error(err.message || `HTTP error ${response.status}`); 
				});
			}
			return response.json();
		})
		.then(data => {
			console.log('Réponse du plugin:', JSON.stringify(data, null, 2));
			// Le backend retourne { "status": "success", "result": sResult } ou une erreur
			if (data.status === 'success' && data.result !== undefined) {
				modalShowMessage(data.result.toString().replaceAll('\n', '<br/>'));
			} else if (data.message) {
				modalShowMessage('Erreur du plugin: ' + data.message.toString().replaceAll('\n', '<br/>'), 'error');
			} else {
				modalShowMessage('Réponse inattendue du serveur après l\'exécution du plugin.', 'error');
			}
		})
		.catch(error => {
			console.error('Error calling /api/plugin/exec_method_model:', error);
			modalShowMessage('Erreur lors de l_appel au plugin: ' + error.message, 'error');
		});

		return true;
	}, 'Annuler', undefined, [
		oFormItemTemp,
		oFormItemOut,
		oFormItemCheckbox
	] );

	// kisstomato-on-clickGenCode-stop-user-code-kisstomato
} );