# print("_response_manager/_input_int_value/input_int_value.py")
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

from ._number_validator import NumberValidator
from ._print_intro_text import print_intro_text
from ._result_processing import result_processing

from cli_styler import (
    get_style,
    cli_print
)

def input_int_value(cli):
    """Metoda umožňující ruční zadání int hodnoty (0 - 1000)"""

    try:

        # Intro text
        print_intro_text(cli.selected_key)

        # Zadání hodnoty
        style, formatted_text = get_style.prompt.input("Zadejte hodnotu: ")
        selected_value = prompt(
            formatted_text,
            validator=NumberValidator(),
            validate_while_typing=True,
            style=Style.from_dict({"": style})
        )
        print()

        # Zpracování výsledku
        result_processing(selected_value, cli)

    except KeyboardInterrupt:
        cli_print.error.title("Zadávání přerušeno uživatelem...")
        cli.response = None
        cli.exit_menu()

