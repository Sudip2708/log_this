from abc import ABC

from abc_helper import abc_property, abc_method


class GetSelectValueMenuMixin(ABC):

    # Atribut pro zaznamenání vybraného klíče
    selected_key = abc_property("selected_key")

    # Atribut pro zaznamenání vybrané hodnoty pro daný klíče
    selected_value = abc_property("selected_key")

    # Metoda která přepne menu na nové menu
    switch_menu = abc_method("switch_menu")

    # Metoda která nastaví atribut 'response' na 'print_configuration' a ukončí menu
    set_response = abc_method("set_response")


    def get_select_value_menu(self):
        """Vrací data (nadpis a položky) pro menu pro výběr hodnoty pro daný klíč."""
        title = f"▼ VYBERTE HODNOTU PRO {self.selected_key.upper()}: "
        items = [
            ("value_1", lambda: self.set_value_and_print("value_1")),
            ("value_2", lambda: self.set_value_and_print("value_2")),
            ("value_3", lambda: self.set_value_and_print("value_3")),
            ("Zadat vlastní hodnotu", self.input_custom_value),
            ("Zpět na výběr klíče", self.switch_menu("select_key_menu"))
        ]
        return title, items


    def set_value_and_print(self, value):
        """Uloží vybranou hodnotu, vypíše výsledek a vrátí se do hlavního menu."""
        self.selected_value = value
        self.set_response("print_new")


    def input_custom_value(self):
        """Zobrazí vstupní dialog pro zadání vlastní hodnoty."""
        self.set_response("input_custom_value")
