from abc import ABC

from abc_helper import abc_property, abc_method

class SetResponseMixin(ABC):

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    # Metoda uzavře aktuální interaktivní menu
    exit_menu = abc_method("exit")

    def set_response(self, request):
        """Nastaví atribut 'response' na 'print_configuration' a ukončí menu"""
        self.response = request
        self.exit_menu()
