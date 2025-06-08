&& set oArgs = o.getArgs()
&& set sAddImport = ''
&& if oArgs|length > 0
&&  set sAddImport = sAddImport + ', argparse'
&& endif
import os, sys{{ sAddImport }}

&& if o.printDescOnStart()
# commentaire de demarrage
print( "{{ o.getDesc().replace( '"', '\"' ) }}" )

&& endif

# kisstomato-imports-start-user-code-kisstomato
# kisstomato-imports-stop-user-code-kisstomato

&& if oArgs|length > 0
oParser = argparse.ArgumentParser( prog="{{ o.getName().replace( '"', '\"' ) }}", description="{{ o.getDesc().replace( '"', '\"' ) }}" )
&&  for oArg in oArgs
oParser.add_argument( "--{{ oArg[ 'name' ] }}"{% if oArg[ 'require' ] %}, required=True{% endif %} )
&&  endfor
oArgs = oParser.parse_args()


print( oArgs )

&& endif

# kisstomato-main-start-user-code-kisstomato
# kisstomato-main-stop-user-code-kisstomato