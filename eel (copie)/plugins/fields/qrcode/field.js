var _oQrCodes = {};

// generation du visuel (edition)
window[ 'pluginFieldGetHtml_qrcode' ] = function( sIdField, oField ){
    if( oField.value == undefined ){
        oField.value = sIdField;
    }
    return '<div id="' + sIdField + '">' +
        '<input type="text" value="' + oField.value + '" class="form-control field_qrcode" style="margin-bottom:5px"/>' +
        '<div id="qrcode_' + sIdField + '"></div>' + 
    '</div>';
}

// execution apres la generation du HTML
window[ 'pluginFieldAfterHtml_qrcode' ] = function( sIdField, oField ){
    _oQrCodes[ sIdField ] = new QRCode( document.getElementById( 'qrcode_' + sIdField ), oField.value );
}

// passage du visuel en mode "view"
window[ 'pluginFieldSetView_qrcode' ] = function( sIdField, oField ){
    $( '#' + sIdField ).find( 'input' ).prop( "disabled", true ).val();
}

// recuperation de la valeur en fonction du visuel
window[ 'pluginFieldForm2val_qrcode' ] = function( sIdField, oField ){
    return $( '#' + sIdField ).find( 'input' ).val();
}

// mise a jour du champ
$( document ).on( "change", ".field_qrcode", function() {
    var sIdField = $( this ).closest( 'div' ).attr( 'id' );
    _oQrCodes[ sIdField ].clear();
    _oQrCodes[ sIdField ].makeCode( $( this ).val() );
} );