# print("_methods_mixins/loop_methods.py")
from abc import ABC

from cli_styler import cli_print
from abc_helper import abc_property, abc_method

class LoopMethodsMixin(ABC):
    """Mixin pro spuštění, ukončení a obnovení interaktivního menu"""


    # Atribut pro definici odpovědí
    response = abc_property("response")

    # Atribut zprostředkovávající instanci pro vytvoření odpovědi
    response_manager = abc_property("response")

    # Metoda pro spuštění aplikace
    run_menu = abc_method("run_menu")

    # Metoda pro zobrazení menu
    show_menu = abc_method("show_menu")



    def run_loop(self):
        """Hlavní interaktivní smyčka programu"""

        # Vytvoření smyčky
        while True:

            # Zpuštění interaktivního režimu
            self.run_menu()

            # Cyklus pro zpracování vybraného úkonu
            self._response_loop()

            # Zpracování ukončení režimu
            if self._exit_response():
                break

            # Zobrazení menu pro potvrzení ukončení
            self.show_menu("exit_menu")


    def _response_loop(self):
        """Cyklus pro zpracování vybraného úkonu"""

        # Dokud nenastane break
        while self.response:

            # Zachycení přerušení cyklu uživatelem a přerušení smyčky
            if self.response == "exit":
                break

            # Zpracování vybraného úkonu
            self.response_manager()


    def _exit_response(self):
        """Zpracování ukončení režimu"""

        # Kontrola zda je nastaven požadavek pro ukončení
        if self.response == "exit":

            # Reset hodnoty atributu pro odpověď
            self.response = None

            # Vytištění oznamu o ukončení a přerušení smyčky
            cli_print.intro.end("Ukončuji interaktivní režim... ")

            # Navrácení potvrzení o ukončovacím procesu
            return True
