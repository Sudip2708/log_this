from .menus.get_main_menu import GetMainMenuMixin
from .menus.get_config_menu import GetConfigMenuMixin
from .menus.get_ending_menu import GetEndingMenuMixin
from .menus.get_select_key_menu import GetSelectKeyMenuMixin
from .menus.get_select_value_menu import GetSelectKValueMenuMixin

class GetMenuItems(
    GetMainMenuMixin,
    GetConfigMenuMixin,
    GetEndingMenuMixin,
    GetSelectKeyMenuMixin,
    GetSelectKValueMenuMixin,
):

    # Funkce pro navrácení menu dle požadovaného typu menu
    def get_menu_items(self, menu_type):

        # Definice menu položek podle typu menu
        if menu_type == "main_menu":
            return self.get_main_menu()

        elif menu_type == "config_menu":
            return self.get_config_menu()

        elif menu_type == "ending_menu":
            return self.get_ending_menu()

        elif menu_type == "select_key_menu":
            return self.get_select_key_menu()

        elif menu_type == "select_value_menu":
            return self.get_select_value_menu()


