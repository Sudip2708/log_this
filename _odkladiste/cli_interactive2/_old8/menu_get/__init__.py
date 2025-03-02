from .get_menu_data import GetMenuDataMixin
from .get_menu_text import GetMenuTextMixin
from .get_interactive_menu import GetInteractiveMenuMixin
from .show_menu import DisplayMenuMixin

__all__ = [

    "GetMenuDataMixin",
    # Na základě 'menu_name' načte data pro požadované menu.
    # Používá metody: get_main_menu(), get_config_menu(), get_ending_menu(), get_select_key_menu(), get_select_value_menu()

    "GetMenuTextMixin",
    # Vrací naformátovaný text pro menu
    # Používá atributy: 'menu_title', 'menu_items', 'show_instruction', 'current_selection'

    "GetInteractiveMenuMixin",
    # Vytvoří interaktivní menu
    # Používá atributy: 'kb',
    # Používá metodu: get_menu_text()

    "DisplayMenuMixin",  # show_menu(new_menu_name)
    # Přepne na nové menu
    # Používá atributy: 'menu_name', 'current_selection'
    # Používá metodu: get_menu_attributes(), reload_menu()
]