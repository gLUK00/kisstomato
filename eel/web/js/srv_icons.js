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

	// affichage du nom de l'icon pour information
	$( '#icon_info_name' ).html( sIcon );
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
function iconsGetHtml( sIcon, sColor ){
	var oIcon = iconsGetOne( sIcon );
	return '<i class="fa-' + oIcon[ 'styles' ][ '0' ] + ' fa-' + sIcon + ' fa-2xl"' + ( sColor != undefined && sColor != '' ? ' style="color:' + sColor + '"' : '' ) + '></i>';
}

// recupere le code html de selection du style d'un icon
function iconsGetHtmlStyle( sIcon, sStyle ){
	var sHtmlStyles = '';
	var oIcon = iconsGetOne( sIcon );

	for( var i=0; i<oIcon[ 'styles' ].length; i++ ){
		if( sStyle == oIcon[ 'styles' ][ i ] || ( [ undefined, null ].includes( sStyle ) && i == 0 ) ){
			sHtmlStyles += '<button type="button" class="btn btn-primary btn-sm icon_style">' + oIcon[ 'styles' ][ i ] + '</button>';
		}else{
			sHtmlStyles += '<button type="button" class="btn btn-outline-primary btn-sm icon_style">' + oIcon[ 'styles' ][ i ] + '</button>';
		}
	}

	return sHtmlStyles;
}

// selection du style
$( document ).on( "click", ".icon_style", function() {

} );