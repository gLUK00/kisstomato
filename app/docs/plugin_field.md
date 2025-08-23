# Documentation des Plugins de Type "Fields" pour Kisstomato Studio

Les plugins de type "Fields" permettent d'étendre l'interface de Kisstomato Studio avec des types de champs personnalisés pour la saisie et l'affichage de données. Ces champs peuvent ensuite être utilisés dans les modèles de projets gérés par Kisstomato Studio.

## Objectif

L'objectif principal d'un plugin "Field" est de fournir une interface utilisateur spécifique pour un type de donnée particulier, allant au-delà des champs HTML standards. Par exemple, un sélecteur de couleur, un éditeur Markdown, un champ pour générer un QR Code, etc.

## Structure d'un Plugin "Field"

Chaque plugin "Field" doit être placé dans son propre répertoire à l'intérieur de `eel/plugins/fields/`. Le nom de ce répertoire devient l'identifiant unique du plugin (`<pluginName>`).

eel/ └── plugins/ └── fields/ └──


## Composants Principaux

### 1. `field.js` (Obligatoire)

Ce fichier est le cœur du comportement frontend du plugin. Il doit définir plusieurs fonctions JavaScript qui seront appelées par l'application Kisstomato Studio à différents moments du cycle de vie du champ.

**Convention de Nommage des Fonctions :** `pluginField<Action>_<pluginName>`

**Fonctions Requises :**

*   `pluginFieldGetHtml_<pluginName>(sIdField, oField)`
    *   **Rôle :** Générer et retourner la structure HTML du champ pour le mode édition.
    *   **Paramètres :**
        *   `sIdField` (String) : Un identifiant unique pour cette instance spécifique du champ. Cet ID doit être utilisé pour les éléments HTML principaux afin d'éviter les conflits.
        *   `oField` (Object) : Un objet contenant les propriétés du champ (par exemple, `oField.value` pour la valeur actuelle, `oField.name`, etc.).
    *   **Retourne :** (String) La chaîne HTML représentant le champ.

*   `pluginFieldAfterHtml_<pluginName>(sIdField, oField)`
    *   **Rôle :** Exécuter du code JavaScript après que le HTML du champ a été inséré dans le DOM. Utile pour initialiser des bibliothèques JavaScript, attacher des écouteurs d'événements, etc.
    *   **Paramètres :** Les mêmes que `pluginFieldGetHtml_<pluginName>`.

*   `pluginFieldSetView_<pluginName>(sIdField, oField)`
    *   **Rôle :** Modifier l'apparence du champ pour un mode lecture seule (non éditable).
    *   **Paramètres :** Les mêmes que `pluginFieldGetHtml_<pluginName>`.
    *   **Exemple :** Désactiver les champs de saisie, masquer les boutons d'édition.

*   `pluginFieldForm2val_<pluginName>(sIdField, oField)`
    *   **Rôle :** Récupérer la valeur actuelle du champ à partir de son état dans le DOM.
    *   **Paramètres :** Les mêmes que `pluginFieldGetHtml_<pluginName>`.
    *   **Retourne :** La valeur actuelle du champ (type dépendant du champ : String, Number, Object, etc.).

**Exemple Basé sur le Plugin `qrcode` :**

```javascript
// Dans eel/plugins/fields/qrcode/field.js

var _oQrCodes = {}; // Stockage des instances QRCode

// Generation du visuel (edition)
window[ 'pluginFieldGetHtml_qrcode' ] = function( sIdField, oField ){
    if( oField.value == undefined ){
        oField.value = sIdField; // Valeur par défaut si non définie
    }
    return '<div id="' + sIdField + '">' +
        '<input type="text" value="' + oField.value + '" class="form-control field_qrcode" style="margin-bottom:5px"/>' +
        '<div id="qrcode_' + sIdField + '"></div>' + // Conteneur pour le QR Code
    '</div>';
}

// Execution apres la generation du HTML
window[ 'pluginFieldAfterHtml_qrcode' ] = function( sIdField, oField ){
    // Initialisation de la bibliothèque QRCode (supposée chargée)
    _oQrCodes[ sIdField ] = new QRCode( document.getElementById( 'qrcode_' + sIdField ), oField.value );
}

// Passage du visuel en mode "view"
window[ 'pluginFieldSetView_qrcode' ] = function( sIdField, oField ){
    $( '#' + sIdField ).find( 'input' ).prop( "disabled", true );
}

// Recuperation de la valeur en fonction du visuel
window[ 'pluginFieldForm2val_qrcode' ] = function( sIdField, oField ){
    return $( '#' + sIdField ).find( 'input' ).val();
}

// Gestionnaire d'événements spécifique au plugin qrcode
$( document ).on( "change", ".field_qrcode", function() {
    var sIdField = $( this ).closest( 'div' ).attr( 'id' );
    _oQrCodes[ sIdField ].clear();
    _oQrCodes[ sIdField ].makeCode( $( this ).val() );
} );
