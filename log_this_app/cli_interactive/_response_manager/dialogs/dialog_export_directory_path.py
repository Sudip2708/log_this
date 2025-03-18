

from prompt_toolkit.validation import Validator, ValidationError
from cli_styler import styler
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


def dialog_export_directory_path(menus_manager):
    """
    Otevře dialogové okno pro výběr souboru a provede jeho validaci.

    Returns:
        Path: Platná cesta k souboru.

    Raises:
        KeyboardInterrupt: Pokud uživatel zruší zadávání.
    """

    # Načtení metody pro výpis do konzole
    cli_print = styler.cli_print

    try:
        # Intro text
        cli_print.info.title("Výběr cesty k složce pro uložení konfigurace")
        cli_print.info.text("(Zadání probýhá přes dialogové okno.)")
        cli_print.info.text("Pro návrat bez zadání cesty zavřete dialogové okno.")

        # Spuštění dialogu pro výběr souboru
        root = tk.Tk()
        root.withdraw()  # Skryje hlavní okno
        root.attributes("-topmost", True)  # Nastaví okno jako "vždy navrchu"
        selected_path = filedialog.askdirectory(title="Vyberte složku pro export")

        # Prázdný řádek pro oddělení výstupu
        print()

        # Pokud nebyla zvolena žádná cesta, vrací se None
        if not selected_path:
            cli_print.warning.title("Nebyla vybrána žádná cesta.")
            cli_print.warning.direction("Návrat do předchozího menu.")
            menus_manager.continue_with_menu = "export_menu"
            return None

        # Převod na Path objekt
        return Path(selected_path)

    except KeyboardInterrupt:
        cli_print.error.title("Zadávání přerušeno uživatelem...")
        return None

