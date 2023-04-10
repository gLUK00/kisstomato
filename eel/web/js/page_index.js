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
			eel.set_file_project( oData[ 'file' ].trim() )( function( result ){

				console.log( 'js set_file_project' );
				console.log( result );

				if( result === true ){
					refreshProjects();
				}
			} );
			
			return true;
		}, "Annuler", null,
		[
			{ 'name': 'file', 'title': 'Fichier du projet', 'type': 'set-file', 'ext': 'json', 'ext-title': 'Fichier Json'}
		]
	);
} );

// creation d'un projet
$( document ).on( "click", "#btn-new-projet", function() {

	// recupere tous des types de modeles des plugins
	/*oModels = [
		{ 'name': 'python_flask', 'title': 'Application Python Flask' },
		{ 'name': 'python_script', 'title': 'Script Python' }
	];*/

	eel.get_all_models()( function( oModels ){
		modalShowForm( "Nouveau projet", "Enregistrer sous",
			function( oData ){

				// controle du formulaire
				sError = '';
				if( oData[ 'name' ].trim() == '' ){
					sError += '<li>Le nom ne peut être vide</li>';
				}
				if( oData[ 'desc' ].trim() == '' ){
					sError += '<li>La description ne peut être vide</li>';
				}
				if( oData[ 'model' ].trim() == '' ){
					sError += '<li>Le modèle du fichier ne peut être vide</li>';
				}
				if( oData[ 'file' ].trim() == '' ){
					sError += '<li>Le nom du fichier ne peut être vide</li>';
				}
				if( sError != '' ){
					return '<ul>' + sError + '</ul>';
				}

				// enregistrement du nouveau projet
				eel.get_create_file_project( oData )( function( result ){

					console.log( 'js get_create_file_project' );
					console.log( result );

					if( result === true ){
						refreshProjects();
					}
				} );

				return true;
			}, "Annuler", null,
			[
				{ 'name': 'name', 'title': 'Nom', 'type': 'string' },
				{ 'name': 'desc', 'title': 'Description', 'type': 'text' },
				{ 'name': 'model', 'title': 'Type d\'application', 'type': 'list', 'k-key': 'name', 'k-value': 'title', 'value': oModels },
				{ 'name': 'file', 'title': 'Enregistrer sous', 'type': 'save-as', 'ext': 'json', 'ext-title': 'Fichier Json', 'initial-file': 'kisstomato.json' }
			]
		);
	} );
});

// supprime un projet
$( document ).on( "click", ".del-project", function() {
	var fileProject = $( this ).parent().attr( 'file' );

	modalShowForm( "Supprimer le projet ?", "Supprimer",
		function( oData ){

			eel.del_project( fileProject, oData[ 'del-file' ] )( function( result ){
				console.log( 'js del_project' );
				console.log( result );

				if( result === true ){
					refreshProjects();
				}
			} );

			return true;
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
		eel.app_new_window( 'project.html?project=' + fileProject )
	}
} );

// chargement des projets
function refreshProjects(){
	eel.get_all_projects()( function( projects ){

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
	} );
}