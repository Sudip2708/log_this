from abc import ABC, abstractmethod
from .menus.get_main_menu import GetMainMenuMixin
from .menus.get_config_menu import GetConfigMenuMixin
from .menus.get_ending_menu import GetEndingMenuMixin
from .menus.get_select_key_menu import GetSelectKeyMenuMixin
from .menus.get_select_value_menu import GetSelectKValueMenuMixin
from .handlers import (
    HandlersMixin,
    SwitchToMainMixin,
    SwitchToConfigMenuMixin,
    SwitchToMSelectKeyMixin,
    SwitchToSetKeyMixin,
    SetValueAndPrintMixin,
    ResetKeyValueMixin,
    InputCustomValueMixin,
    ShowHelpHandlerMixin,
    ShowConfigHandlerMixin,
    SetValueHandlerMixin,
    ExitHandlerMixin,
)



class GetMenuItems(
    SwitchToMainMixin,
    SwitchToConfigMenuMixin,
    SwitchToMSelectKeyMixin,
    SwitchToSetKeyMixin,
    SetValueAndPrintMixin,
    ResetKeyValueMixin,
    InputCustomValueMixin,
    ShowHelpHandlerMixin,
    ShowConfigHandlerMixin,
    SetValueHandlerMixin,
    ExitHandlerMixin,
    GetMainMenuMixin,
    GetConfigMenuMixin,
    GetEndingMenuMixin,
    GetSelectKeyMenuMixin,
    GetSelectKValueMenuMixin,
    ABC
):

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def switch_menu(self, new_menu_type):
        pass

    @property
    @abstractmethod
    def show_help(self):
        pass

    @show_help.setter
    @abstractmethod
    def show_help(self, value):
        pass

    @property
    @abstractmethod
    def response(self):
        pass

    @response.setter
    @abstractmethod
    def response(self, value):
        pass

    @property
    @abstractmethod
    def selected_key(self):
        pass

    @selected_key.setter
    @abstractmethod
    def selected_key(self, value):
        pass

    @property
    @abstractmethod
    def selected_value(self):
        pass

    @selected_value.setter
    @abstractmethod
    def selected_value(self, value):
        pass


    # Funkce pro navrácení menu dle požadovaného typu menu
    def get_menu_items(self, menu_type):

        # Definice menu položek podle typu menu
        if menu_type == "main":
            return self.get_main_menu()

        elif menu_type == "config_menu":
            return self.get_config_menu()

        elif menu_type == "ending_menu":
            return self.get_ending_menu()

        elif menu_type == "select_key_menu":
            return self.get_select_key_menu()

        elif menu_type == "select_value_menu":
            return self.get_select_value_menu()

    # def switch_to_main(self):
    #     """Přepne zpět na hlavní menu."""
    #     self.switch_menu("main")

    # def switch_to_config_menu(self):
    #     """Přepne do submenu pro nastavení konfigurace."""
    #     self.switch_menu("config_menu")

    # def switch_to_select_key(self):
    #     """Přepne do submenu pro výběr klíče."""
    #     self.reset_key_value()
    #     self.switch_menu("select_key_menu")

    # def switch_to_set_key(self, key=None):
    #     """Uloží vybraný klíč a přepne na výběr hodnoty."""
    #     if key:
    #         self.selected_key = key
    #     if self.selected_key:
    #         self.switch_menu("select_value_menu")
    #     else:
    #         print("Není vybrán žádný klíč, zadejte klíč prosím znovu.")
    #         self.switch_menu("select_key_menu")

    # def set_value_and_print(self, value):
    #     """Uloží vybranou hodnotu, vypíše výsledek a vrátí se do hlavního menu."""
    #     self.selected_value = value
    #     self.response = "print_new"
    #     self.exit()

    def reset_key_value(self):
        """Resetuje hodnoty těchto dvou atributů na None"""
        self.selected_key = None
        self.selected_value = None

    # def input_custom_value(self):
    #     """Zobrazí vstupní dialog pro zadání vlastní hodnoty."""
    #     self.response = "input_custom_value"
    #     self.exit()

    # # Funkce pro zobrazení a skyrytí menu
    # def show_help_handler(self):
    #     self.show_help = not self.show_help

    # # Funkce pro výpis aktuální konfigurace
    # def show_config_handler(self):
    #     self.response = "print_configuration"
    #     self.exit()

    # # Funkce pro nasavení nové konfigurace
    # def set_value_handler(self):
    #     self.response = "set_value"
    #     self.exit()

    # # Funkce pro ukončení interaktivního režimu
    # def exit_handler(self):
    #     self.response = "exit"
    #     self.exit()


