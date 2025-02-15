from abc import ABC


from abc_helper import abc_property, abc_method
from utils.print_configuration import print_configuration
from utils.set_value import set_value


class GetResponseMixin(ABC):

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    # Atribut pro zaznamenání vybraného klíče
    selected_key = abc_property("selected_key")

    # Atribut pro zaznamenání vybrané hodnoty pro daný klíče
    selected_value = abc_property("selected_key")

    # Metoda která přepne menu na nové menu
    display_menu = abc_method("display_menu")

    # Metoda načte a zobrazí aktuální nabídku interaktivního menu
    run_menu = abc_method("run_menu")

    # Metoda umožňující ruční zadání int hodnoty (0 - 1000)
    input_custom_int_value = abc_method("input_custom_int_value")


    def get_response(self):
        """Vrací výstupní reakci na daný požadavek"""

        # Pokud je požadavek na vytištění konfigurace
        if self.response == "print_configuration":
            self.print_configuration_response()

        # Pokud je požadavek na změnu konfigurace
        elif self.response == "set_value":
            self.set_value_response()

        # Pokud je požadavek na změnu konfigurace
        elif self.response == "print_new":
            self.print_new_response()

        # Pokud je požadavek na změnu konfigurace
        elif self.response == "input_custom_int_value":
            self.input_custom_value_response()


    def print_configuration_response(self):
        print_configuration()
        self.response = None

    def set_value_response(self):
        set_value()

    def print_new_response(self):
        print(f"Vybrán klíč: {self.selected_key}, hodnota: {self.selected_value}")
        print()
        self.selected_key = None
        self.selected_value = None
        self.response = None

    def input_custom_value_response(self):
        self.input_custom_int_value()

