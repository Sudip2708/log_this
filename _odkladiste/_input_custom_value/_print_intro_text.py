# print("_response_manager/_input_int_value/_print_intro_text.py")
from cli_styler import cli_print

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