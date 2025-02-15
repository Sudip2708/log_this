from abc import ABC

from abc_helper import abc_property, abc_method

class GetMenuDataMixin(ABC):

    # Atribut pro zaznamenání jaké menu má být zobrazeno
    menu_name = abc_property("menu_name")

    # Metoda která vrací data (nadpis a položky) pro hlavní menu.
    get_main_menu = abc_method("get_main_menu")

    # Metoda která vrací data (položky) pro ukončovací menu
    get_ending_menu = abc_method("get_ending_menu")

    # Metoda která vrací data (nadpis a položky) pro konfigurační menu
    get_config_menu = abc_method("get_config_menu")

    # Metoda která vrací data (nadpis a položky) pro menu pro výběr klíče
    get_select_key_menu = abc_method("get_select_key_menu")

    # Metoda která vrací data (nadpis a položky) pro menu pro výběr hodnoty pro daný klíč
    get_select_value_menu = abc_method("get_select_value_menu")


    def get_menu_data(self):
        """Na základě 'menu_name' načte data pro požadované menu"""

        menus_dict = {
            "main_menu": self.get_main_menu,
            "ending_menu": self.get_ending_menu,
            "config_menu": self.get_config_menu,
            "select_key_menu": self.get_select_key_menu,
            "select_value_menu": self.get_select_value_menu,
        }

        if self.menu_name in menus_dict:
            return menus_dict[self.menu_name]()

        # if self.menu_name == "main_menu":
        #     return self.get_main_menu()
        #
        # elif self.menu_name == "ending_menu":
        #     return self.get_ending_menu()
        #
        # elif self.menu_name == "config_menu":
        #     return self.get_config_menu()
        #
        # elif self.menu_name == "select_key_menu":
        #     return self.get_select_key_menu()
        #
        # elif self.menu_name == "select_value_menu":
        #     return self.get_select_value_menu()


