# kisstomato-module-a-start-user-code-kisstomato
# kisstomato-module-a-stop-user-code-kisstomato

import json, os, sys, shutil

from core import generator

# referencement du repertoire parent
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)

from classes import *

# kisstomato-module-b-start-user-code-kisstomato
# kisstomato-module-b-stop-user-code-kisstomato

# {{ o.desc }}

&&  for oF in o.fonctions

# {{ oF.desc }}
&&      if oF.args|length > 0
# Argument{% if oF.args|length > 1 %}s{% endif %} :
&&          for oArg in oF.args
# - {{ oArg[ 'name' ] }} : {{ oArg[ 'type' ] }} : {% if oArg[ 'require' ] %}(obligatoire) {% endif %}{{ oArg[ 'desc' ] }}
&&          endfor
&&      endif
def {{ oF.name }}({% for oArg in oF.args %}{% if oArg != oF.args[ 0 ] %}, {% endif %}{{ oArg[ 'name' ] }}{% endfor %}):
&&              if oF[ 'return-val' ]
    oResult = None

&&              endif
    # kisstomato-fonction-{{ oF.name }}-init-start-user-code-kisstomato
    # kisstomato-fonction-{{ oF.name }}-init-stop-user-code-kisstomato

&&              if oF[ 'exception' ]
    try:
&&              endif

    {% if oF[ 'exception' ] %}    {% endif %}# kisstomato-fonction-{{ oF.name }}-try-start-user-code-kisstomato
    {% if oF[ 'exception' ] %}    {% endif %}pass()
    {% if oF[ 'exception' ] %}    {% endif %}# kisstomato-fonction-{{ oF.name }}-try-stop-user-code-kisstomato

&&              if oF[ 'exception' ]
    except Exception as e:
        # kisstomato-exception-{{ oF.name }}-a-start-user-code-kisstomato
        # kisstomato-exception-{{ oF.name }}-a-stop-user-code-kisstomato
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        # kisstomato-exception-{{ oF.name }}-b-start-user-code-kisstomato
        # kisstomato-exception-{{ oF.name }}-b-stop-user-code-kisstomato

&&              endif

    # kisstomato-return-{{ oF.name }}-return-start-user-code-kisstomato
    # kisstomato-return-{{ oF.name }}-return-stop-user-code-kisstomato
    return{% if oF[ 'return-val' ] %} oResult{% endif %}

&&  endfor

# kisstomato-module-c-start-user-code-kisstomato
# kisstomato-module-c-stop-user-code-kisstomato