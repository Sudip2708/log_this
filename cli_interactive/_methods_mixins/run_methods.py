# print("_methods_mixins/run_methods.py")
from abc import ABC
import traceback

from cli_styler import cli_print
from abc_helper import abc_property

class RunMethodsMixin(ABC):
    """Mixin pro spuštění, ukončení a obnovení interaktivního menu"""

    # Atribut pro instanci MenuRenderer
    menu_renderer = abc_property("menu_renderer")

    # Atribut pro definici odpovědí
    response = abc_property("response")


    def run_menu(self):
        """Spustí interaktivní režim s ošetřením chyb"""
        try:
            # Požadavek na zpuštění menu
            self.menu_renderer.run()

        except Exception as e:
            # Výpis o chybě a trekování chby
            cli_print.error.title(f"Došlo k neočekávané chybě: {str(e)}")
            print(traceback.format_exc())


    def exit_menu(self):
        """Ukončí interaktivní režim"""

        # Nastavení odezvy na ukončení aplikace
        self.response = "exit"

        # Požadavek na ukončení menu
        self.menu_renderer.exit()


    def refresh_menu(self):
        """Znovu načte interaktivní režim"""

        # Kontrola zda interaktivní menu běží
        if self.menu_renderer.is_running():

            # Požadavek na obnovu menu
            self.menu_renderer.refresh()

        else:
            # Požadavek na zpuštění menu
            self.run_menu()
