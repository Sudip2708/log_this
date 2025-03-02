from abc import ABC
import traceback

from cli_styler import print_styled_intro_title, print_styled_error_title, print_styled_intro_end
from interactive_cli import InteractiveCli
from abc_helper import abc_property, abc_method

class RunMethodMixin(ABC):
    """Mixin pro navigaci v interaktivním menu"""


    # Atribut pro instanci hlavní třídy
    cli = abc_property("cli")

    # Atribut pro instanci hlavní třídy
    silent = abc_property("silent")

    # Atribut pro instanci hlavní třídy
    start_menu = abc_property("start_menu")

    # Atribut pro instanci hlavní třídy
    run_loop = abc_method("run_loop")


    def run(self):
        """Spustí interaktivní CLI režim"""
        try:
            if not self.silent:
                print_styled_intro_title("VÍTEJTE V INTERAKTIVNÍM REŽIMU!")

            # Inicializace CLI menu
            self.cli = InteractiveCli(menu_name=self.start_menu)

            # Spuštění hlavní smyčky
            self.run_loop()

        except Exception as e:
            print_styled_error_title(f"Došlo k neočekávané chybě: {str(e)}")
            print(traceback.format_exc())
