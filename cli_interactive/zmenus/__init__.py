from .get_main_menu import GetMainMenuMixin
from .get_ending_menu import GetEndingMenuMixin
from .get_config_menu import GetConfigMenuMixin
from .get_select_key_menu import GetSelectKeyMenuMixin
from .get_select_value_menu import GetSelectValueMenuMixin

__all__ = [
    "GetMainMenuMixin",  # Vrací data (nadpis a položky) pro hlavní menu.
    # Používá atributy: 'show_instruction'
    # Používá metody: set_response(), switch_menu(), exit_menu()

    "GetEndingMenuMixin",  # Vrací data (položky) pro ukončovací menu
    # Používá metody: switch_menu(), exit_menu()

    "GetConfigMenuMixin",  # Vrací data (nadpis a položky) pro konfigurační menu.
    # Používá metody: switch_menu(), no_methods_yet()

    "GetSelectKeyMenuMixin",  # Vrací data (nadpis a položky) pro menu pro výběr klíče
    # Používá atributy: 'selected_key'
    # Používá metody: switch_menu()

    "GetSelectValueMenuMixin",  # Vrací data (nadpis a položky) pro menu pro výběr hodnoty pro daný klíč.
    # Používá atributy: 'selected_key', 'selected_value'
    # Používá metody: switch_menu(), set_response()

]