from abc import ABC

from abc_helper import abc_property, abc_method

class GetMenuAttributesMixin(ABC):

    # Atribut pro zaznamenání nadpisu zobrazeného menu
    menu_title = abc_property("menu_title")

    # Atribut pro zaznamenání položek zobrazeného menu
    menu_items = abc_property("menu_items")

    # Atribut pro zaznamenání jaké menu má být zobrazeno
    menu_name = abc_property("menu_name")

    # Metoda která na základě menu_name vrátí jeho menu_title a menu_items
    get_menu_data = abc_method("get_menu_data", "menu_name")


    def get_menu_attributes(self):
        """Na základě 'menu_name' vrátí obsah pro 'menu_title' a 'menu_items'"""

        self.menu_title, self.menu_items = self.get_menu_data(self.menu_name)


