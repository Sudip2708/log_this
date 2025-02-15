from abc import ABC

from abc_helper import abc_property, abc_method

class GetMenuDataMixin(ABC):

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


    def get_menu_data(self, menu_name):
        """Na základě 'menu_name' načte data pro požadované menu"""

        if menu_name == "main_menu":
            return self.get_main_menu()

        elif menu_name == "ending_menu":
            return self.get_ending_menu()

        elif menu_name == "config_menu":
            return self.get_config_menu()

        elif menu_name == "select_key_menu":
            return self.get_select_key_menu()

        elif menu_name == "select_value_menu":
            return self.get_select_value_menu()


