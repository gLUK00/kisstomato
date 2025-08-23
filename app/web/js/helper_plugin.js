// generation du visuel (edition)
function pluginFieldGetHtml( sIdField, oField ){
	return window[ 'pluginFieldGetHtml_' + oField.type ]( sIdField, oField );
}

// apres la generation du HTML
function pluginFieldAfterHtml( sIdField, oField ){
	return window[ 'pluginFieldAfterHtml_' + oField.type ]( sIdField, oField );
}

// passage du visuel en mode "view"
function pluginFieldSetView( sIdField, oField ){
	return window[ 'pluginFieldSetView_' + oField.type ]( sIdField, oField );
}

// recuperation de la valeur en fonction du visuel
function pluginFieldForm2val( sIdField, oField ){
	return window[ 'pluginFieldForm2val_' + oField.type ]( sIdField, oField );
}