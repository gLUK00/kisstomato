import argparse

# kisstomato-script-import-start-user-code-kisstomato
# kisstomato-script-import-stop-user-code-kisstomato

"""
{{ o.getDesc() }}
"""

&&  if o.printDescOnStart()
print( "{{ o.getDesc() | replace( "\n", "\\n" ) }}" )

&&  endif

&&  if o.getArgs() | length > 0
# recuperation des arguments
oParser = argparse.ArgumentParser( prog="{{ o.getName() }}", description="{{ o.getDesc() | replace( "\n", "\\n" ) }}" )

# kisstomato-script-arg-start-start-user-code-kisstomato
# kisstomato-script-arg-start-stop-user-code-kisstomato

&&    for oArg in o.args

# kisstomato-script-arg-{{ oArg[ 'name' ] }}-a-start-user-code-kisstomato
# kisstomato-script-arg-{{ oArg[ 'name' ] }}-a-stop-user-code-kisstomato
oParser.add_argument( "--{{ oArg[ 'name' ] }}"{% if oArg[ 'require' ] %}, required=True{% endif %} )
# kisstomato-script-arg-{{ oArg[ 'name' ] }}-b-start-user-code-kisstomato
# kisstomato-script-arg-{{ oArg[ 'name' ] }}-b-stop-user-code-kisstomato

&&      endfor
oArgs = oParser.parse_args()

# kisstomato-script-arg-end-start-user-code-kisstomato
# kisstomato-script-arg-end-stop-user-code-kisstomato

&&  endif

# arguments

# fonctions
#   arguments


"""
oParser = argparse.ArgumentParser( prog="importation", description="Batch d'importation de l'historique des transactions" )
oParser.add_argument( "--pair", required=True )
oArgs = oParser.parse_args()


print( oArgs )
"""