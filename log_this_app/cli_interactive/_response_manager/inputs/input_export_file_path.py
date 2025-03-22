from pathlib import Path
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from cli_styler import styler

from ._validators import PathValidator

def input_export_file_path(menus_manager):
    """
    Zobrazí dialog pro zadání adresy souboru nebo složky a provede její validaci.

    Returns:
        Path: Platná cesta k souboru nebo složce.

    Raises:
        KeyboardInterrupt: Pokud uživatel zruší zadávání.
        ValueError: Pokud zadaná cesta není validní.
    """

    # Načtení metody pro výpis do konzole pro jednodušší zápis
    cli_print = styler.cli_print

    try:

        # Intro text
        cli_print.info.title(f"Zadání cesty k souboru")
        cli_print.info.text("Cesta musí být absolutní a předána jako řetězec s lomítky")
        cli_print.info.text("Pro návrat bez zadání ponechte prázdné pole a stiskněte Enter.")

        # Výzva k zadání hodnoty
        style, formatted_text = styler.get_style.prompt.input(
            "• Zadejte cestu: "
        )

        # Validace a zapsání hodnoty
        selected_path = prompt(
            formatted_text,
            validator=PathValidator(check_folder_only=True, must_be_json=True),
            validate_while_typing=True,
            style=Style.from_dict({"": style})
        )

        # Prázdný řádek pro oddělení výstupu
        print()

        # Pokud nebyla zadána žádná hodnota, vrací se None
        if selected_path == "":
            cli_print.warning.title("Nebyla zadaná žádná hodnota.")
            cli_print.warning.direction("Návrat do předchozího menu.")
            menus_manager.continue_with_menu = True
            return None

        return selected_path

    except KeyboardInterrupt:
        cli_print.error.title("Zadávání přerušeno uživatelem...")
        return None

