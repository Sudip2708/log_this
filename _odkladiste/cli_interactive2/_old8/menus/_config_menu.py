from abc import ABC

from abc_helper import abc_property, abc_method

class ConfigMenuMixin(ABC):

    # Metoda která přepne menu na nové menu
    show_menu = abc_method("show_menu")


    def config_menu(self):
        """# Vrací data (nadpis a položky) pro konfigurační menu."""

        title = "VYBERTE ÚKON:"
        items = [
            ("Nastavit hodnotu 1", lambda: self.show_menu("select_key_menu")),
            ("Nastavit hodnotu 2", self.no_methods_yet),
            ("Nastavit hodnotu 3", self.no_methods_yet),
            ("Zpět do hlavního menu", lambda: self.show_menu("main_menu"))
        ]
        selected = 0
        return title, items, selected

    def no_methods_yet(self):
        print("Požadovaný úkon nemá ještě definovaný kod")
        pass

