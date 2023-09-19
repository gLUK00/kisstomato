var fModalQueryYes = function(){};
var fModalQueryNo = function(){};
$( document ).on( "click", "#btnModalQueryNo", function(){ fModalQueryNo(); } );
$( document ).on( "click", "#btnModalQueryYes", function(){ fModalQueryYes(); } );

var oModalList = null;
var fModalSelectItemList = function(){};
var oModalItemList = [];
$( document ).on( "click", ".btnItemListModal", function(){
	var sIndex = $( this ).attr( 'indexItem' );

	oModalList.hide();

	fModalSelectItemList( oModalItemList[ sIndex ] );
} );

var fModalInputYes = function(){};
var fModalInputNo = function(){};
$( document ).on( "click", "#btnModalInputNo", function(){ fModalInputNo(); } );
$( document ).on( "click", "#btnModalInputYes", function(){ fModalInputYes(); } );

var fModalFormYes = function(){};
var fModalFormNo = function(){};
$( document ).on( "click", "#btnModalFormNo", function(){ fModalFormNo(); } );
$( document ).on( "click", "#btnModalFormYes", function(){ fModalFormYes(); } );

// affichage d'une question yes/no
function modalShowQuery( sTitle, sQuery, sTitleYes, fYes, sTitleNo, fNo ){

	// determine si la modale existe dans le DOM
	if( $( '#modalQuery' ).length == 0 ){
		$( 'body' ).append( '<div id="modalQuery" class="modal" tabindex="-1"></div>' );
	}

	var sHtml = '<div class="modal-dialog">' +
		'<div class="modal-content">' +
			'<div class="modal-header">' +
				'<h5 class="modal-title">' + sTitle + '</h5>' +
				'<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>' +
			'</div>' +
			'<div class="modal-body">' +
				'<p>' + sQuery + '</p>' +
			'</div>' +
			'<div class="modal-footer">' +
				'<button type="button" id="btnModalQueryNo" class="btn btn-secondary" data-bs-dismiss="modal">' + sTitleNo + '</button>' +
				'<button type="button" id="btnModalQueryYes" class="btn btn-primary">' + sTitleYes + '</button>' +
			'</div>' +
		'</div>' +
	'</div>';
	$( '#modalQuery' ).html( sHtml );

	var myModal = new bootstrap.Modal( document.getElementById( 'modalQuery' ), {keyboard: false});

	fModalQueryYes = function(){
		myModal.hide();
		fYes();
	};
	fModalQueryNo = fNo !== undefined ? fNo : function(){};
	
	myModal.show();
}

// selection d'un element d'une liste
function modalShowList( sTitle, oItems, sKeyShow, fSelect ){

	// determine si la modale existe dans le DOM
	if( $( '#modalList' ).length == 0 ){
		$( 'body' ).append( '<div id="modalList" class="modal" tabindex="-1"></div>' );
	}

	var sHtml = '<div class="modal-dialog">' +
		'<div class="modal-content">' +
			'<div class="modal-header">' +
				'<h5 class="modal-title">' + sTitle + '</h5>' +
				'<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>' +
			'</div>' +
			'<div class="modal-body">' +
				'<div class="list-group">';
	for( var i=0; i<oItems.length; i++ ){

		sHtml += '<button type="button" indexItem="' + i + '" class="btnItemListModal list-group-item list-group-item-action">' + oItems[ i ][ sKeyShow ] + '</button>';
	}
	sHtml += '</div>' +
			'</div>' +
		'</div>' +
	'</div>';
	$( '#modalList' ).html( sHtml );

	oModalItemList = oItems;
	fModalSelectItemList = fSelect;

	oModalList = new bootstrap.Modal( document.getElementById( 'modalList' ), {keyboard: false});
	oModalList.show();
}

// renseignement d'un champ de saisie texte
function modalShowInput( sTitle, sTitleYes, fYes, sTitleNo, fNo, sValue ){

	// determine si la modale existe dans le DOM
	if( $( '#modalInput' ).length == 0 ){
		$( 'body' ).append( '<div id="modalInput" class="modal" tabindex="-1"></div>' );
	}

	var sHtml = '<div class="modal-dialog">' +
		'<div class="modal-content">' +
			'<div class="modal-header">' +
				'<h5 class="modal-title">' + sTitle + '</h5>' +
				'<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>' +
			'</div>' +
			'<div class="modal-body">' +
				'<input type="text" class="form-control" id="modal-input"/>' +
			'</div>' +
			'<div class="modal-footer">' +
				'<button type="button" id="btnModalInputNo" class="btn btn-secondary" data-bs-dismiss="modal">' + sTitleNo + '</button>' +
				'<button type="button" id="btnModalInputYes" class="btn btn-primary">' + sTitleYes + '</button>' +
			'</div>' +
		'</div>' +
	'</div>';
	$( '#modalInput' ).html( sHtml );

	var oModal = document.getElementById( 'modalInput' );
	var myModal = new bootstrap.Modal( oModal, {keyboard: false});
	oModal.addEventListener('shown.bs.modal', function(){
		if( sValue !== undefined ){
			$( '#modal-input' ).val( sValue );
		}
		$( '#modal-input' ).focus();
	})

	fModalInputYes = function(){
		myModal.hide();
		fYes( $( '#modal-input' ).val() );
	};
	fModalInputNo = fNo !== undefined ? fNo : function(){};
	
	myModal.show();
}

// affichage d'un message
function modalShowMessage( sMessage, sStyle ){

	// determine si la modale existe dans le DOM
	if( $( '#modalMessage' ).length == 0 ){
		$( 'body' ).append( '<div id="modalMessage" class="modal" tabindex="-1"></div>' );
	}

	var sHtml = '<div class="modal-dialog modal-dialog-scrollable modal-xl">' +
		'<div class="modal-content ' + ( sStyle == 'error' ? 'messageErreur' : '' ) + '">' +
			'<div class="modal-body">' +
				sMessage +
			'</div>' +
		'</div>' +
	'</div>';
	$( '#modalMessage' ).html( sHtml );

	var oModalMessage = new bootstrap.Modal( document.getElementById( 'modalMessage' ), {keyboard: false});
	oModalMessage.show();
}

// affichage d'une notification
function notifyShowMessage( sTitle, sMessage, sStyle ){

	// determine si la modale existe dans le DOM
	if( $( '#notifyMessage' ).length == 0 ){
		$( 'body' ).append( '<div class="position-fixed bottom-0 end-0 p-3" style="z-index: 11">' +
			'<div id="notifyMessage" class="toast hide" role="alert" aria-live="assertive" aria-atomic="true">' +
			'</div>' +
		'</div>' );
	}

	var sHtml = '<div class="toast-header">' +
			'<i class="fa-solid fa-comment"></i> ' +
			'<strong class="me-auto">' + sTitle + '</strong>' +
			'<small>11 mins ago</small>' +
			'<button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>' +
		'</div>' +
		'<div class="toast-body">' +
			sMessage +
		'</div>';
	$( '#notifyMessage' ).html( sHtml );

	var oNotifyMessage = new bootstrap.Toast( document.getElementById( 'notifyMessage' ), {autohide: true, delay: 2000} );
	oNotifyMessage.show();
}

// affichage d'un formulaire
function modalShowForm( sTitle, sTitleYes, fYes, sTitleNo, fNo, oForm, oOptions ){

	// determine si la modale existe dans le DOM
	if( $( '#modalShowForm' ).length == 0 ){
		$( 'body' ).append( '<div id="modalShowForm" class="modal" tabindex="-1"></div>' );
	}

	// construction du formulaire
	var sForm = '';
	for( var i=0; i<oForm.length; i++ ){
		var oEle = oForm[ i ];
		if( oEle[ 'type' ] == 'string' ){
			sForm += '<div class="mb-3">' +
				'<label for="modalShowForm_' + oEle[ 'name' ] + '" class="form-label">' + oEle[ 'title' ] + '</label>' +
				'<input type="text" class="form-control" id="modalShowForm_' + oEle[ 'name' ] + '">' +
			'</div>';
		}else if( oEle[ 'type' ] == 'text' ){
			sForm += '<div class="mb-3">' +
				'<label for="modalShowForm_' + oEle[ 'name' ] + '" class="form-label">' + oEle[ 'title' ] + '</label>' +
				'<textarea class="form-control" id="modalShowForm_' + oEle[ 'name' ] + '" rows="3">' + ( oEle[ 'value' ] != undefined ? oEle[ 'value' ] : '' ) + '</textarea>' +
			'</div>';
		}else if( oEle[ 'type' ] == 'checkbox' ){
			sForm += '<div class="mb-3">' +
				'<div class="form-check">' +
					'<input type="checkbox" class="form-check-input" id="modalShowForm_' + oEle[ 'name' ] + '"' + ( oEle[ 'value' ] != undefined && oEle[ 'value' ] ? ' checked="checked"' : '' ) + '>' +
					'<label for="modalShowForm_' + oEle[ 'name' ] + '" class="form-check-label">' + oEle[ 'title' ] + '</label>' +
				'</div>' +
			'</div>';
		}else if( oEle[ 'type' ] == 'set-file' ){
			sForm += '<div class="mb-3">' +
				'<div class="form-check">' +
					'<label for="modalShowForm_' + oEle[ 'name' ] + '" class="form-label">' + oEle[ 'title' ] + '</label>' +
					'<button type="button" fileext="' + oEle[ 'ext' ] + '" filetitle="' + oEle[ 'ext-title' ] + '" idtarget="modalShowForm_' + oEle[ 'name' ] + '" class="app-btn-set-file btn btn-primary btn-sm" style="float:right;"><i class="fa-solid fa-file-lines"></i></button>' +
					'<input type="text" class="form-control" id="modalShowForm_' + oEle[ 'name' ] + '"' + ( oEle[ 'value' ] != undefined ? ' value="' + oEle[ 'value' ] + '"' : '' ) + '>' +
				'</div>' +
			'</div>';
		}else if( oEle[ 'type' ] == 'set-dir' ){
			sForm += '<div class="mb-3">' +
				'<div class="form-check">' +
					'<label for="modalShowForm_' + oEle[ 'name' ] + '" class="form-label">' + oEle[ 'title' ] + '</label>' +
					'<button type="button" filetitle="' + oEle[ 'ext-title' ] + '" idtarget="modalShowForm_' + oEle[ 'name' ] + '" class="app-btn-set-dir btn btn-primary btn-sm" style="float:right;"><i class="fa-solid fa-file-lines"></i></button>' +
					'<input type="text" class="form-control" id="modalShowForm_' + oEle[ 'name' ] + '"' + ( oEle[ 'value' ] != undefined ? ' value="' + oEle[ 'value' ] + '"' : '' ) + '>' +
				'</div>' +
			'</div>';
		}else if( oEle[ 'type' ] == 'list' ){
			var sList = '';
			for( var a=0; a<oEle[ 'value' ].length; a++ ){
				sList += '<option value="' + oEle[ 'value' ][ a ][ oEle[ 'k-key' ] ] + '">' + oEle[ 'value' ][ a ][ oEle[ 'k-value' ] ] + '</option>';
			}
			sForm += '<div class="mb-3">' +
				'<label for="modalShowForm_' + oEle[ 'name' ] + '" class="form-label">' + oEle[ 'title' ] + '</label>' +
				'<select class="form-select" id="modalShowForm_' + oEle[ 'name' ] + '">' +
					sList +
				'</select>' +
			'</div>';
		}else if( oEle[ 'type' ] == 'save-as' ){
			sForm += '<div class="mb-3">' +
				'<label for="modalShowForm_' + oEle[ 'name' ] + '" class="form-label">' + oEle[ 'title' ] + '</label>' +
				'<button type="button" fileext="' + oEle[ 'ext' ] + '" filetitle="' + oEle[ 'ext-title' ] + '" initialfile="' + oEle[ 'initial-file' ] + '" idtarget="modalShowForm_' + oEle[ 'name' ] + '" class="app-btn-save-as btn btn-primary btn-sm" style="float:right;"><i class="fa-solid fa-file-lines"></i></button>' +
				'<input type="text" class="form-control" id="modalShowForm_' + oEle[ 'name' ] + '">' +
			'</div>';
		}
	}

	var sClassBtnOk = 'primary';
	if( oOptions != undefined && oOptions[ 'class-btn-ok' ] != undefined ){
		sClassBtnOk = oOptions[ 'class-btn-ok' ];
	}

	var sHtml = '<div class="modal-dialog">' +
		'<div class="modal-content">' +
			'<div class="modal-header">' +
				'<h5 class="modal-title">' + sTitle + '</h5>' +
				'<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>' +
			'</div>' +
			'<div class="modal-body">' +
				sForm +
				'<div id="modalShowFormError" class="alert alert-danger" style="display:none;" role="alert"></div>' +
			'</div>' +
			'<div class="modal-footer">' +
				'<button type="button" id="btnModalFormNo" class="btn btn-secondary" data-bs-dismiss="modal">' + sTitleNo + '</button>' +
				'<button type="button" id="btnModalFormYes" class="btn btn-' + sClassBtnOk + '">' + sTitleYes + '</button>' +
			'</div>' +
		'</div>' +
	'</div>';
	$( '#modalShowForm' ).html( sHtml );

	var oModalForm = new bootstrap.Modal( document.getElementById( 'modalShowForm' ), {keyboard: false});

	fModalFormYes = function(){

		// recuperation des valeurs du formulaire
		var oData = {};
		for( var i=0; i<oForm.length; i++ ){
			if( oForm[ i ][ 'type' ] == 'checkbox' ){
				oData[ oForm[ i ][ 'name' ] ] = $( '#modalShowForm_' + oForm[ i ][ 'name' ] ).is( ':checked' );
			}else{
				oData[ oForm[ i ][ 'name' ] ] = $( '#modalShowForm_' + oForm[ i ][ 'name' ] ).val();
			}
		}

		var resultValidation = fYes( oData );
		if( resultValidation === true ){
			oModalForm.hide();
		}else{
			$( '#modalShowFormError' ).html( resultValidation ).show();
		}
	};
	fModalFormNo = fNo !== null ? fNo : function(){};
	
	oModalForm.show();
}