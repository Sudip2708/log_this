from abc import ABC

from abc_helper import abc_method


class GetEndingMenuMixin(ABC):

    # Metoda která přepne manu na nové menu
    switch_menu = abc_method("switch_menu")

    # Metoda která ukončí aktuální menu
    exit_menu = abc_method("exit_menu")

    def get_ending_menu(self):
        """Vrací data (položky) pro ukončovací menu"""
        title = None
        items = [
            ("Pokračovat v interaktivním režimu", lambda: self.switch_menu("config_menu")),
            ("Ukončit interaktivní režim", self.exit_menu)
        ]
        return title, items
