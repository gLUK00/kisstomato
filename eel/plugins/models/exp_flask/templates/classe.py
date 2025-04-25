# kisstomato-class-import-start-user-code-kisstomato
# kisstomato-class-import-stop-user-code-kisstomato

"""
{{ o.getDesc() }}
"""

class {{ o.getName() }}:
    # kisstomato-class-properties-start-user-code-kisstomato
    # kisstomato-class-properties-stop-user-code-kisstomato
    def __init__(self, required_arg, optional_arg=None):
        """
        Constructeur de la classe.

        :param required_arg: Argument obligatoire.
        :param optional_arg: Argument facultatif (par défaut None).
        """
        self.required_arg = required_arg
        self.optional_arg = optional_arg

    def method_with_required_arg(self, required_arg):
        """
        Méthode avec un argument obligatoire.

        :param required_arg: Argument obligatoire.
        """
        print(f"Argument obligatoire: {required_arg}")

    def method_with_optional_arg(self, required_arg, optional_arg="default_value"):
        """
        Méthode avec un argument obligatoire et un argument facultatif.

        :param required_arg: Argument obligatoire.
        :param optional_arg: Argument facultatif (par défaut 'default_value').
        """
        print(f"Argument obligatoire: {required_arg}")
        print(f"Argument facultatif: {optional_arg}")


# Exemple d'utilisation
example = ExampleClass("valeur_obligatoire", optional_arg="valeur_facultative")
example.method_with_required_arg("valeur_obligatoire")
example.method_with_optional_arg("valeur_obligatoire", optional_arg="autre_valeur")