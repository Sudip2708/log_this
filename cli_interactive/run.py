# print("run.py")
import traceback

from _menus_manager import MenusManager

def run(start_menu="main_menu", silent=False):
    """Spustí interaktivní CLI režim"""
    try:

        # Inicializace CLI menu
        mm = MenusManager(menu_name=start_menu)

        # Zobrazení nadpisu (je-li požadováno)
        if not silent:
            mm.styler.cli_print.intro.title(
                "VÍTEJTE V INTERAKTIVNÍM REŽIMU!"
            )

        # Spuštění hlavní smyčky
        mm.run_loop()

    # Zachycení nepodchycených chyb
    except Exception as e:
        print(f"Došlo k neočekávané chybě: {str(e)}")
        print(traceback.format_exc())


if __name__ == "__main__":
    run()