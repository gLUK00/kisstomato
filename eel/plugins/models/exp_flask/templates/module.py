# kisstomato-module-import-start-user-code-kisstomato
# kisstomato-module-import-stop-user-code-kisstomato

"""
{{ o.getDesc() }}
"""

# kisstomato-module-properties-start-user-code-kisstomato
# kisstomato-module-properties-stop-user-code-kisstomato

&& for oF in o.getFunctions()

"""
{{ oF.desc }}
"""
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
&&      if oF[ 'exception' ]
    try:
&&      endif

{% if oF[ 'exception' ] %}    {% endif %}    # kisstomato-methode-{{ oF.name }}-start-user-code-kisstomato
{% if oF[ 'exception' ] %}    {% endif %}    pass
{% if oF[ 'exception' ] %}    {% endif %}    # kisstomato-methode-{{ oF.name }}-stop-user-code-kisstomato

&&      if oF[ 'exception' ]
    except Exception as e:
        # kisstomato-methode-exception-{{ oF.name }}-start-user-code-kisstomato
        print( e )
        # kisstomato-methode-exception-{{ oF.name }}-stop-user-code-kisstomato
            
    # kisstomato-methode-finally-{{ oF.name }}-start-user-code-kisstomato
    # kisstomato-methode-finally-{{ oF.name }}-stop-user-code-kisstomato 
&&      endif

&&      if oF[ 'return' ] and oF[ 'return' ] != 'none'
    return oResult

&&      endif
&& endfor

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato