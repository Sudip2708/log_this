from abc import ABC

from abc_helper import abc_property, abc_method

class RunMenuMixin(ABC):

    # Aplikace s aktuálním menu
    current_menu = abc_property("current_menu")

    # Metoda uzavře aktuální nabídku interaktivního menu
    exit_menu = abc_method("exit_menu")

    def run_menu(self):
        """Metoda načte a zobrazí aktuální nabídku interaktivního menu"""
        try:
            self.current_menu.run()
        except Exception as e:
            print(f"Došlo k chybě: {e}")
            self.exit_menu()