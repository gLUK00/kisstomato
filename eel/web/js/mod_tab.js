
// reference des onglets
var oTabs = [];

$( document ).ready( function(){
	
	document.styleSheets[0].insertRule('.object_select_path{\
			border:1px solid #ccc;\
			border-radius: 5px;\
			padding: 5px;\
			margin-right: 5px;\
			min-height: 35px;\
		}', 0);
} );

// selection unique d'un bouton radio
$( document ).on( "click", ".select-radio-item", function() {
	$( this ).closest( '.mb-3' ).find( '.select-radio-item' ).prop( "checked", false );
	$( this ).prop( "checked", true );
} );

// report d'affichage de la valeur d'un range
$( document ).on( "click", "input.form-range", function() {
	
	$( this ).closest( '.mb-3' ).find( '.select-range-show' ).html( $( this ).val() );
	
} );

// click sur la selection d'un objet
$( document ).on( "click", ".object_selector", function() {
	let sField = $( this ).attr( 'field' );

	// recherche de l'onglet et du champ
	var oTab = null;
	var oField = null;
	rechercheElements: {
		for( var i=0; i<oTabs.length; i++ ){
			var oTab = oTabs[ i ];
			for( var a=0; a<oTab.form.length; a++ ){
				oField = oTab.form[ a ];
				var sIdField = 'tab-field-' + oTab.id + '-' + oField.id;
				if( sField == 'tab-field-' + oTab.id + '-' + oField.id ){
					break rechercheElements;
				}
			}
		}
	}

	var { oItems, sKey } = _tabSelectObject == null ? { oItems: [], sKey: '' } : _tabSelectObject( oField );
	modalShowList( 'Selection d\'un objet', oItems, sKey, function( oItem ){
		$( '#' + sIdField ).val( oItem[ 'id' ] );
		$( '#object_select_' + sIdField ).html( nodeGetHtmlName( oItem ) );
	} );

} );

// click sur le bouton "modifier"
$( document ).on( "click", ".tabUpdate", function() {
	var sId = $( this ).attr( 'idTab' );
	var oTab = tabGetTab( sId );

	// change l'etat de l'onglet
	oTab.state = 'edit';
	refreshTabs();
} );

// enregistrement d'un evenement d'affichage sur le selecteur d'un objet
var _tabSelectObject = null;
function tabSetShowSelectObject( fSelector ){
	_tabSelectObject = fSelector;
}

// click sur le bouton "fermer"
function tabClose( sId ){
	var oNewTabs = [];

	for( var i=0; i<oTabs.length; i++ ){
		if( oTabs[ i ].id == sId ){
			continue;
		}
		oNewTabs.push( oTabs[ i ] );
	}

	oTabs = oNewTabs;
	refreshTabs();
}
$( document ).on( "click", ".tabClose", function() {
	var sId = $( this ).attr( 'idTab' );
	tabClose( sId );
} );

// click molette sur un onglet
$( document ).on( "mousedown", "#nav-tab > button", function( e ) {
	if( e.which != 2 ){
		return;
	}
	var sId = $( this ).attr( 'idTab' );
	var oTab = tabGetTab( sId );
	if( [ 'edit', 'new' ].includes( oTab.state ) ){
		tabCancel( sId, true );
		return;
	}
	tabClose( sId );
} );

// click sur un onglet
$( document ).on( "click", "#nav-tab > button", function( e ) {
	var sId = $( this ).attr( 'idTab' );
	$( '#nav-tab > button' ).removeClass( 'active' );
	$( this ).addClass( 'active' );
	$( '#nav-tabContent > div' ).removeClass( 'active show' );
	$( '#tab-' + sId ).addClass( 'active show' );
} );

// click sur le bouton "enregistrer"
$( document ).on( "click", ".tabSave", function() {
	var sId = $( this ).attr( 'idTab' );
	var oTab = tabGetTab( sId );

	// recupere les donnees du formulaire
	for( var a=0; a<oTab.form.length; a++ ){
		var oField = oTab.form[ a ];
		var sIdField = 'tab-field-' + oTab.id + '-' + oField.id;

		if( [ 'string', 'text', 'color', 'range', 'list', 'object' ].includes( oField.type ) ){
			oField.value = $( '#' + sIdField ).val();
		}else if( oField.type == 'switch' ){
			oField.value = $( '#' + sIdField ).is( ':checked' );
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
			oField.value = { icon: $( '#icon_value_' + sIdField ).val(), color: $( '#icon_color_' + sIdField ).val(), style: $( '#icon_style_' + sIdField ).val() };
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
function tabCancel( sId, bForceClose ){
	modalShowQuery( 'Annuler les modifications', 'Voulez vous annuler les modifications ?', 'Oui', function(){
		
		// mise a jour de l'etat de l'onglet
		if( bForceClose ){
			tabClose( sId );
			return;
		}
		var oTab = tabGetTab( sId );
		oTab.state = 'view';
		refreshTabs();
	}, 'Non' );
}
$( document ).on( "click", ".tabCancel", function() {
	var sId = $( this ).attr( 'idTab' );
	tabCancel( sId );
} );

// focus sur un onglet si il existe
function tabFocusIfExist( sId ){
	var bExist = false;

	// recherche si l'onglet existe
	for( var i=0; i<oTabs.length; i++ ){
		if( oTabs[ i ].id == sId ){
			bExist = true;
			break;
		}
	}
	if( bExist ){
		for( var i=0; i<oTabs.length; i++ ){
			oTabs[ i ].focus = ( oTabs[ i ].id == sId );
		}
		refreshTabs();
	}

	return bExist;
}

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
	//$( '#col_right' ).modTab( { tabs: oTabs } );

	// determine l'index du tab affiche au premier plan
	var iViewIndex = oTabs.length - 1;
	for( var i=0; i<oTabs.length; i++ ){
		var oTab = oTabs[ i ];
		if( oTab.focus != undefined && oTab.focus ){
			iViewIndex = i;
			break;
		}
	}

	// pour tous les onglets
	var sTabs = '';
	var sForms = '';
	for( var i=0; i<oTabs.length; i++ ){
		var oTab = oTabs[ i ];

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
						'<label class="form-label">' + oField.text + '</label>' +
						'<table>' +
							'<tr>' +
								'<td style="width:70px">' +
									'<div class="icon_selected" id="icon_' + sIdField + '">' +
										( oField.value != undefined && oField.value.icon != '' ? iconsGetHtml( oField.value.icon, oField.value.color, oField.value.style ) : '' ) +
									'</div>' +
									'<input type="hidden" id="icon_value_' + sIdField + '" value="' + ( oField.value != undefined ? oField.value.icon : '' ) + '">' +
									'<input type="hidden" id="icon_style_' + sIdField + '" value="' + ( oField.value != undefined ? oField.value.style : '' ) + '">' +
								'</td>' +
								'<td style="width:70px">' +
									'<input type="color" class="form-control form-control-color icon-color" field="' + sIdField + '" id="icon_color_' + sIdField + '" value="' + ( oField.value != undefined ? oField.value.color : '' ) + '" title="Choisir la couleur">' +
								'</td>' +
								'<td>' +
									'<div id="div_style_icon_' + sCpIdField + '">' +
										( oField.value != undefined && oField.value.icon != '' ? iconsGetHtmlStyle( oField.value.icon, oField.value.style, 'icon_style_' + sCpIdField ) : '' ) +
									'</div>' +
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

							// mise a jour des styles
							$( '#div_style_icon_' + sCpIdField ).html( iconsGetHtmlStyle( icon, null, 'icon_style_' + sCpIdField ) );
						} ) +
					'</div>';
				}else if( oField.type == 'object' ){
					sForm +=  '<div class="mb-3">' +
						'<label class="form-label">' + oField.text + '</label>' +
						'<table width="100%">' +
							'<tr>' +
								'<td>' +
									'<input type="hidden" id="' + sIdField + '" value="' + oField.value + '">' +
									( oTab.state != 'view' ?
										'<div class="object_select_path" id="object_select_' + sIdField + '">' + nodeGetHtmlName( nodeGetNode( oField.value ) ) + '</div>' :
										'<div class="object_select_path" id="object_select_' + sIdField + '" style="background-color:#e9ecef;" disabled>' + nodeGetHtmlName( nodeGetNode( oField.value ) ) + '</div>'
									) +
								'</td>' +
								'<td width="130px" align="right" style="display: contents;">' +
									( oTab.state != 'view' ?
										'<button type="button" refId="' + sIdField + '" htmlId="object_select_' + sIdField + '" class="btn btn-danger btn-sm object_erase_modal"><i class="fa-solid fa-eraser"></i></button>&nbsp;' +
										'<button type="button" field="' + sIdField + '" class="btn btn-primary btn-sm object_selector">Sélectionner</button>'
										:
										'<button type="button" class="btn btn-secondary btn-sm">Sélectionner</button>'
									) +
								'</td>' +
							'</tr>' +
						'</table>' +
					'</div>';
				}
				
			}
		}

		sTabs += '<button class="nav-link' + ( i == iViewIndex ? ' active' : '' ) + '" idTab="' + oTab.id + '">' + oTab.text + ( oTab.state != 'view' ? ' *': '' ) + '</button>';
		//sTabs += '<button class="nav-link' + ( i == iViewIndex ? ' active' : '' ) + '" idTab="' + oTab.id + '" id="' + oTab.id + '-tab" data-bs-toggle="tab" data-bs-target="#' + oTab.id + '" type="button" role="tab" aria-controls="' + oTab.id + '" aria-selected="' + ( i == iViewIndex ? 'true' : 'false' ) + '">' + oTab.text + ( oTab.state != 'view' ? ' *': '' ) + '</button>';
		sForms += '<div class="tab-pane fade' + ( i == iViewIndex ? ' active show' : '' ) + '" id="tab-' + oTab.id + '" tabindex="0">' +
		//sForms += '<div class="tab-pane fade' + ( i == iViewIndex ? ' active show' : '' ) + '" id="' + oTab.id + '" role="tabpanel" aria-labelledby="' + oTab.id + 'e-tab" tabindex="0">' +
			'<div style="height:40px;">' +
					( oTab.state == 'view' ?
						'<div style="float:left;">' +
							'<button idTab="' + oTab.id + '" type="button" class="btn btn-secondary btn-sm tabClose">Fermer</button>' +
						'</div>' : ''
					) +
				'<div style="float:right;">' + sStateBar + '</div>' +
			'</div>' +
			'<div>' + sForm + '</div>' +
		'</div>';
	}

	$( '#col_right' ).html( '<nav>' +
			'<div class="nav nav-tabs" id="nav-tab" role="tablist">' +
				sTabs +
			'</div>' +
		'</nav>' +
		'<div class="tab-content" id="nav-tabContent" style="border-left: 1px solid #dee2e6;padding: 10px;">' +
			sForms +
		'</div>'
	);

	// attribution des valeurs
	for( var i=0; i<oTabs.length; i++ ){
		var oTab = oTabs[ i ];

		// pour le formulaire
		if( oTab.form != undefined && oTab.form.length > 0 ){

			// pour tous les champs
			for( var a=0; a<oTab.form.length; a++ ){
				var oField = oTab.form[ a ];
				var sIdField = 'tab-field-' + oTab.id + '-' + oField.id;

				// attribution des valeurs
				if( oField.value != undefined && $.inArray( oField.type, [ 'string', 'text', 'int', 'list', 'color', 'range', 'object' ] ) != -1 ){
					$( '#' + sIdField ).val( oField.value );
					//console.log( '#tab-field-' + oTab.id + '-' + oField.id );
					//console.log( oField.value );
				}else if( oField.value != undefined && $.inArray( oField.type, [ 'checkbox' ] ) != -1 ){
					for( var b=0; b<oField.items.length; b++ ){
						var oItem = oField.items[ b ];
						if( $.inArray( oItem.value, oField.value ) != -1 ){
							$( '#' + sIdField + '-' + b ).prop( "checked", true );
						}
					}
				}else if( oField.value != undefined && $.inArray( oField.type, [ 'checkbox', 'radio' ] ) != -1 ){
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
						$( '.icon_style[id_target=icon_style_' + sIdField + ']' ).prop( "disabled", true );
					}
				}
			}
		}
		
	}
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

// efface la selection d'un objet


/*
jQuery.extend(jQuery.fn, {
	modTab: function(options){
		var defauts={
			'action': 'show',
			'tabs': []
		};
		var params=$.extend(defauts, options);

		

	}
});*/