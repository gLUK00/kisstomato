// sur l'affichage d'un noeud de type "item"
window[ 'formShowItemTypeObject' ] = function( oForm ){

    for( var a=0; a<oForm.length; a++ ){
        if( oForm[ a ].id == 'type' ){

            return oForm[ a ].value == 'object';
        }
    }

    return false;
}