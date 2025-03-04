# print("_response_manager/_input_int_value/input_int_value.py")
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

from ._number_validator import NumberValidator

class InputCustomValue:

    def __init__(self, menus_manager):
        self.mm = menus_manager


    def __call__(self):
        """Metoda umožňující ruční zadání int hodnoty (0 - 1000)"""

        try:

            # Vymazání atibutu pro hodnotu
            self.mm.selected_value = None

            # Intro text
            self.intro_text()

            # Zadání hodnoty
            self.input_dialog()

            # Zpracování výsledku
            self.result_processing()

        except KeyboardInterrupt:
            self.mm.styler.cli_print.error.title("Zadávání přerušeno uživatelem...")
            self.mm.response = "exit"
            self.mm.exit_menu()


    def intro_text(self):
        self.mm.styler.cli_print.info.title(
            f"Ruční zadání hodnoty pro klíč '{self.mm.selected_key}'")
        self.mm.styler.cli_print.info.text(
            "Povolené hodnoty: celé číslo v rozmezí 0 - 1000")
        self.mm.styler.cli_print.info.text(
            "Pro návrat bez zadání ponechte prázdné pole a stiskněte Enter.")

    def input_dialog(self):
        style, formatted_text = self.mm.styler.get_style.prompt.input("Zadejte hodnotu: ")
        self.mm.selected_value = prompt(
            formatted_text,
            validator=NumberValidator(),
            validate_while_typing=True,
            style=Style.from_dict({"": style})
        )
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