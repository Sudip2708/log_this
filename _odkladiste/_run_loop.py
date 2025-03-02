print("_run_loop.py")
from cli_styler import cli_print


def run_loop(cli):
    """Hlavní interaktivní smyčka programu"""

    # Vytvoření smyčky
    while True:

        # Zpuštění interaktivního režimu
        cli.run_menu()

        # Cyklus pro zpracování vybraného úkonu
        response_loop(cli)

        # Zpracování ukončení režimu
        if exit_response(cli):

            # Přeušení smyčky
            break

        # Zobrazení menu pro potvrzení ukončení
        cli.show_menu("exit_menu")

def response_loop(cli):
    """Cyklus pro zpracování vybraného úkonu"""

    while cli.response:

        # Zachycení přerušení cyklu uživatelem
        if cli.response == "exit":
            # Přeušení smyčky
            break

        # Zpracování vybraného úkonu
        cli.response_manager()

def exit_response(cli):
    """Zpracování ukončení režimu"""

    if cli.response == "exit":

        # Nastavení atributu pro odpověď na None
        cli.response = None

        # Vytištění oznamu o ukončení
        cli_print.intro.end("Ukončuji interaktivní režim... ")

        return True