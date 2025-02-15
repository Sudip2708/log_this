from abc import ABC

from abc_helper import abc_property

class ExitMenuMixin(ABC):

    # Aplikace s aktuálním menu
    interactive_menu = abc_property("interactive_menu")

    def exit_menu(self):
        """Metoda uzavře aktuální nabídku interaktivního menu"""
        if self.interactive_menu.is_running:
            self.interactive_menu.exit()