// chargement du fichier javascript
_pluginFields = {};
function pluginLoadFieldJS( sField, fCode, oField ){
	if( _pluginFields[ sField ] != undefined ){
		fCode( sIdField, oField );
		return;
	}
	
	// chargement du fichier javascript
	eel.get_javascript_field( sField )( function( sJsCode ){
		eval( sJsCode );
		_pluginFields[ sField ] = sJsCode != '';
		fCode( sIdField, oField );
	} );
}

// generation du visuel (edition)
function pluginFieldGetHtml( sIdField, oField ){


	let fCode = function( sIdField, oField  ){
		eval( 'pluginFieldGetHtml_qrcode( sIdField, oField )' );
	};

	get_javascript_field( sIdField, fCode, oField );
}

// passage du visuel en mode "view"
function pluginFieldSetView( sIdField, oField ){

}

// recuperation de la valeur en fonction du visuel
function pluginFieldForm2val( sIdField, oField ){

}