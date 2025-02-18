from abc import ABC
from prompt_toolkit import prompt

from abc_helper import abc_property, abc_method
from cli_styler import cli_style, cli_print
from .number_validator import NumberValidator


class InputCustomIntValueMixin(ABC):

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    # Atribut pro zaznamenání vybraného klíče
    selected_key = abc_property("selected_key")

    # Atribut pro zaznamenání vybrané hodnoty pro daný klíče
    selected_value = abc_property("selected_key")

    # Metoda která přepne menu na nové menu
    display_menu = abc_method("display_menu")

    # Metoda načte a zobrazí aktuální nabídku interaktivního menu
    run_menu = abc_method("run_menu")

    # Metoda uzavře aktuální interaktivní menu
    exit_menu = abc_method("exit")

    def input_custom_int_value(self):
        """Metoda umožňující ruční zadání int hodnoty (0 - 1000)"""

        try:

            # Intro text
            cli_print("_info.title", f" ☐ Ruční zadání hodnoty pro klíč '{self.selected_key}'")
            cli_print("info.text", " - Povolené hodnoty: celé číslo v rozmezí 0 - 1000")
            cli_print("info.text", " - Pro návrat bez zadání ponechte prázdné pole a stiskněte Enter.")
            # print()

            # Zadání hodnoty
            selected_value = prompt(
                " » Zadejte hodnotu: ",
                validator = NumberValidator(),
                validate_while_typing = True,
                style=cli_style
            )
            print()

            # Kontrola zda byla zadaná hodnota
            # Nastaví atributu 'selected_value' na danou hodnotu
            # Nastaví atributu 'response' na vytištění výsledku
            if selected_value:
                self.selected_value = selected_value
                self.response = "print_new"

            # Pokud nebyla zadaná žádná hodnota (pro opuštění zadání)
            # Vypíše se oznam o návratu do menu pro výběr hodnoty
            # Zavolá se metoda pro zobrazení menu
            else:
                cli_print("error.title", " ⚠ Nebyla zadaná žádná hodnota. ")
                cli_print("error.text", " » Návrat do menu pro výběr hodnoty. ")
                print()
                self.display_menu("select_value_menu")
                self.run_menu()

        except KeyboardInterrupt:
            cli_print("error", "\n ⚠ Zadávání přerušeno uživatelem... \n")
            self.response = None
            self.exit_menu()


