// evenement de prise en charge des boutons de type "save-as"
$( document ).on( "click", ".app-btn-save-as", function(){

	var idTarget = $( this ).attr( 'idtarget' );
	var fileTitle = $( this ).attr( 'filetitle' );
	var fileExt = $( this ).attr( 'fileext' );
	var initialfile = $( this ).attr( 'initialfile' );

	fetch('/api/app/save_as', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ dialog_title_text: fileTitle, ext: fileExt, initialfile_name: initialfile })
	})
	.then(response => {
		if (!response.ok) { return response.json().then(err => { throw new Error(err.message || `HTTP error ${response.status}`); }); }
		return response.json();
	})
	.then(data => {
		if (data.path) {
			$( '#' + idTarget ).val( data.path );
		} else {
			console.error('API /api/app/save_as did not return a path.');
			alert('Erreur: Le chemin du fichier n\'a pas pu être déterminé.');
		}
	})
	.catch(error => {
		console.error('Error calling /api/app/save_as:', error);
		alert('Erreur lors de l_enregistrement du fichier: ' + error.message);
	});

} );

// evenement de prise en charge des boutons de type "set-file"
$( document ).on( "click", ".app-btn-set-file", function(){

	var idTarget = $( this ).attr( 'idtarget' );
	var fileTitle = $( this ).attr( 'filetitle' );
	var fileExt = $( this ).attr( 'fileext' );

	// TODO: Remplacer par une logique de sélection de fichier côté client (ex: <input type="file">).
	// Le backend Flask (/api/app/set_file) attend maintenant que le client fournisse le chemin du fichier.
	// L'ancien appel eel.app_set_file ouvrait une boîte de dialogue native, ce qui n'est plus possible directement avec Flask.
	// Exemple de remplacement (nécessite un <input type="file" id="fileInput" style="display:none;">):
	/*
	const fileInput = document.createElement('input');
	fileInput.type = 'file';
	if (fileExt) { // Note: l'attribut 'accept' est un indice, pas une contrainte stricte
		fileInput.accept = '.' + fileExt.split(',').map(ext => ext.trim()).join(',.');
	}
	fileInput.onchange = e => {
		const file = e.target.files[0];
		if (file) {
			// Pour l'instant, on met juste le nom. Le backend attend un chemin complet si c'est pertinent.
			// Ou, si le backend doit juste connaître le nom et l'extension:
			$( '#' + idTarget ).val( file.name ); 

			// Si vous devez envoyer ce chemin au backend via /api/app/set_file:
			// fetch('/api/app/set_file', {
			// method: 'POST',
			// headers: { 'Content-Type': 'application/json' },
			// body: JSON.stringify({ file_path: file.name, ext: fileExt })
			// })
			// .then(response => response.json())
			// .then(data => { /* ... * });
		}
	};
	fileInput.click();
	*/
	console.warn('La fonctionnalité "set-file" via eel.app_set_file n\'est plus supportée directement. Une implémentation côté client est nécessaire.');
	alert('Fonctionnalité non disponible: la sélection de fichier doit être gérée par le navigateur.');

} );

// evenement de prise en charge des boutons de type "set-dir"
$( document ).on( "click", ".app-btn-set-dir", function(){

	var idTarget = $( this ).attr( 'idtarget' );
	var fileTitle = $( this ).attr( 'filetitle' );

	// TODO: Remplacer par une logique de sélection de répertoire côté client (ex: <input type="file" webkitdirectory>).
	// Le backend Flask (/api/app/set_dir) attend maintenant que le client fournisse le chemin du répertoire.
	// L'ancien appel eel.app_set_dir ouvrait une boîte de dialogue native.
	// spinnerShow(); // Peut être conservé si l'opération client est asynchrone
	/*
	const dirInput = document.createElement('input');
	dirInput.type = 'file';
	dirInput.webkitdirectory = true;
	dirInput.onchange = e => {
		const files = e.target.files;
		if (files.length > 0) {
			// Le chemin est généralement le chemin du premier fichier relatif au répertoire sélectionné
			// ou le nom du répertoire lui-même, selon le navigateur.
			// Pour obtenir un chemin de répertoire, il faut souvent une astuce ou se contenter du nom.
			let dirPath = files[0].webkitRelativePath.split('/')[0];
			$( '#' + idTarget ).val( dirPath );
		}
		// spinnerHide();
	};
	dirInput.click();
	*/
	console.warn('La fonctionnalité "set-dir" via eel.app_set_dir n\'est plus supportée directement. Une implémentation côté client est nécessaire.');
	alert('Fonctionnalité non disponible: la sélection de répertoire doit être gérée par le navigateur.');
	// spinnerHide(); // Assurez-vous qu'il est appelé si spinnerShow l'est.

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