from pathlib import Path
from prompt_toolkit.shortcuts import input_dialog

from cli_styler import styler




def input_file_path() -> Path:
    """
    Zobrazí dialog pro zadání adresy souboru nebo složky a provede její validaci.

    Returns:
        Path: Platná cesta k souboru nebo složce.

    Raises:
        KeyboardInterrupt: Pokud uživatel zruší zadávání.
        ValueError: Pokud zadaná cesta není validní.
    """

    # Indikátor vypsání nadpisu při první iteraci
    show_title = True

    # Nekonečný cyklus pkončící správným výsledkem
    while True:

        # Vytvoření dialogu a načtení výsledu
        result = input_dialog(
            title="Zadání adresy" if show_title else "",
            text="Zadejte cestu k souboru nebo složce:",
            # style=dialog_style,
        ).run()

        # Nastavení skrytí nadpisu pro případ chybného zadání hodnoty
        show_title = False

        # Kontrola, zda bylo zadávání přerušeno uživatelem
        if result is None:
            raise KeyboardInterrupt

        try:
            # Převedeme vstup na objekt Path
            path = Path(result.strip())

            # Kontrola, zda je cesta validní (musí obsahovat aspoň jeden znak a nesmí být pouze mezery)
            if not path.as_posix():
                print("Neplatná cesta. Zkuste to znovu.")
                continue  # Skočí na začátek cyklu

            return path

        except Exception as e:
            print(f"Neplatný formát cesty: {e}. Zkuste to znovu.")
