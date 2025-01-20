# kisstomato-imports-a-start-user-code-kisstomato
# kisstomato-imports-a-stop-user-code-kisstomato

from core import generator

# kisstomato-imports-b-start-user-code-kisstomato
# kisstomato-imports-b-stop-user-code-kisstomato

# {{ o.desc }}
&&  if o.args|length > 0
# Argument{% if o.args|length > 1 %}s{% endif %} :
&&      for oArg in o.args
# - {{ oArg[ 'name' ] }} : {{ oArg[ 'type' ] }} : {% if oArg[ 'require' ] %}(obligatoire) {% endif %}{{ oArg[ 'desc' ] }}
&&      endfor
&&  endif
class {{ o.node[ 'text' ] }}:
    def __init__(self{% for oArg in o.args %}, {{ oArg[ 'name' ] }}{% endfor %}):
&&  for oArg in o.args
        # kisstomato-init-a-start-user-code-kisstomato
        # kisstomato-init-a-stop-user-code-kisstomato

        self.{{ oArg[ 'name' ] }} = {{ oArg[ 'name' ] }}

&&  endfor

        # kisstomato-init-b-start-user-code-kisstomato
        # kisstomato-init-b-stop-user-code-kisstomato

&&  for oM in o.methodes

    # {{ oM.desc }}
&&      if oM.args|length > 0
    # Argument{% if oM.args|length > 1 %}s{% endif %} :
&&          for oArg in oM.args
    # - {{ oArg[ 'name' ] }} : {{ oArg[ 'type' ] }} : {% if oArg[ 'require' ] %}(obligatoire) {% endif %}{{ oArg[ 'desc' ] }}
&&          endfor
&&      endif
    def {{ oM.name }}(self{% for oArg in oM.args %}, {{ oArg[ 'name' ] }}{% endfor %}):

        # kisstomato-methode-{{ oM.name }}-start-user-code-kisstomato
        # kisstomato-methode-{{ oM.name }}-stop-user-code-kisstomato

        return

&&  endfor

    # kisstomato-methodes-a-start-user-code-kisstomato
    # kisstomato-methodes-a-stop-user-code-kisstomato