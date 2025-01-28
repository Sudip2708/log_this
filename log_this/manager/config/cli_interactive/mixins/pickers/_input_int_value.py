from prompt_toolkit.shortcuts import input_dialog

from log_this.manager.config.styler import dialog_style


def input_int_value() -> int:
    """
    Zobrazí dialog pro zadání celočíselné hodnoty a provede její validaci.

    Returns:
        int: Zadaná celočíselná hodnota, pokud je validní.

    Raises:
        ValueError: Pokud zadání není celočíselné nebo je příliš velké.
    """

    while True:
        # Výzva k zadání celočíselné hodnoty
        result = input_dialog(
            title="Zadejte celočíselnou hodnotu:",
            text="Zadejte celočíselnou hodnotu (musí být menší než 1000):",
            style=dialog_style,
        ).run()

        if result is None:
            raise KeyboardInterrupt  # Pokud uživatel přeruší dialog

        try:
            # Pokusíme se převést na int
            int_value = int(result)

            # Kontrola, jestli je hodnota menší než 1000
            if int_value >= 1000:
                print("Hodnota musí být menší než 1000. Zkuste to znovu.")
            else:
                return int_value  # Pokud je hodnota validní, vracíme ji
        except ValueError:
            print("Zadaná hodnota není celočíselná. Zkuste to znovu.")
