
// reference des onglets
var oTabs = [];

// selection unique d'un bouton radio
$( document ).on( "click", ".select-radio-item", function() {
	$( this ).closest( '.mb-3' ).find( '.select-radio-item' ).prop( "checked", false );
	$( this ).prop( "checked", true );
} );

// report d'affichage de la valeur d'un range
$( document ).on( "click", "input.form-range", function() {
	
	$( this ).closest( '.mb-3' ).find( '.select-range-show' ).html( $( this ).val() );
	
} );

// click sur le bouton "modifier"
$( document ).on( "click", ".tabUpdate", function() {
	var sId = $( this ).attr( 'idTab' );
	var oTab = tabGetTab( sId );

	// change l'etat de l'onglet
	oTab.state = 'edit';
	refreshTabs();
} );

// click sur le bouton "fermer"
$( document ).on( "click", ".tabClose", function() {
	
	console.log( 'tabClose' );
} );

// click sur le bouton "enregistrer"
$( document ).on( "click", ".tabSave", function() {
	var sId = $( this ).attr( 'idTab' );
	var oTab = tabGetTab( sId );

	// recupere les donnees du formulaire
	for( var a=0; a<oTab.form.length; a++ ){
		var oField = oTab.form[ a ];
		var sIdField = 'tab-field-' + oTab.id + '-' + oField.id;

		if( [ 'string', 'text', 'color', 'switch', 'range', 'list' ].includes( oField.type ) ){
			oField.value = $( '#' + sIdField ).val();
		}else if( oField.type == 'checkbox' ){
			oField.value = [];
			for( var b=0; b<oField.items.length; b++ ){
				if( $( '#' + sIdField + '-' + b ).is( ':checked' ) ){
					oField.value.push( $( '#' + sIdField + '-' + b ).val() );
				}
			}
		}else if( oField.type == 'radio' ){
			for( var b=0; b<oField.items.length; b++ ){
				if( $( '#' + sIdField + '-' + b ).is( ':checked' ) ){
					oField.value = $( '#' + sIdField + '-' + b ).val();
				}
			}
		}else if( oField.type == 'icon' ){
			oField.value = { icon: $( '#icon_value_' + sIdField ).val(), color: $( '#icon_color_' + sIdField ).val() };
		}
	}

	// change l'etat de l'onglet
	oTab.state = 'view';
	refreshTabs();

	// si il y a une fonction de callback
	if( oTab.eOnSave != undefined ){
		oTab.eOnSave( oTab );
	}
} );

// click sur le bouton "annuler"
$( document ).on( "click", ".tabCancel", function() {
	var sId = $( this ).attr( 'idTab' );
	var oTab = tabGetTab( sId );

	

	/*oTab.state = 'view';
	refreshTabs();*/

	
	console.log( 'tabCancel' );
} );

// ajout d'un onglet
function tabAddTab( oTab ){
	for( var i=0; i<oTabs.length; i++ ){
		if( oTabs[ i ].focus ){
			oTabs[ i ].focus = false;
		}
	}
	oTab.focus = true;
	oTabs.push( oTab );
	refreshTabs();
}

function refreshTabs(){
	$( '#col_right' ).modTab( { tabs: oTabs } );
}

//recherche un tab en fonction de son id
function tabGetTab( sId ){
	for( var i=0; i<oTabs.length; i++ ){
		if( oTabs[ i ].id == sId ){
			return oTabs[ i ];
		}
	}
	return null;
}


/*

oTabs.push( { id: 's6d4fsd65f', text: 'Nouveau', state: 'new', form: [], focus: true } );
oTabs.push( { id: 's6d4fsd65f', text: 'Edition', state: 'edit', form: [] } );
oTabs.push( { id: 's6d4fsd65fcccd', text: 'un autre', state: 'view', form: [] } );

*/

// changement de la couleur de l'icon
$( document ).on( "change", ".icon-color", function() {
	let sField = $( this ).attr( 'field' );
	$( '#icon_' + sField + ' > i' ).css( "color", $( this ).val() );
} );


jQuery.extend(jQuery.fn, {
	modTab: function(options){
		var defauts={
			'action': 'show',
			'tabs': []
		};
		var params=$.extend(defauts, options);

		// determine l'index du tab affiche au premier plan
		var iViewIndex = params.tabs.length - 1;
		for( var i=0; i<params.tabs.length; i++ ){
			var oTab = params.tabs[ i ];
			if( oTab.focus != undefined && oTab.focus ){
				iViewIndex = i;
				break;
			}
		}

		return this.each(function(){

			var sTabs = '';
			var sForms = '';
			for( var i=0; i<params.tabs.length; i++ ){
				var oTab = params.tabs[ i ];

				// determine l'etat de la barre d'edition
				var sStateBar = '<button idTab="' + oTab.id + '" type="button" class="btn btn-info btn-sm tabUpdate">Modifier</button>';
				if( oTab.state != 'view' ){
					sStateBar = '<button idTab="' + oTab.id + '" type="button" class="btn btn-warning btn-sm tabCancel" style="margin-right:50px">Annuler</button>' +
						'<button idTab="' + oTab.id + '" type="button" class="btn btn-success btn-sm tabSave">Enregistrer</button>';
				}

				// construction du formulaire
				var sForm = '';
				if( oTab.form != undefined && oTab.form.length > 0 ){
					for( var a=0; a<oTab.form.length; a++ ){
						var oField = oTab.form[ a ];
						var sIdField = 'tab-field-' + oTab.id + '-' + oField.id;
						if( oField.type == 'string' ){
							sForm += '<div class="mb-3">' +
								'<label for="' + sIdField + '" class="form-label">' + oField.text + '</label>' +
								'<input type="text" class="form-control" id="' + sIdField + '">' +
							'</div>';
						}else if( oField.type == 'text' ){
							sForm += '<div class="mb-3">' +
								'<label for="' + sIdField + '" class="form-label">' + oField.text + '</label>' +
								'<textarea class="form-control" id="' + sIdField + '" rows="3"></textarea>' +
							'</div>';
						}else if( oField.type == 'list' ){
							sForm +=  '<div class="mb-3">' +
								'<label for="' + sIdField + '" class="form-label">' + oField.text + '</label>' +
								'<select id="' + sIdField + '" class="form-select" aria-label="Default select example">';
							for( var b=0; b<oField.items.length; b++ ){
								var oItem = oField.items[ b ];
								sForm += '<option value="' + oItem.value + '">' + oItem.text + '</option>';
							}
							sForm += '</select>' +
								'</div>';
						}else if( oField.type == 'checkbox' ){
							sForm +=  '<div class="mb-3">' +
								'<label class="form-label">' + oField.text + '</label>';
							for( var b=0; b<oField.items.length; b++ ){
								var oItem = oField.items[ b ];
								sForm += '<div class="form-check">' +
									'<input class="form-check-input" type="checkbox" value="' + oItem.value + '" id="' + sIdField + '-' + b + '">' +
									'<label class="form-check-label" for="' + sIdField + '-' + b + '">' + oItem.text + '</label>' +
								'</div>';
							}
							sForm += '</div>';
						}else if( oField.type == 'radio' ){
							sForm +=  '<div class="mb-3">' +
								'<label class="form-label">' + oField.text + '</label>';
							for( var b=0; b<oField.items.length; b++ ){
								var oItem = oField.items[ b ];
								sForm += '<div class="form-check">' +
									'<input class="select-radio-item form-check-input" type="radio" value="' + oItem.value + '" id="' + sIdField + '-' + b + '">' +
									'<label class="form-check-label" for="' + sIdField + '-' + b + '">' + oItem.text + '</label>' +
								'</div>';
							}
							sForm += '</div>';
						}else if( oField.type == 'color' ){
							sForm +=  '<div class="mb-3">' +
								'<label for="' + sIdField + '" class="form-label">' + oField.text + '</label>' +
								'<input type="color" class="form-control form-control-color" id="' + sIdField + '" title="Choisir la couleur">' +
							'</div>';
						}else if( oField.type == 'switch' ){
							sForm +=  '<div class="form-check form-switch">' +
								'<input class="form-check-input" type="checkbox" role="switch" id="' + sIdField + '">' +
								'<label class="form-check-label" for="' + sIdField + '">' + oField.text + '</label>' +
							'</div>';
						}else if( oField.type == 'range' ){
							sForm +=  '<div class="mb-3">' +
								'<label for="' + sIdField + '" class="form-label">' + oField.text + '</label>' +
								'<span class="select-range-show" style="float:right">' + ( oField.value != undefined ? oField.value : '' ) + '</span>' +
								'<input type="range" class="form-range" id="' + sIdField + '" min="' + oField.min + '" max="' + oField.max + '">' +
							'</div>';
						}else if( oField.type == 'icon' ){

							var sCpIdField = sIdField;
							sForm +=  '<div class="mb-3">' +
								'<label for="' + sIdField + '" class="form-label">' + oField.text + '</label>' +
								'<table width="200px">' +
									'<tr>' +
										'<td style="width:200px">' +
											'<div class="icon_selected" id="icon_' + sIdField + '">' +
												( oField.value != undefined && oField.value.icon != '' ? iconsGetHtml( oField.value.icon, oField.value.color ) : '' ) +
											'</div>' +
											'<input type="hidden" id="icon_value_' + sIdField + '" value="' + ( oField.value != undefined ? oField.value.icon : '' ) + '">' +
										'</td>' +
										'<td style="width:200px">' +
											'<input type="color" class="form-control form-control-color icon-color" field="' + sIdField + '" id="icon_color_' + sIdField + '" value="' + ( oField.value != undefined ? oField.value.color : '' ) + '" title="Choisir la couleur">' +
										'</td>' +
									'</tr>' +
								'</table>' +
								iconsGetHtmlPicker( 'div_select_icon_' + sCpIdField, function( icon ){

									// recupere l'icone
									$( '#icon_' + sCpIdField ).html( iconsGetHtml( icon ) );
									$( '#icon_value_' + sCpIdField ).val( icon );

									// si il y a une couleur
									let sColor = $( '#icon_color_' + sCpIdField ).val();
									if( sColor != '' ){
										$( '#icon_' + sCpIdField + ' > i' ).css( 'color', sColor );
									}
								} ) +
							'</div>';
						}



						
					}
				}


				sTabs += '<button class="nav-link' + ( i == iViewIndex ? ' active' : '' ) + '" id="' + oTab.id + '-tab" data-bs-toggle="tab" data-bs-target="#' + oTab.id + '" type="button" role="tab" aria-controls="' + oTab.id + '" aria-selected="' + ( i == iViewIndex ? 'true' : 'false' ) + '">' + oTab.text + ( oTab.state != 'view' ? ' *': '' ) + '</button>';
				sForms += '<div class="tab-pane fade' + ( i == iViewIndex ? ' show active' : '' ) + '" id="' + oTab.id + '" role="tabpanel" aria-labelledby="' + oTab.id + 'e-tab" tabindex="0">' +
					'<div style="height:40px;">' +
							( oTab.state == 'view' ? '<div style="float:left;">' +
								'<button idTab="' + oTab.id + '" type="button" class="btn btn-secondary btn-sm tabClose">Fermer</button>' +
							'</div>' : '' ) +
						'<div style="float:right;">' + sStateBar + '</div>' +
					'</div>' +
					'<div>' + sForm + '</div>' +
				'</div>';
			}

			$(this).html( '<nav><div class="nav nav-tabs" id="nav-tab" role="tablist">' + sTabs +
				'</div></nav><div class="tab-content" id="nav-tabContent" style="border-left: 1px solid #dee2e6;padding: 10px;">' + sForms + '</div>' );

			// attribution des valeurs
			for( var i=0; i<params.tabs.length; i++ ){
				var oTab = params.tabs[ i ];

				// pour le formulaire
				if( oTab.form != undefined && oTab.form.length > 0 ){

					// pour tous les champs
					for( var a=0; a<oTab.form.length; a++ ){
						var oField = oTab.form[ a ];
						var sIdField = 'tab-field-' + oTab.id + '-' + oField.id;

						// attribution des valeurs
						if( oField.value != undefined && $.inArray( oField.type, [ 'string', 'text', 'int', 'list', 'color', 'range' ] ) != -1 ){
							$( '#' + sIdField ).val( oField.value );
							//console.log( '#tab-field-' + oTab.id + '-' + oField.id );
							//console.log( oField.value );
						}else if( oField.values != undefined && $.inArray( oField.type, [ 'checkbox' ] ) != -1 ){
							for( var b=0; b<oField.items.length; b++ ){
								var oItem = oField.items[ b ];
								if( $.inArray( oItem.value, oField.values ) != -1 ){
									$( '#' + sIdField + '-' + b ).prop( "checked", true );
								}
							}
						}else if( oField.value != undefined && $.inArray( oField.type, [ 'radio' ] ) != -1 ){
							for( var b=0; b<oField.items.length; b++ ){
								var oItem = oField.items[ b ];
								if( oItem.value == oField.value ){
									$( '#' + sIdField + '-' + b ).prop( "checked", true );
								}
							}
						}else if( oField.value != undefined && oField.value && $.inArray( oField.type, [ 'switch' ] ) != -1 ){
							$( '#' + sIdField ).prop( "checked", true );
						}else if( oField.type == 'icon' && oField.icon != undefined && oField.icon != '' ){
							let oIcon = iconsGetOne( oField.icon );
							$( '#icon_' + sIdField ).html( '<i class="fa-' + oIcon[ 'styles' ][ '0' ] + ' fa-' + oField.icon + ' fa-2xl"></i>' );
						}

						if( oField.type == 'icon' && oField.color != undefined && oField.color != '' ){
							$( '#icon_' + sIdField + ' > i' ).css( "color", oField.color );
						}

						// gestion de l'etat
						if( oTab.state == 'view' ){
							if( $.inArray( oField.type, [ 'string', 'text', 'int', 'list', 'color', 'switch', 'range' ] ) != -1 ){
								$( '#' + sIdField ).prop( "disabled", true );
							}else if( $.inArray( oField.type, [ 'checkbox', 'radio' ] ) != -1 ){
								for( var b=0; b<oField.items.length; b++ ){
									var oItem = oField.items[ b ];
									$( '#' + sIdField + '-' + b ).prop( "disabled", true );
								}
							}else if( oField.type == 'icon' ){
								$( '#div_select_icon_' + sIdField ).hide();
								$( '#icon_color_' + sIdField ).prop( "disabled", true );
							}
						}
					}
				}

				
			}

/*
{ id: 's6d4fsd65f', text: 'Nouveau', state: 'new', form: [
{ id: '4sf5sd4': type: 'string', text: 'Nom', value: 'un truc' },	
{ id: '4sfsss5sd4': type: 'string', text: 'Nom 2' },
{ id: '4sfsss5sdss4': type: 'int', text: 'Un nombre' },
{ id: '4sfsss5sd4ddd': type: 'text', text: 'Un texte' },
{ id: 'utut': type: 'list', text: 'Une liste', value:'b', items:[
		{ text: 'valeur a', value: 'a' },
		{ text: 'valeur b', value: 'b' },
		{ text: 'valeur c', value: 'c' }
	]
},
{ id: 'ututss': type: 'checkbox', text: 'Une liste de CAC', values:['a', 'c' ], items:[
		{ text: 'valeur a', value: 'a' },
		{ text: 'valeur b', value: 'b' },
		{ text: 'valeur c', value: 'c' }
	]
}
*/
			

			console.log( '-------------------------' );
			console.log( $(this) );

			//$(this).css( 'border', '1px solid red');


			/*<nav>
						<div class="nav nav-tabs" id="nav-tab" role="tablist">
							<button class="nav-link active" id="nav-home-tab" data-bs-toggle="tab" data-bs-target="#nav-home" type="button" role="tab" aria-controls="nav-home" aria-selected="true">Home</button>
							<button class="nav-link" id="nav-profile-tab" data-bs-toggle="tab" data-bs-target="#nav-profile" type="button" role="tab" aria-controls="nav-profile" aria-selected="false">Profile *</button>
							<button class="nav-link" id="nav-contact-tab" data-bs-toggle="tab" data-bs-target="#nav-contact" type="button" role="tab" aria-controls="nav-contact" aria-selected="false">Contact</button>
							<button class="nav-link" id="nav-disabled-tab" data-bs-toggle="tab" data-bs-target="#nav-disabled" type="button" role="tab" aria-controls="nav-disabled" aria-selected="false" disabled>Disabled</button>
						</div>
					</nav>
					<div class="tab-content" id="nav-tabContent" style="border-left: 1px solid #dee2e6;padding: 10px;">
						<div class="tab-pane fade show active" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab" tabindex="0">
							<div style="text-align: right;">
								<button type="button" class="btn btn-info btn-sm">Modifier</button>
								<button type="button" class="btn btn-warning btn-sm" style="margin-right:50px">Annuler</button>
								<button type="button" class="btn btn-success btn-sm">Enregistrer</button>
							</div>
							fghjfg fgh jfh jfg jgfhj gfhj
						</div>
						<div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab" tabindex="0">.ghhhhhhhh h h dh dgfhgfh.</div>
						<div class="tab-pane fade" id="nav-contact" role="tabpanel" aria-labelledby="nav-contact-tab" tabindex="0">fffffffffffffff fg fg sdf gsdfg sdfg sdfg</div>
						<div class="tab-pane fade" id="nav-disabled" role="tabpanel" aria-labelledby="nav-disabled-tab" tabindex="0">.ffffffffffffffffffffff sfd sdf sdf d fdf</div>
					</div>*/
		} );
	}
});