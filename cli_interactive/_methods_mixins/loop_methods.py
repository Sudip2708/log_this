# print("_methods_mixins/loop_methods.py")
from abc import ABC

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

    # Atribut zprostředkovávající instanci styleru
    styler = abc_property("styler")

    # Atribut zaznamenávající menu s ktým se má prokračovat po response kolečku
    continue_with_menu = abc_property("continue_with_menu")

    def run_loop(self):
        """Hlavní interaktivní smyčka programu"""

        # Vytvoření smyčky
        while True:

            # Zpuštění interaktivního režimu
            self.run_menu()

            # Cyklus pro zpracování vybraného úkonu
            self._response_loop()

            # print("### self.response", self.response)

            # Kontrola zda je nastaven požadavek pro ukončení
            if self.response == "exit":

                # Reset hodnoty atributu pro odpověď
                self.response = None

                # Vytištění oznamu o ukončení a přerušení smyčky
                self.styler.cli_print.intro.end("Ukončuji interaktivní režim... ")
                break

            # KOntrola, zda je vyžadováno pokračující menu
            if self.continue_with_menu:
                # Zobrazení pokračujícího menu
                self.show_menu(self.continue_with_menu, target_reset=False)
                # Reset hodnoty
                self.continue_with_menu = None
            else:
                # Zobrazení menu pro potvrzení ukončení
                self.show_menu("exit_menu")


    def _response_loop(self):
        """Cyklus pro zpracování vybraného úkonu"""

        # Dokud nenastane break
        while self.response:

            # Zachycení přerušení cyklu uživatelem a přerušení smyčky
            if self.response in ("exit", "exit_menu"):
                break

            # Zpracování vybraného úkonu
            self.response_manager()


