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

// evenement de prise en charge des boutons de type "set-file"
$( document ).on( "click", ".app-btn-set-file", function(){

	var idTarget = $( this ).attr( 'idtarget' );
	var fileTitle = $( this ).attr( 'filetitle' );
	var fileExt = $( this ).attr( 'fileext' );

	eel.app_set_file( fileTitle, fileExt )( function( path ){
		$( '#' + idTarget ).val( path );
	} );

} );

// evenement de prise en charge des boutons de type "set-dir"
$( document ).on( "click", ".app-btn-set-dir", function(){

	var idTarget = $( this ).attr( 'idtarget' );
	var fileTitle = $( this ).attr( 'filetitle' );

	spinnerShow();
	eel.app_set_dir( fileTitle )( function( path ){
		$( '#' + idTarget ).val( path );
		spinnerHide();
	} );

} );

// redimension de la fenetre en plein ecran
function fullScreen(){
	window.resizeTo( screen.width, screen.height );
}

function makeid(length) {
	if( length == undefined ){
		length = 16;
	}
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

function getUrlParameter(sParam) {
	var sPageURL = window.location.search.substring(1),
		sURLVariables = sPageURL.split('&'),
		sParameterName,
		i;

	for (i = 0; i < sURLVariables.length; i++) {
		sParameterName = sURLVariables[i].split('=');

		if (sParameterName[0] === sParam) {
			return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
		}
	}
	return false;
};

function generate_uuidv4() {
	var dt = new Date().getTime();
	return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,
		function( c ) {
			var rnd = Math.random() * 16;//random number in range 0 to 16
			rnd = (dt + rnd)%16 | 0;
			dt = Math.floor(dt/16);
			return (c === 'x' ? rnd : (rnd & 0x3 | 0x8)).toString(16);
		});
}

// gestion du spinner de chargement
$( 'body' ).append( '<div id="spinner" style="display:none !important" class="d-flex justify-content-center"><div class="spinner-border" role="status"><span class="sr-only">Loading...</span></div></div>')
function spinnerShow(){
	$( 'body > div' ).each( function(){
		if( $( this ).attr( 'id' ) == 'spinner' ){
			$( this ).show();
		}else{
			$( this ).hide();
		}
	} );
}
function spinnerHide(){
	$( 'body > div' ).each( function(){
		if( $( this ).attr( 'id' ) == 'spinner' ){
			$( this ).hide().attr("style", "display: none !important");
		}else{
			$( this ).show();
		}
	} );
}