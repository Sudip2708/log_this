from abc import ABC

from abc_helper import abc_property

class ExitMenuMixin(ABC):

    # Aplikace s aktuálním menu
    current_menu = abc_property("current_menu")

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    def exit_menu(self):
        """Metoda uzavře aktuální nabídku interaktivního menu"""

        # kontrola zda interaktivní menu běží
        if self.current_menu.is_running:

            # Kontrola zda je zadána atribut pro odezvu
            if not self.response:

                # Pokud ne nastaví se na ukončení aplikace
                self.response = "exit"

            # Ukončení aktuálního menu
            self.current_menu.exit()
