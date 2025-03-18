# print("_response_manager/_input_int_value/input_int_value.py")
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

from cli_styler import styler
from ._validators import NumberValidator



def input_int_value(menus_manager):
    """Metoda umožňující ruční zadání int hodnoty (0 - 1000)"""

    # Načtení metody pro výpis do konzole pro jednodušší zápis
    cli_print = styler.cli_print

    try:

        # Intro text
        cli_print.info.title(f"Zadání hodnoty pro klíč '{menus_manager.selected_key}'")
        cli_print.info.text("Povolené hodnoty: celé číslo v rozmezí 0 - 1000")
        cli_print.info.text("Pro návrat bez zadání ponechte prázdné pole a stiskněte Enter.")

        # Výzva k zadání hodnoty
        style, formatted_text = styler.get_style.prompt.input(
            "• Zadejte hodnotu: "
        )

        # Validace a zapsání hodnoty
        selected_value = prompt(
            formatted_text,
            validator=NumberValidator(),
            validate_while_typing=True,
            style=Style.from_dict({"": style})
        )

        # Prázdný řádek pro oddělení výstupu
        print()

        # Pokud nebyla zadána žádná hodnota, vrací se None
        if selected_value == "":
            cli_print.warning.title("Nebyla zadaná žádná hodnota.")
            cli_print.warning.direction("Návrat do menu pro výběr hodnoty.")
            menus_manager.continue_with_menu = "select_value_menu"
            return None

        return int(selected_value)  # Vrací zadanou hodnotu

    except KeyboardInterrupt:
        cli_print.error.title("Zadávání přerušeno uživatelem...")
        return None
