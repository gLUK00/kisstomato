$( document ).ready( function(){
	refreshProjects();
} );

// referencement d'un projet
$( document ).on( "click", "#btn-ref-projet", function() {

	modalShowForm( "Référencer un projet existant", "Valider",
		function( oData ){

			// controle du formulaire
			sError = '';
			if( oData[ 'file' ].trim() == '' ){
				sError += '<li>Le nom du fichier ne peut être vide</li>';
			}
			if( sError != '' ){
				return '<ul>' + sError + '</ul>';
			}

			// enregistrement du nouveau projet
			fetch('/api/project/set_file', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ filename: oData['file'].trim(), relatif_path: oData['relatif-path'] })
			})
			.then(response => {
				if (!response.ok) { return response.json().then(err => { throw new Error(err.message || `HTTP error ${response.status}`); }); }
				return response.json();
			})
			.then(data => {
				if (data.status === 'success') {
					refreshProjects();
				} else {
					console.error("Failed to set file project:", data.message);
					alert("Error: " + (data.message || "Could not set file project."));
				}
			})
			.catch(error => {
				console.error('Error setting file project:', error);
				alert("Error: " + error.message);
			});
			
			return true; // Modal closes, fetch handles outcome
		}, "Annuler", null,
		[
			{ 'name': 'file', 'title': 'Fichier du projet', 'type': 'set-file', 'ext': 'json', 'ext-title': 'Fichier Json'},
			{ 'name': 'relatif-path', 'type': 'checkbox', 'title': 'Activer la prise en charge du chemin relatif à KissTomato', 'value': true }
		]
	);
} );

// creation d'un projet
$( document ).on( "click", "#btn-new-projet", function() {

	// recupere tous des types de modeles des plugins
	fetch('/api/model/get_all')
		.then(response => {
			if (!response.ok) { return response.json().then(err => { throw new Error(err.message || `HTTP error ${response.status}`); }); }
			return response.json();
		})
		.then(oModels => {
			modalShowForm( "Nouveau projet", "Enregistrer sous",
				function( oData ){ // fnOk for modalShowForm
					// controle du formulaire
					sError = '';
					if( oData[ 'name' ].trim() == '' ){ sError += '<li>Le nom ne peut être vide</li>'; }
					if( oData[ 'desc' ].trim() == '' ){ sError += '<li>La description ne peut être vide</li>'; }
					if( oData[ 'model' ].trim() == '' ){ sError += '<li>Le modèle du fichier ne peut être vide</li>'; }
					if( oData[ 'file' ].trim() == '' ){ sError += '<li>Le nom du fichier ne peut être vide</li>'; }
					if( sError != '' ){ return '<ul>' + sError + '</ul>'; }

					// enregistrement du nouveau projet
					fetch('/api/project/create_file', {
						method: 'POST',
						headers: { 'Content-Type': 'application/json' },
						body: JSON.stringify(oData) // oData from form
					})
					.then(response => {
						if (!response.ok) { return response.json().then(err => { throw new Error(err.message || `HTTP error ${response.status}`); }); }
						return response.json();
					})
					.then(data => {
						if (data.status === 'success') {
							refreshProjects();
						} else {
							console.error("Failed to create file project:", data.message);
							alert("Error: " + (data.message || "Could not create file project."));
						}
					})
					.catch(error => {
						console.error('Error creating file project:', error);
						alert("Error: " + error.message);
					});
					return true; // Modal closes, fetch handles outcome
				}, "Annuler", null,
				[
					{ 'name': 'name', 'title': 'Nom', 'type': 'string' },
					{ 'name': 'desc', 'title': 'Description', 'type': 'text' },
					{ 'name': 'model', 'title': 'Type d\'application', 'type': 'list', 'k-key': 'name', 'k-value': 'title', 'value': oModels },
					{ 'name': 'file', 'title': 'Enregistrer sous', 'type': 'save-as', 'ext': 'json', 'ext-title': 'Fichier Json', 'initial-file': 'kisstomato.json' },
					{ 'name': 'relatif-path', 'type': 'checkbox', 'title': 'Activer la prise en charge du chemin relatif à KissTomato', 'value': true }
				]
			);
		})
		.catch(error => {
			console.error('Error fetching models:', error);
			alert("Error fetching models: " + error.message);
		});
});

// supprime un projet
$( document ).on( "click", ".del-project", function() {
	var fileProject = $( this ).parent().attr( 'file' );

	modalShowForm( "Supprimer le projet ?", "Supprimer",
		function( oData ){

			fetch('/api/project/delete', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ filename: fileProject, deletefile: oData['del-file'] })
			})
			.then(response => {
				if (!response.ok) { return response.json().then(err => { throw new Error(err.message || `HTTP error ${response.status}`); }); }
				return response.json();
			})
			.then(data => {
				if (data.status === 'success') {
					refreshProjects();
				} else {
					console.error("Failed to delete project:", data.message);
					alert("Error: " + (data.message || "Could not delete project."));
				}
			})
			.catch(error => {
				console.error('Error deleting project:', error);
				alert("Error: " + error.message);
			});

			return true; // Modal closes, fetch handles outcome
		}, "Annuler", null,
		[
			{ 'name': 'del-file', 'title': 'Supprimer également le fichier JSON ?', 'type': 'checkbox' }
		],
		{ 'class-btn-ok': 'danger' }
	);
} );

// actualise les projets
$( document ).on( "click", ".refresh-project", function() {
	refreshProjects();
} );

// ouvre un projet
$( document ).on( "mouseup", ".open-project", function(e) {
	var fileProject = $( this ).parent().attr( 'file' );

	// determine le type de clic
	if( e.which == 1 ){ // clic gauche
		window.location.href = 'project.html?project=' + fileProject;
	}else if( e.which == 2 ){ // clic molette
		window.open('project.html?project=' + fileProject, '_blank');
	}
} );

	// chargement des projets
function refreshProjects(){
	fetch('/api/project/get_all')
		.then(response => {
			if (!response.ok) { return response.json().then(err => { throw new Error(err.message || `HTTP error ${response.status}`); }); }
			return response.json();
		})
		.then(projects => {
			var html = '';
			for( var i=0; i<projects.length; i++ ){
				html += '<div file="' + projects[ i ][ 'file' ] + '"' +
					( projects[ i ][ 'error' ] != undefined ? ' class="alert alert-danger"' :
						' class="alert alert-secondary"' ) + '>';

				// si il y a une erreur
				if( projects[ i ][ 'error' ] != undefined ){
					html += '<p>' + projects[ i ][ 'error' ] + '</p>' +
						'<button type="button" class="del-project btn btn-warning btn-sm">Supprimer</button>' +
						'<button type="button" class="refresh-project btn btn-info btn-sm" style="float:right;">Actualiser</button>';
				}else{
					html += '<h4>' +projects[ i ][ 'name' ] +
							'<span style="margin-left:20px" class="badge text-bg-secondary">' + projects[ i ][ 'model' ] + '</span>' +
						'</h4>' +
						'<p>' + projects[ i ][ 'desc' ] + '</p>' +
						'<button type="button" class="del-project btn btn-warning btn-sm">Supprimer</button>' +
						'<button type="button" class="open-project btn btn-info btn-sm" style="float:right;">Ouvrir</button>';
				}
				html += '</div>';
			}
			$( '#lstProjets' ).html( html );
		})
		.catch(error => {
			console.error('Error fetching projects:', error);
			$( '#lstProjets' ).html('<div class="alert alert-danger">Error loading projects: ' + error.message + '</div>');
		});
}