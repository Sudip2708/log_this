from abc import ABC

from abc_helper import abc_method


class EndingMenuMixin(ABC):

    # Metoda která přepne manu na nové menu
    display_menu = abc_method("display_menu")

    # Metoda která ukončí aktuální menu
    exit_menu = abc_method("exit_menu")

    def get_ending_menu(self):
        """Vrací data (položky) pro ukončovací menu"""
        title = None
        items = [
            ("Pokračovat v interaktivním režimu", lambda: self.display_menu("main_menu")),
            ("Ukončit interaktivní režim", self.exit_menu)
        ]
        return title, items
