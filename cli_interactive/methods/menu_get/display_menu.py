from abc import ABC

from abc_helper import abc_property, abc_method


class DisplayMenuMixin(ABC):

    # Atribut pro zaznamenání jaké menu má být zobrazeno
    menu_name = abc_property("menu_name")

    # Atribut pro zaznamenání vybrané položky
    current_selection = abc_property("current_selection")

    # Metoda která na základě 'menu_name' vrátí obsah pro 'menu_title' a 'menu_items'
    get_menu_attributes = abc_method("get_menu_attributes")

    # Metoda znovu načte data pro vykreselní menu
    reload_menu = abc_method("reload_menu")


    def display_menu(self, new_menu_name):
        """Přepne na nové menu"""

        # Přepsání atributu pro jméno menu
        self.menu_name = new_menu_name

        # Nastavení pozice výběru na první položku
        self.current_selection = 0

        # Volání metody pro načtení dat daného menu
        self.get_menu_attributes()

        # Volání metody pro obnovu pohledu
        self.reload_menu()


