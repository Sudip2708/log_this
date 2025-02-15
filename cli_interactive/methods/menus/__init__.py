from .main_menu import MainMenuMixin
from .ending_menu import EndingMenuMixin
from .config_menu import ConfigMenuMixin
from .select_key_menu import SelectKeyMenuMixin
from .select_value_menu import SelectValueMenuMixin

__all__ = [
    "MainMenuMixin",  # get_main_menu()
    # Vrací data (nadpis a položky) pro hlavní menu.
    # Používá atributy: 'show_instruction'
    # Používá metody: display_menu(), exit_menu()

    "EndingMenuMixin",  # get_ending_menu()
    # Vrací data (položky) pro ukončovací menu
    # Používá metody: display_menu(), exit_menu()

    "ConfigMenuMixin",  # get_config_menu()
    # Vrací data (nadpis a položky) pro konfigurační menu.
    # Používá metody: display_menu(), no_methods_yet()

    "SelectKeyMenuMixin",  # get_select_key_menu()
    # Vrací data (nadpis a položky) pro menu pro výběr klíče
    # Používá atributy: 'selected_key'
    # Používá metody: display_menu()

    "SelectValueMenuMixin",  # get_select_value_menu()
    # Vrací data (nadpis a položky) pro menu pro výběr hodnoty pro daný klíč.
    # Používá atributy: 'selected_key', 'selected_value'
    # Používá metody: display_menu()


]