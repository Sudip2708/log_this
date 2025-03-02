print("runner.py")
import traceback

from cli_styler import cli_print
from _manager import InteractiveCliManager


class InteractiveCliRunner:
    """Řídí hlavní smyčku interaktivního režimu"""


    def __call__(self, start_menu="main_menu", silent=False):
        """Spustí interaktivní CLI režim"""

        try:
            if not silent:
                cli_print.intro.title("VÍTEJTE V INTERAKTIVNÍM REŽIMU!")

            # Inicializace CLI menu
            self.cli = InteractiveCliManager(menu_name=start_menu)

            # Spuštění hlavní smyčky
            self._run_loop()

        except Exception as e:
            cli_print.error.title(f"Došlo k neočekávané chybě: {str(e)}")
            print(traceback.format_exc())


    def _run_loop(self):
        """Hlavní interaktivní smyčka programu"""

        # Vytvoření smyčky
        while True:

            # Zpuštění interaktivního režimu
            self.cli.run_menu()

            # Cyklus pro zpracování vybraného úkonu
            self.response_loop()

            # Zpracování ukončení režimu
            if self.exit_response():
                break

            # Zobrazení menu pro potvrzení ukončení
            self.cli.show_menu("exit_menu")


    def response_loop(self):
        """Cyklus pro zpracování vybraného úkonu"""

        while self.cli.response:

            # Zachycení přerušení cyklu uživatelem a přerušení smyčky
            if self.cli.response == "exit":
                break

            # Zpracování vybraného úkonu
            self.cli.response_manager()


    def exit_response(self):
        """Zpracování ukončení režimu"""

        if self.cli.response == "exit":

            # Reset hodnoty atributu pro odpověď
            self.cli.response = None

            # Vytištění oznamu o ukončení a přerušení smyčky
            cli_print.intro.end("Ukončuji interaktivní režim... ")

            return True


# Vytvoření instance runneru jako výchozího objektu
runner = InteractiveCliRunner()

# Pokud je soubor spuštěn jako hlavní program, spustí interaktivní režim
if __name__ == "__main__":
    runner()



