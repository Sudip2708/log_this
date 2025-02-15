from .get_menu_attributes import GetMenuAttributesMixin
from .get_menu_data import GetMenuDataMixin
from .set_response import SetResponseMixin
from .run_menu import RunMenuMixin
from .setup_key_bindings import SetupKeyBindingsMixin
from .get_menu_text import GetMenuText
from .get_interactive_menu import GetInteractiveMenuMixin

__all__ = [

    "RunMenuMixin",  # Metoda načte a zobrazí aktuální nabídku interaktivního menu
    # Používá atributy: 'interactive_menu'
    # Používá metody: exit_menu()

    "SetResponseMixin", # Nastaví atribut 'response' na požadovaný úkon a ukončí menu
    # Používá atributy: 'response'
    # Používá metody: exit_menu()

    "GetMenuDataMixin",  # Na základě 'menu_name' načte data pro požadované menu.
    # Používá metody: get_main_menu(), get_config_menu(), get_ending_menu(), get_select_key_menu(), get_select_value_menu()

    "GetMenuAttributesMixin",  # Na základě 'menu_name' vrátí obsah pro 'menu_title' a 'menu_items'.
    # Používá atributy: 'menu_name', 'menu_title', 'menu_items'
    # Používá metodu: get_menu_data()

    "SetupKeyBindingsMixin",  # Nastavení klávesových příkazů pro používání interaktivního menu
    # Používá atributy: 'kb', 'current_selection', 'menu_items'
    # Používá metodu: reload_menu(), exit_menu()

    "GetMenuText",  # Vrací naformátovaný text pro menu
    # Používá atributy: 'menu_title', 'menu_items', 'show_instruction', 'current_selection'

    "GetInteractiveMenuMixin",  # Vytvoří interaktivní menu
    # Používá atributy: 'kb',
    # Používá metodu: get_menu_text()
]