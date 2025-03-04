from abc import ABC
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

from abc_helper import abc_property
from ._number_validator import NumberValidator

class InputIntValueMethodMixin(ABC):

    mm = abc_property("mm")

    def intro_text(self):
        self.mm.styler.cli_print.info.title(
            f"Ruční zadání hodnoty pro klíč '{self.mm.selected_key}'")
        self.mm.styler.cli_print.info.text(
            "Povolené hodnoty: celé číslo v rozmezí 0 - 1000")
        self.mm.styler.cli_print.info.text(
            "Pro návrat bez zadání ponechte prázdné pole a stiskněte Enter.")

    def input_dialog(self):
        # Vstupní dialog s výzvou k zadání hodnoty
        style, formatted_text = self.mm.styler.get_style.prompt.input(
            "Zadejte hodnotu: "
        )
        #  Získání a zápis vstupní hodnoty
        self.mm.selected_value = prompt(
            formatted_text,
            validator=NumberValidator(),
            validate_while_typing=True,
            style=Style.from_dict({"": style})
        )
        # Prázdný řádek
        print()

    def result_processing(self):
        # Pokud je výsledek
        if self.mm.selected_value:
            # Nastaví atributu 'response' na vytištění výsledku
            self.mm.response = "print_new_settings"

        # Pokud nebyla zadaná žádná hodnota (pro opuštění zadání)
        else:
            # Vypíše se oznam o návratu do menu pro výběr hodnoty
            self.mm.styler.cli_print.warning.title(
                "Nebyla zadaná žádná hodnota.")
            self.mm.styler.cli_print.warning.direction(
                "Návrat do menu pro výběr hodnoty.")
            # Vyčistí se obsah atributu 'response'
            self.mm.response = None
            # Načtení a spuštění okna s menu pro výběr hodnoty
            self.mm.switch_menu("select_value_menu")
            self.mm.run_menu()

