from prompt_toolkit.shortcuts import input_dialog
from log_this.manager.config.cli.styler import dialog_style

def input_int_value() -> int:
    """
    Zobrazí dialog pro zadání celočíselné hodnoty a provede její validaci.

    Returns:
        int: Zadaná celočíselná hodnota, pokud je validní.

    Raises:
        ValueError: Pokud zadání není celočíselné nebo je příliš velké.
    """

    # Indikátor vypsání nadpisu při první iteraci
    show_title = True

    # Nekonečný cyklus pkončící správným výsledkem
    while True:

        # Vytvoření dialogu a načtení výsledu
        result = input_dialog(
            title="Zadání vlastní celočíselné hodnoty" if show_title else "",
            text="Zadejte číslo (0-1000):",
            style=dialog_style,
        ).run()

        # Nastavení skrytí nadpisu pro případ chybného zadání hodnoty
        show_title = False

        if result is None:
            raise KeyboardInterrupt  # Uživatel přerušil zadávání

        try:
            int_value = int(result)

            if int_value >= 1000:
                print("Hodnota musí být menší než 1000. Zkuste to znovu.")
                continue

            if int_value < 0:
                print("Hodnota musí být kladné číslo. Zkuste to znovu.")
                continue

            return int_value  # Správná hodnota, ukončí cyklus

        except ValueError:
            print("Zadaná hodnota není celočíselná. Zkuste to znovu.")
