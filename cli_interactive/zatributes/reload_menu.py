from abc import ABC

from abc_helper import abc_property

class ReloadMenuMixin(ABC):

    # Aplikace s aktuálním menu
    interactive_menu = abc_property("interactive_menu")

    def reload_menu(self):
        """Metoda znovu načte data pro vykreselní menu"""
        self.interactive_menu.invalidate()