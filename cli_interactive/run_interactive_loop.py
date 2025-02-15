from styler.cli_printer import cli_print


def run_interactive_loop(cli):
    """
    Zpracovává hlavní interaktivní smyčku programu.

    Args:
        cli: Instance InteractiveCli
    """

    # Hlavní cyklus pro interaktivní menu
    while True:

        # Zpuštění interaktivního režimu
        cli.run_menu()

        # Cyklus pro zpracování vybraného úkonu
        while cli.response:

            # Zachycení přerušení cyklu uživatelem
            if cli.response == "exit":
                break

            # Zpracování vybraného úkonu
            cli.get_response()

        # Zpracování ukončení režimu
        if cli.response == "exit":

            # Nastavení požadovaného úkonu na None
            cli.response = None

            # Výpis do terminálu a přerušení cyklu
            cli_print("main.end", "☑ Ukončuji interaktivní režim...")
            break

        # Zobrazení menu pro potvrzení ukončení
        cli.switch_menu("ending_menu")