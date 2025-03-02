from abc import ABC

from abc_helper import abc_method


class EndingMenuMixin(ABC):

    # Metoda která přepne manu na nové menu
    show_menu = abc_method("show_menu")

    # Metoda která ukončí aktuální menu
    exit_menu = abc_method("exit_menu")

    def ending_menu(self):
        """Vrací data (položky) pro ukončovací menu"""
        title = None
        items = [
            ("Pokračovat v interaktivním režimu", lambda: self.show_menu("main_menu")),
            ("Ukončit interaktivní režim", self.exit_menu)
        ]
        selected = 0
        return title, items, selected
