# print("run.py")
import traceback

from cli_styler import cli_print
from _manager import InteractiveCliManager

def run(start_menu="main_menu", silent=False):
    """Spustí interaktivní CLI režim"""
    try:

        # Inicializace CLI menu
        menu_app = InteractiveCliManager(menu_name=start_menu)

        # Zobrazení nadpisu (je-li požadováno)
        if not silent:
            cli_print.intro.title(
                "VÍTEJTE V INTERAKTIVNÍM REŽIMU!"
            )

        # Spuštění hlavní smyčky
        menu_app.run_loop()

    # Zachycení nepodchycených chyb
    except Exception as e:
        cli_print.error.title(
            f"Došlo k neočekávané chybě: {str(e)}"
        )
        print(traceback.format_exc())


if __name__ == "__main__":
    run()