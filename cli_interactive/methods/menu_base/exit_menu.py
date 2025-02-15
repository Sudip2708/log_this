from abc import ABC

from abc_helper import abc_property

class ExitMenuMixin(ABC):

    # Aplikace s aktuálním menu
    interactive_menu = abc_property("interactive_menu")

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    def exit_menu(self):
        """Metoda uzavře aktuální nabídku interaktivního menu"""

        # kontrola zda interaktivní menu běží
        if self.interactive_menu.is_running:

            # Kontrola zda je zadána atribut pro odezvu
            if not self.response:

                # Pokud ne nastaví se na ukončení aplikace
                self.response = "exit"

            # Ukončení aktuálního menu
            self.interactive_menu.exit()
