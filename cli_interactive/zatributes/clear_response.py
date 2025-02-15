from abc import ABC

from abc_helper import abc_property

class ClearResponseMixin(ABC):

    # Atribut pro zaznamenání požadavku na odpověď z interaktivního menu
    response = abc_property("response")

    def clear_response(self):
        """Metoda přepíše obsah atributu 'response' na None"""
        self.response = None