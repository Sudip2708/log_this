import traceback

from cli_styler import cli_print
from interactive_cli import InteractiveCli
from .run_interactive_loop import run_interactive_loop



def run_interactive_mode(start_menu="main_menu", silent=False):
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
            cli_print("cli_intro.title", "\n ■ VÍTEJTE V INTERAKTIVNÍM REŽIMU! \n")

        # Inicializace a spuštění hlavní smyčky
        cli_menu = InteractiveCli(menu_name=start_menu)
        run_interactive_loop(cli_menu)

    # Zachycení neočekávaných chyb a výpis tracebacku
    except Exception as e:
        cli_print("cli_error", f"⛝ Došlo k neočekávané chybě: {str(e)}")
        print(traceback.format_exc())

