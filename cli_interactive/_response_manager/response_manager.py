# print("_response_manager/response_manager.py")
from ._print_configuration import print_configuration
from ._set_value import set_value
from ._print_new_settings import print_new_settings
from ._input_int_value import input_int_value


class ResponseManager:
    """Spravuje reakce na vybrané položky menu"""

    def __init__(self, menus_manager):

        # Přiřazení instance hlavní třídy
        self.menus_manager = menus_manager

        # Definice akcí odezvy
        self.response_actions = {
            "print_configuration": lambda: print_configuration(),
            "set_value": lambda: set_value(),
            "print_new": lambda: print_new_settings(self.menus_manager),
            "input_int_value": lambda: input_int_value(self.menus_manager)
        }

    def __call__(self):
        """Vrací výstupní reakci na daný požadavek"""
        action = self.response_actions.get(self.menus_manager.response)
        if action:
            action()
            self.menus_manager.response = None  # Reset odpovědi





