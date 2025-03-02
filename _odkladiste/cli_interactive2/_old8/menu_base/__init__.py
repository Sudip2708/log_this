from .exit_menu import ExitMenuMixin
from .reload_menu import ReloadMenuMixin
from .run_menu import RunMenuMixin

__all__ = [

    "ExitMenuMixin",  # exit_menu()
    # Metoda uzavře aktuální interaktivní menu.
    # Používá atributy: 'current_menu'

    "ReloadMenuMixin",  # reload_menu()
    # Metoda znovu načte data pro vykreselní menu
    # Používá atributy: 'current_menu'

    "RunMenuMixin",   # run_menu()
    # Metoda načte a zobrazí aktuální nabídku interaktivního menu
    # Používá atributy: 'current_menu'
    # Používá metody: exit_menu()

]