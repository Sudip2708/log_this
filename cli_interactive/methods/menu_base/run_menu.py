from abc import ABC
import traceback

from abc_helper import abc_property, abc_method
from cli_styler import cli_print


class RunMenuMixin(ABC):

    # Aplikace s aktuálním menu
    current_menu = abc_property("current_menu")

    # Metoda uzavře aktuální nabídku interaktivního menu
    exit_menu = abc_method("exit_menu")

    def run_menu(self):
        """Metoda načte a zobrazí aktuální nabídku interaktivního menu"""

        try:
            self.current_menu.run()

        # Zachycení neočekávaných chyb a výpis tracebacku
        except Exception as e:
            cli_print("error", f"⛝ Došlo k neočekávané chybě: {str(e)}")
            print(traceback.format_exc())