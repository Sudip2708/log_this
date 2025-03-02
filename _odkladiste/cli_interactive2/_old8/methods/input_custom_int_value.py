from abc import ABC
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

from abc_helper import abc_property, abc_method
from .number_validator import NumberValidator
from cli_styler import (
    print_info_title,
    print_info_text,
    get_prompt_input,
    print_warning_title,
    print_warning_direction,
    print_error_title,
)


class InputCustomIntValueMixin(ABC):

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    # Atribut pro zaznamenání vybraného klíče
    selected_key = abc_property("selected_key")

    # Atribut pro zaznamenání vybrané hodnoty pro daný klíče
    selected_value = abc_property("selected_key")

    # Metoda která přepne menu na nové menu
    show_menu = abc_method("show_menu")

    # Metoda načte a zobrazí aktuální nabídku interaktivního menu
    run_menu = abc_method("run_menu")

    # Metoda uzavře aktuální interaktivní menu
    exit_menu = abc_method("exit")

    def input_custom_int_value(self):
        """Metoda umožňující ruční zadání int hodnoty (0 - 1000)"""

        try:

            # Intro text
            print_info_title(f"Ruční zadání hodnoty pro klíč '{self.selected_key}'")
            print_info_text("Povolené hodnoty: celé číslo v rozmezí 0 - 1000")
            print_info_text("Pro návrat bez zadání ponechte prázdné pole a stiskněte Enter.")

            # Zadání hodnoty
            style, formatted_text = get_prompt_input("Zadejte hodnotu: ")
            selected_value = prompt(
                formatted_text,
                validator = NumberValidator(),
                validate_while_typing = True,
                style = Style.from_dict({"": style})
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
                print_warning_title("Nebyla zadaná žádná hodnota.")
                print_warning_direction("Návrat do menu pro výběr hodnoty.")
                self.response = None
                self.show_menu("select_value_menu")
                self.run_menu()

        except KeyboardInterrupt:
            print_error_title("Zadávání přerušeno uživatelem...")
            self.response = None
            self.exit_menu()


