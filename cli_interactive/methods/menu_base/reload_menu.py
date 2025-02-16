from abc import ABC

from abc_helper import abc_property, abc_method

class ReloadMenuMixin(ABC):

    # Aplikace s aktuálním menu
    current_menu = abc_property("current_menu")

    # Metoda načte a zobrazí aktuální nabídku interaktivního menu
    run_menu = abc_method("run_menu")


    def reload_menu(self):
        """Metoda znovu načte data pro vykreselní menu"""

        # Kontrola zda interaktivní menu běží
        if self.current_menu:

            # Požadavek na obnovu menu
            self.current_menu.invalidate()

        # Pokud menu nebježí
        else:

            # Požadavek na jeho zpuštění
            self.run_menu()