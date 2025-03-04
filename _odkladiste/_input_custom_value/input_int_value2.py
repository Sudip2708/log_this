# print("_response_manager/_input_int_value/input_int_value.py")
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.validation import Validator, ValidationError


class NumberValidator(Validator):
    """Validátor pro zadávání čísel od 0 do 1000"""
    def validate(self, document):
        try:
            value = int(document.text)
            if not (0 <= value <= 1000):
                raise ValidationError(message="Zadejte číslo mezi 0 a 1000.")
        except ValueError:
            raise ValidationError(message="Zadejte platné celé číslo.")

def print_intro_text(cli):

    cli.styler.cli_print.info.title(
        f"Ruční zadání hodnoty pro klíč '{cli.selected_key}'"
    )
    cli.styler.cli_print.info.text(
        "Povolené hodnoty: celé číslo v rozmezí 0 - 1000"
    )
    cli.styler.cli_print.info.text(
        "Pro návrat bez zadání ponechte prázdné pole a stiskněte Enter."
    )

def result_processing(selected_value, cli):

    # Pokud je výsledek
    if selected_value:

        # Nastaví atributu 'selected_value' na danou hodnotu
        cli.selected_value = selected_value

        # Nastaví atributu 'response' na vytištění výsledku
        cli.response = "print_new_settings"

    # Pokud nebyla zadaná žádná hodnota (pro opuštění zadání)
    else:

        # Vypíše se oznam o návratu do menu pro výběr hodnoty
        cli.styler.cli_print.warning.title("Nebyla zadaná žádná hodnota.")
        cli.styler.cli_print.warning.direction("Návrat do menu pro výběr hodnoty.")

        # Vyčistí se obsah atributu 'response'
        cli.response = None

        # Načtení a spuštění okna s menu pro výběr hodnoty
        cli.switch_menu("select_value_menu")
        cli.run_menu()


def input_int_value(menus_manager):
    """Metoda umožňující ruční zadání int hodnoty (0 - 1000)"""

    try:

        # Intro text
        print_intro_text(menus_manager)

        # Zadání hodnoty
        style, formatted_text = menus_manager.styler.get_style.prompt.input("Zadejte hodnotu: ")
        selected_value = prompt(
            formatted_text,
            validator=NumberValidator(),
            validate_while_typing=True,
            style=Style.from_dict({"": style})
        )
        print()

        # Zpracování výsledku
        result_processing(selected_value, menus_manager)

    except KeyboardInterrupt:
        menus_manager.styler.cli_print.error.title("Zadávání přerušeno uživatelem...")
        menus_manager.response = "exit"
        menus_manager.exit_menu()

