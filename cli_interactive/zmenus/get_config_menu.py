from abc import ABC

from abc_helper import abc_method

class GetConfigMenuMixin(ABC):

    # Metoda která přepne menu na nové menu
    switch_menu = abc_method("switch_menu")

    def get_config_menu(self):
        """# Vrací data (nadpis a položky) pro konfigurační menu."""
        title = "▼ VYBERTE ÚKON: "
        items = [
            ("Nastavit hodnotu 1", lambda: self.switch_menu("select_key_menu")),
            ("Nastavit hodnotu 2", self.no_methods_yet),
            ("Nastavit hodnotu 3", self.no_methods_yet),
            ("Zpět do hlavního menu", lambda: self.switch_menu("main_menu"))
        ]
        return title, items


    def no_methods_yet(self):
        print("Požadovaný úkon nemá ještě definovaný kod")
        pass