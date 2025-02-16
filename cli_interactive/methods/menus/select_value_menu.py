from abc import ABC

from abc_helper import abc_property, abc_method


class SelectValueMenuMixin(ABC):

    # Atribut pro zaznamenání vybraného klíče
    selected_key = abc_property("selected_key")

    # Atribut pro zaznamenání vybrané hodnoty pro daný klíče
    selected_value = abc_property("selected_key")

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    # Metoda která přepne menu na nové menu
    display_menu = abc_method("display_menu")

    # Metoda uzavře aktuální interaktivní menu
    exit_menu = abc_method("exit")


    def get_select_value_menu(self):
        """Vrací data (nadpis a položky) pro menu pro výběr hodnoty pro daný klíč."""
        title = f"VYBERTE HODNOTU PRO {self.selected_key.upper()}:"
        items = [
            ("value_1", lambda: self.set_value_and_print("value_1")),
            ("value_2", lambda: self.set_value_and_print("value_2")),
            ("value_3", lambda: self.set_value_and_print("value_3")),
            ("Zadat vlastní hodnotu", self.input_custom_value),
            ("Zpět na výběr klíče", self.return_to_key_menu)
        ]
        return title, items


    def set_value_and_print(self, value):
        """Uloží vybranou hodnotu, vypíše výsledek a vrátí se do hlavního menu."""
        self.selected_value = value
        self.response = "print_new"
        self.exit_menu()


    def input_custom_value(self):
        """Zobrazí vstupní dialog pro zadání vlastní hodnoty."""
        self.response = "input_custom_int_value"
        self.exit_menu()

    def return_to_key_menu(self):
        """Metoda přepne na menu pro výběr klíče"""
        self.selected_key = None
        self.display_menu("select_key_menu")
