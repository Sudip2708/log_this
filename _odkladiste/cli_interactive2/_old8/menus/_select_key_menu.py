from abc import ABC

from abc_helper import abc_property, abc_method


class SelectKeyMenuMixin(ABC):

    # Atribut pro zaznamenání vybraného klíče
    selected_key = abc_property("selected_key")

    # Metoda která přepne menu na nové menu
    show_menu = abc_method("show_menu")

    def select_key_menu(self):
        """Vrací data (nadpis a položky) pro menu pro výběr klíče."""

        # Vymazání hodnot pro klíč a hodnotu
        self.selected_key = None

        title = "VYBERTE KLÍČ:"
        items = [
            ("key_1", lambda: self.switch_to_set_key("key_1")),
            ("key_2", lambda: self.switch_to_set_key("key_2")),
            ("key_3", lambda: self.switch_to_set_key("key_3")),
            ("Zpět do konfiguračního menu", lambda: self.show_menu("config_menu"))
        ]
        selected = 0
        return title, items, selected


    def switch_to_set_key(self, key=None):
        """Uloží vybraný klíč a přepne na výběr hodnoty."""
        if key:
            self.selected_key = key
            self.show_menu("select_value_menu")
        else:
            print("Není vybrán žádný klíč, zadejte klíč prosím znovu.")
            self.show_menu("select_key_menu")

