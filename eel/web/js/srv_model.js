// modeles de donnees
var oModel = [];

// recupere un element du modele par ID
function modelGetElementById( sId ){
	for( var a=0; a<oModel[ 'elements' ].length; a++ ){
		if( oModel[ 'elements' ][ a ][ 'id' ] == sId ){
			return oModel[ 'elements' ][ a ];
		}
	}
	return null;
}

// enregistrement du modele du projet
function modelSaveProjectModel( filename, properties, data, eOnSave ){
	fetch('/api/project/update', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ filename: filename, properties: properties, data: data })
	})
	.then(response => {
		if (!response.ok) {
			// Essayer de lire le message d'erreur du corps JSON si possible
			return response.json().then(err => { 
				throw new Error(err.message || `HTTP error ${response.status}`); 
			});
		}
		return response.json();
	})
	.then(result => {
		if (eOnSave !== undefined) {
			eOnSave(result);
		}
	})
	.catch(error => {
		console.error('Error updating project via /api/project/update:', error);
		// Peut-être appeler eOnSave avec une indication d'erreur ou afficher une alerte
		if (eOnSave !== undefined) {
			eOnSave({ success: false, message: error.message }); // ou un format d'erreur convenu
		}
		alert('Erreur lors de la mise à jour du projet: ' + error.message);
	});
}