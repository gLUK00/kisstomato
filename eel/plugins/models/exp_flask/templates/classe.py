# kisstomato-class-import-start-user-code-kisstomato
# kisstomato-class-import-stop-user-code-kisstomato

"""
{{ o.getDesc() }}
"""

class {{ o.getName() }}:

    # kisstomato-class-properties-start-user-code-kisstomato
    # kisstomato-class-properties-stop-user-code-kisstomato

    def __init__(self{% if o.getArgsInit()|length > 0 %}{% for oArg in o.getArgsInit() %}, {{ oArg[ 'name' ] }}{% if not oArg[ 'require' ] %}=None{% endif %}{% endfor %}{% endif %}):
        # kisstomato-class-init-start-user-code-kisstomato
        pass
        # kisstomato-class-init-stop-user-code-kisstomato

&& for oF in o.getMethodes()
    """
    {{ oF.desc }}
    """
&&  if oF.args|length > 0
# Argument{% if oF.args|length > 1 %}s{% endif %} :
&&      for oArg in oF.args
# - {{ oArg[ 'name' ] }} : {{ oArg[ 'type' ] }} : {% if oArg[ 'require' ] %}(obligatoire) {% else %}(facultatif) {% endif %}{{ oArg[ 'desc' ] }}
&&      endfor
&&  endif
    def {{ oF.name }}(self{% if oF.args|length > 0 %}{% for oArg in oF.args %}, {{ oArg[ 'name' ] }}{% if not oArg[ 'require' ] %}=None{% endif %}{% endfor %}{% endif %}):
&&      if oF[ 'return' ] and oF[ 'return' ] != 'none'
        oResult = None

&&      endif

        # kisstomato-class-methode-{{ oF.name }}-start-user-code-kisstomato
        pass
        # kisstomato-class-methode-{{ oF.name }}-stop-user-code-kisstomato

&&      if oF[ 'return' ] and oF[ 'return' ] != 'none'
        return oResult
&&      endif
&& endfor
        
