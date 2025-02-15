from cli_styler import cli_print


def run_interactive_loop(cli_menu):
    """
    Zpracovává hlavní interaktivní smyčku programu.

    Args:
        cli_menu: Instance InteractiveCli
    """

    # Hlavní cyklus pro interaktivní menu
    while True:

        # Zpuštění interaktivního režimu
        cli_menu.run_menu()

        # Cyklus pro zpracování vybraného úkonu
        while cli_menu.response:

            # Zachycení přerušení cyklu uživatelem
            if cli_menu.response == "exit":
                break

            # Zpracování vybraného úkonu
            cli_menu.get_response()

        # Zpracování ukončení režimu
        if cli_menu.response == "exit":

            # Nastavení požadovaného úkonu na None
            cli_menu.response = None

            # Výpis do terminálu a přerušení cyklu
            cli_print("main.end", "☑ Ukončuji interaktivní režim...")
            break

        # Zobrazení menu pro potvrzení ukončení
        cli_menu.display_menu("ending_menu")