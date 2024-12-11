var iconsData = {};

$( document ).ready( function(){
	
	// chargement des icones
	$.getJSON( "js/lib/fontawesome/icons.json", function( data ) {
		iconsData = data;
	});

	document.styleSheets[0].insertRule('.icon_selector{\
			height: 200px;\
			border:1px solid #ccc;\
			border-radius: 5px;\
			overflow-y: scroll;\
			overflow-x: hidden;\
			padding: 5px;\
		}', 0);
	document.styleSheets[0].insertRule('.icon_selector > div {\
			border:1px solid #ccc;\
			border-radius: 5px;\
			padding: 8px;\
			margin: 0 5px 5px 0;\
			cursor: grab;\
			text-align: center;\
			width: 60px;\
			float: left;\
		}', 0);
	document.styleSheets[0].insertRule('.icon_selector > div:hover {\
			background-color: lightblue;\
		}', 0);
	document.styleSheets[0].insertRule('.icon_style {\
			margin-left: 10px;\
		}', 0);
} );

// selection d'un icone
var iconsSelectEvents = {};
$( document ).on( "click", ".icon_select", function() {
	let sIcon = $( this ).attr( 'icon' );
	let sId = $( this ).closest( '.srv_icons' ).attr( 'icon_selector' );

	// memorisation de l'icone et propagation de l'evenement
	iconsSelectEvents[ sId ]( sIcon );
} );

// filter textuel
$( document ).on( "keyup", ".icon_filter", function() {
	let sValue = $( this ).val();
	let sId = $( this ).closest( '.srv_icons' ).attr( 'icon_selector' );

	var oAllIcons = iconsGetAll();

	var sHtmlIcons = '';
	for( var key in oAllIcons ){
		if( key == 'acquisitions-incorporated' ){
			continue;
		}
		let oIcon = oAllIcons[ key ];
		if( oIcon.label.toLowerCase().indexOf( sValue.toLowerCase() ) == -1 ){
			continue;
		}
		sHtmlIcons += '<div class="icon_select" icon="' + key + '"><i class="fa-' + oIcon[ 'styles' ][ '0' ] + ' fa-' + key + ' fa-2xl"></i></div>';
	}

	$( '#icon_selector_' + sId ).html( sHtmlIcons );
} );

// recupere la liste des icones
function iconsGetAll(){
	return iconsData
}

// recupere un icon
function iconsGetOne( key ){
	return iconsGetAll()[ key ];
}

// recupere le code html de selection d'un icon
function iconsGetHtmlPicker( sIdDiv, fSelectIconAndColor ){
	var sHtmlIcons = '';

	var oAllIcons = iconsGetAll();

	for( var key in oAllIcons ){
		if( key == 'acquisitions-incorporated' ){
			continue;
		}
		let oIcon = oAllIcons[ key ];
		sHtmlIcons += '<div class="icon_select" icon="' + key + '"><i class="fa-' + oIcon[ 'styles' ][ '0' ] + ' fa-' + key + ' fa-2xl"></i></div>';
	}
	let sId = makeid();
	sHtmlIcons = '<div id="' + sIdDiv + '" class="srv_icons" icon_selector="' + sId + '">\
			Filtrer sur <input class="icon_filter" type="text" icon_selector="' + sId + '"/> <span id="icon_info_name"></span>\
			<div class="icon_selector" id="icon_selector_' + sId + '">' + sHtmlIcons + '</div>\
		</div>';

	// enregistrement du callback
	iconsSelectEvents[ sId ] = fSelectIconAndColor;

	return sHtmlIcons;
}

// recupere le code html d'un icon
function iconsGetHtml( sIcon, sColor, sStyle ){
	var oIcon = iconsGetOne( sIcon );
	if( [ undefined, null, '' ].includes( sColor ) ){
		sColor = '';
	}else{
		sColor = ' style="color:' + sColor + '"';
	}
	if( [ undefined, null, '' ].includes( sStyle ) ){
		sStyle = oIcon[ 'styles' ][ '0' ];
	}
	return '<i class="fa-' + sStyle + ' fa-' + sIcon + ' fa-2xl"' + sColor + '></i>';
}

// recupere le code html de selection du style d'un icon
function iconsGetHtmlStyle( sIcon, sStyle, sIdTarget ){
	var sHtmlStyles = '';
	var oIcon = iconsGetOne( sIcon );

	for( var i=0; i<oIcon[ 'styles' ].length; i++ ){

		// determine si le style doit etre selectionne
		var bSelected = sStyle == oIcon[ 'styles' ][ i ] || ( [ undefined, null ].includes( sStyle ) && i == 0 );
		sHtmlStyles += '<button type="button" class="btn btn' + ( !bSelected ? '-outline' : '' ) + '-primary btn-sm icon_style" id_target="' + sIdTarget + '">' + oIcon[ 'styles' ][ i ] + '</button>';
	}

	// si pas de style, selection du premier par defaut
	if( [ undefined, null ].includes( sStyle ) ){
		window.setTimeout( function(){
			$( '.icon_style[id_target=' + sIdTarget + ']' )[ 0 ].click();
		}, 100 );
	}

	return sHtmlStyles;
}

// selection du style
$( document ).on( "click", ".icon_style", function() {
	let sId = $( this ).attr( 'id_target' );
	$( '#' + sId ).val( $( this ).html() );

	// gestion de la selection des boutons
	$( '.icon_style[id_target=' + sId + ']' ).removeClass( 'btn-primary' ).addClass( 'btn-outline-primary' );
	$( this ).removeClass( 'btn-outline-primary' ).addClass( 'btn-primary' );

	// modification de l'affichage de l'icon
	let sIdField = sId.replace( 'icon_style_', '' );
	iconsRefresh( sIdField );
} );

// changement de couleur
$( document ).on( "change", ".icon-color", function() {

	// modification de l'affichage de l'icon
	let sIdField = $( this ).attr( 'id' ).replace( 'icon_color_', '' );
	iconsRefresh( sIdField );
} );

// mise a jour de l'affichage
function iconsRefresh( sIdField ){
	$( '#icon_' + sIdField ).html( iconsGetHtml( $( '#icon_value_' + sIdField ).val(), $( '#icon_color_' + sIdField ).val(), $( '#icon_style_' + sIdField ).val() ) );
	$( '#icon_info_name' ).html( 'fa-' + $( '#icon_style_' + sIdField ).val() +  ' fa-' + $( '#icon_value_' + sIdField ).val() + ' : color = ' + $( '#icon_color_' + sIdField ).val() );
}