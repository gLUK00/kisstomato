# coding=utf-8
import argparse

# kisstomato-script-import-start-user-code-kisstomato
# kisstomato-script-import-stop-user-code-kisstomato

"""
{{ o.getDesc() }}
"""

# kisstomato-script-init-start-user-code-kisstomato
# kisstomato-script-init-stop-user-code-kisstomato

&&  if o.printDescOnStart()
print( "{{ o.getDesc() | replace( "\n", "\\n" ) }}" )

&&  endif

&&  if o.getArgs() | length > 0
# recuperation des arguments
oParser = argparse.ArgumentParser( prog="{{ o.getName() }}", description="{{ o.getDesc() | replace( "\n", "\\n" ) }}" )

# kisstomato-script-arg-start-start-user-code-kisstomato
# kisstomato-script-arg-start-stop-user-code-kisstomato

&&    for oArg in o.getArgs()

# kisstomato-script-arg-{{ oArg[ 'name' ] }}-a-start-user-code-kisstomato
# kisstomato-script-arg-{{ oArg[ 'name' ] }}-a-stop-user-code-kisstomato
oParser.add_argument( "--{{ oArg[ 'name' ] }}"{% if oArg[ 'require' ] %}, required=True{% endif %} )
# kisstomato-script-arg-{{ oArg[ 'name' ] }}-b-start-user-code-kisstomato
# kisstomato-script-arg-{{ oArg[ 'name' ] }}-b-stop-user-code-kisstomato

&&      endfor

&& if o.implementSwitchSection()
sSwitchSection = None
oParser.add_argument("--goto", required=False, help="Label de section vers laquelle sauter directement")
&& endif
oArgs = oParser.parse_args()

&& if o.implementSwitchSection()

# Gestion de l'argument facultatif --goto
oSection = []
&&     for oSection in o.getSections()
oSection.append( "section_{{ oSection[ 'name' ] }}" )
&&     endfor

if hasattr(oArgs, "goto") and oArgs.goto:
    if oArgs.goto not in oSection:
        print(f"Erreur: le label '{oArgs.goto}' n'existe pas. Labels valides : {oSection}")
        exit(1)
    else:
        sSwitchSection = oArgs.goto

&& endif



# kisstomato-script-arg-end-start-user-code-kisstomato
# kisstomato-script-arg-end-stop-user-code-kisstomato

&&  endif

&& for oF in o.getFunctions()

# {{ oF.desc }}
&&  if oF.args|length > 0
# Argument{% if oF.args|length > 1 %}s{% endif %} :
&&      for oArg in oF.args
# - {{ oArg[ 'name' ] }} : {{ oArg[ 'type' ] }} : {% if oArg[ 'require' ] %}(obligatoire) {% else %}(facultatif) {% endif %}{{ oArg[ 'desc' ] }}
&&      endfor
&&  endif
def {{ oF.name }}({% for oArg in oF.args %}{{ oArg[ 'name' ] }}{% if not oArg[ 'require' ] %}=None{% endif %}{{ "" if loop.last else ", " }}{% endfor %}):
&&      if oF[ 'return' ] and oF[ 'return' ] != 'none'
    oResult = None

&&      endif

    # kisstomato-methode-{{ oF.name }}-start-user-code-kisstomato
    # kisstomato-methode-{{ oF.name }}-stop-user-code-kisstomato

&&      if oF[ 'return' ] and oF[ 'return' ] != 'none'
    return oResult

&&      endif
&& endfor

&&  if o.getSections() | length > 0
&&    for oSection in o.getSections()

&&        if o.implementSwitchSection()
if sSwitchSection is None or sSwitchSection == "section_{{ oSection[ 'name' ] }}":
    
&&        endif
{% if o.implementSwitchSection() %}    {% endif %}"""
{% if o.implementSwitchSection() %}    {% endif %}{{ oSection[ 'desc' ] }}
{% if o.implementSwitchSection() %}    {% endif %}"""
{% if o.implementSwitchSection() %}    {% endif %}print( "\n>> {{ oSection[ 'desc' ] | replace( "\n", "\\n" ) | upper }}\n" )
{% if o.implementSwitchSection() %}    {% endif %}# kisstomato-script-section-{{ oSection[ 'name' ] }}-start-user-code-kisstomato
{% if o.implementSwitchSection() %}    {% endif %}# kisstomato-script-section-{{ oSection[ 'name' ] }}-stop-user-code-kisstomato
&&        if o.implementSwitchSection()
    sSwitchSection = None

&&        endif

&&      endfor
&&  endif

# kisstomato-script-end-start-user-code-kisstomato
# kisstomato-script-end-stop-user-code-kisstomato