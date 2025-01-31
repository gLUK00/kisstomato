/*
	interface principale
*/

// kisstomato-js-front-a-start-user-code-kisstomato
// kisstomato-js-front-a-stop-user-code-kisstomato

// --------------------------------------------------------------------------
// Section : windows_e
/* évènement window de redimensionnent */
// --------------------------------------------------------------------------

// kisstomato-section-windows_e-start-user-code-kisstomato
// kisstomato-section-windows_e-stop-user-code-kisstomato

/* produit une addition */
// Arguments :
// - a : number : (obligatoire) valeur A
// - b : number : (obligatoire) valeur B
function caculer(a, b){
	let oResult = null;

	// kisstomato-function-caculer-start-user-code-kisstomato
	// kisstomato-function-caculer-stop-user-code-kisstomato

	return oResult;
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
	if( localStorage.getItem( 'plugin-flask-generator-dir-temp' ) !== null ){
		oFormItemTemp[ 'value' ] = localStorage.getItem( 'plugin-flask-generator-dir-temp' );
	}
	if( localStorage.getItem( 'plugin-flask-generator-dir-out' ) !== null ){
		oFormItemOut[ 'value' ] = localStorage.getItem( 'plugin-flask-generator-dir-out' );
	}
	oFormItemCheckbox[ 'value' ] = localStorage.getItem( 'plugin-flask-generator-save-params' ) !== null && localStorage.getItem( 'kisstomato-generator-save-params' );

	modalShowForm( 'Génération du code de l\'application Flask', 'Générer', function( oData ){

		if( oData[ 'dir-temp' ].trim() == '' ){
			return 'Le répertoire temporaire ne peut être vide !';
		}
		if( oData[ 'dir-out' ].trim() == '' ){
			return 'Le répertoire de sortie ne peut être vide !';
		}

		// memorisation des chemins
		if( oData[ 'save-params' ] ){
			localStorage.setItem( 'plugin-flask-generator-dir-temp', oData[ 'dir-temp' ].trim() );
			localStorage.setItem( 'plugin-flask-generator-dir-out', oData[ 'dir-out' ].trim() );
			localStorage.setItem( 'plugin-flask-generator-save-params', true );
		}else{
			localStorage.setItem( 'plugin-flask-generator-dir-temp', '' );
			localStorage.setItem( 'plugin-flask-generator-dir-out', '' );
			localStorage.setItem( 'plugin-flask-generator-save-params', false );
		}

		oData[ 'file' ] = getUrlParameter( 'project' );
		eel.plugin_exec_method_model( oInfoProject[ 'model' ], 'generation', 'generateFlaskCode', oData )( function( result ){

			// affichage du rapport de generation, asynchrone
			modalShowMessage( result.replaceAll( '\n', '<br/>' ) );
		} );

		return true;
	}, 'Annuler', undefined, [
		oFormItemTemp,
		oFormItemOut,
		oFormItemCheckbox
	] );

	// kisstomato-on-clickGenCode-stop-user-code-kisstomato
} );

// kisstomato-js-front-b-start-user-code-kisstomato
// kisstomato-js-front-b-stop-user-code-kisstomato