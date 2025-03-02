from ._main_menu import MainMenuMixin
from ._ending_menu import EndingMenuMixin
from ._config_menu import ConfigMenuMixin
from ._select_key_menu import SelectKeyMenuMixin
from ._select_value_menu import SelectValueMenuMixin
from ._menus_config import MenusConfigMixin
from ._menus_colors_settings import MenusColorsSettingsMixin
from ._menus_symbols_settings import MenusSymbolsSettingsMixin

__all__ = [
    "MainMenuMixin",  # main_menu()
    # Vrací data (nadpis a položky) pro hlavní menu.
    # Používá atributy: 'show_instruction'
    # Používá metody: show_menu(), exit_menu()

    "EndingMenuMixin",  # ending_menu()
    # Vrací data (položky) pro ukončovací menu
    # Používá metody: show_menu(), exit_menu()

    "ConfigMenuMixin",  # config_menu()
    # Vrací data (nadpis a položky) pro konfigurační menu.
    # Používá metody: show_menu(), no_methods_yet()

    "SelectKeyMenuMixin",  # select_key_menu()
    # Vrací data (nadpis a položky) pro menu pro výběr klíče
    # Používá atributy: 'selected_key'
    # Používá metody: show_menu()

    "SelectValueMenuMixin",  # select_value_menu()
    # Vrací data (nadpis a položky) pro menu pro výběr hodnoty pro daný klíč.
    # Používá atributy: 'selected_key', 'selected_value'
    # Používá metody: show_menu()

    "MenusConfigMixin",
    "MenusColorsSettingsMixin",
    "MenusSymbolsSettingsMixin",


]