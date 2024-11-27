import os, sys

"""
{{ o.getDesc() }}
"""
{% if o.printDescOnStart() %}
print( "{{ o.getDesc().replace( '"', '\"' ) }}" )
{% endif %}

# kisstomato-imports-start-user-code-kisstomato
# kisstomato-imports-stop-user-code-kisstomato

{{ o.getArgs() }}

# kisstomato-main-start-user-code-kisstomato
# kisstomato-main-stop-user-code-kisstomato