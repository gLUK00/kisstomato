// enregistrement de la fenetre
eel.expose(close_all);
function close_all(){
	window.close();
}

// evenement de prise en charge des boutons de type "save-as"
$( document ).on( "click", ".app-btn-save-as", function(){

	var idTarget = $( this ).attr( 'idtarget' );
	var fileTitle = $( this ).attr( 'filetitle' );
	var fileExt = $( this ).attr( 'fileext' );
	var initialfile = $( this ).attr( 'initialfile' );

	eel.app_save( fileTitle, fileExt, initialfile )( function( path ){
		$( '#' + idTarget ).val( path );
	} );

} );

function makeid(length) {
	let result = '';
	const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
	const charactersLength = characters.length;
	let counter = 0;
	while (counter < length) {
		result += characters.charAt(Math.floor(Math.random() * charactersLength));
		counter += 1;
	}
	return result;
}