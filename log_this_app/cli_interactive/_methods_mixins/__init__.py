# print("_methods_mixins/__init__.py")
from .navigation_methods import NavigationMethodsMixin
from .run_methods import RunMethodsMixin
from .loop_methods import LoopMethodsMixin

__all__ = [

    "NavigationMethodsMixin",
    # Mixin přidávající metody pro ovládání kláves
    # Přidává metody: go_up(), go_down(), run_current_selection()
    # Používá atributy: 'menu_renderer', 'menu'

    "RunMethodsMixin",
    # Mixin přidávající běhové metody
    # Přidává metody: run_menu(), exit_menu(), refresh_menu()
    # Používá atributy: 'menu_renderer'

    "LoopMethodsMixin",
    # Mixin přidávající logiku pro vytvoření smyčky
    # Přidává metody: run_loop(), _response_loop(), _exit_response()
    # Používá atributy: 'response', 'response_manager'
    # Používá metody: 'run_menu', 'show_menu'

]