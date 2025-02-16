from abc import ABC

from abc_helper import abc_property, abc_method


class SelectKeyMenuMixin(ABC):

    # Atribut pro zaznamenání vybraného klíče
    selected_key = abc_property("selected_key")

    # Metoda která přepne menu na nové menu
    display_menu = abc_method("display_menu")

    def get_select_key_menu(self):
        """Vrací data (nadpis a položky) pro menu pro výběr klíče."""
        title = "VYBERTE KLÍČ:"
        items = [
            ("key_1", lambda: self.switch_to_set_key("key_1")),
            ("key_2", lambda: self.switch_to_set_key("key_2")),
            ("key_3", lambda: self.switch_to_set_key("key_3")),
            ("Zpět do konfiguračního menu", lambda: self.display_menu("config_menu"))
        ]
        return title, items


    def switch_to_set_key(self, key=None):
        """Uloží vybraný klíč a přepne na výběr hodnoty."""
        if key:
            self.selected_key = key
            self.display_menu("select_value_menu")
        else:
            print("Není vybrán žádný klíč, zadejte klíč prosím znovu.")
            self.display_menu("select_key_menu")