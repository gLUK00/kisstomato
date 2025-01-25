/*
	{{ o.desc }}
*/

// kisstomato-js-{{ o.name }}-a-start-user-code-kisstomato
// kisstomato-js-{{ o.name }}-a-stop-user-code-kisstomato

&&  for oSection in o.sections
// --------------------------------------------------------------------------
// Section : {{ oSection.name }}
/* {{ oSection.desc }} */
// --------------------------------------------------------------------------

// kisstomato-section-{{ oSection.name }}-start-user-code-kisstomato
// kisstomato-section-{{ oSection.name }}-stop-user-code-kisstomato

&&  endfor

&&  for oFonction in o.fonctions
/* {{ oFonction.desc }} */
&&      if oFonction.args|length > 0
// Argument{% if oFonction.args|length > 1 %}s{% endif %} :
&&          for oArg in oFonction.args
// - {{ oArg[ 'name' ] }} : {{ oArg[ 'type' ] }} : {% if oArg[ 'require' ] %}(obligatoire) {% endif %}{{ oArg[ 'desc' ] }}
&&          endfor
&&      endif
function {{ oFonction.name }}({% for oArg in oFonction.args %}{% if oArg != oFonction.args[ 0 ] %}, {% endif %}{{ oArg[ 'name' ] }}{% endfor %}){
&&          if oFonction[ 'return-val' ]
	let oResult = null;

&&          endif

	// kisstomato-function-{{ oFonction.name }}-start-user-code-kisstomato
	// kisstomato-function-{{ oFonction.name }}-stop-user-code-kisstomato

&&          if oFonction[ 'return-val' ]
	return oResult;
&&          endif
}

&&  endfor

&&  for oR in o.jquerys_ready
/* {{ oR.desc }} */
$( document ).ready( function(){
	// kisstomato-ready-{{ oR.name }}-start-user-code-kisstomato
	// kisstomato-ready-{{ oR.name }}-stop-user-code-kisstomato
} );

&&  endfor

&&  for oO in o.jquerys_on
/* {{ oO.desc }} */
$( document ).on( "{{ oO.event }}", "{{ oO.selector }}", function() {
	// kisstomato-on-{{ oO.name }}-start-user-code-kisstomato
	// kisstomato-on-{{ oO.name }}-stop-user-code-kisstomato
} );

&&  endfor

// kisstomato-js-{{ o.name }}-b-start-user-code-kisstomato
// kisstomato-js-{{ o.name }}-b-stop-user-code-kisstomato