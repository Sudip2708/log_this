import logging
from typing import Optional
from styler.cli_printer import cli_print
from interactive_cli import InteractiveCli
from interactive_loop import handle_interactive_loop


def run_interactive_mode(start_menu="main", silent=False):
    """
    Spustí interaktivní CLI režim aplikace.
    Zajišťuje inicializaci, běh programu a správu chyb.

    Args:
        start_menu (str): Počáteční typ menu
        silent (bool): Potlačí uvítací zprávu
    """
    try:

        if not silent:
            # Úvod do interaktivního režimu
            cli_print("main.title", "\n■ VÍTEJTE V INTERAKTIVNÍM REŽIMU!")
            cli_print("main.line", "-------------------------------------")

        # Inicializace a spuštění hlavní smyčky
        cli = InteractiveCli(menu_type=start_menu)
        handle_interactive_loop(cli)

    except Exception as e:
        # Zachycení neočekávaných chyb
        cli_print("error", f"⛝ Došlo k neočekávané chybě: {str(e)}")