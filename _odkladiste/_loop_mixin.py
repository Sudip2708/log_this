print("_loop_mixin.py")
from abc import ABC

from abc_helper import abc_property, abc_method
from cli_styler import cli_print


class LoopMixin(ABC):
    """Mixin pro navigaci v interaktivním menu"""

    # Atribut pro instanci hlavní třídy
    cli = abc_property("cli")


    def _run_loop(self):
        """Hlavní interaktivní smyčka programu"""

        # Vytvoření smyčky
        while True:

            # Zpuštění interaktivního režimu
            self.cli.run_menu()

            # Cyklus pro zpracování vybraného úkonu
            self.response_loop()

            # Zpracování ukončení režimu
            if self.cli.response == "exit":

                # Reset hodnoty atributu pro odpověď
                self.cli.response = None

                # Vytištění oznamu o ukončení a přerušení smyčky
                cli_print.intro.end("Ukončuji interaktivní režim... ")
                break

            # Zobrazení menu pro potvrzení ukončení
            self.cli.show_menu("exit_menu")

    def response_loop(self):

        # Cyklus pro zpracování vybraného úkonu
        while self.cli.response:

            # Zachycení přerušení cyklu uživatelem a přerušení smyčky
            if self.cli.response == "exit":
                break

            # Zpracování vybraného úkonu
            self.cli.response_manager()

