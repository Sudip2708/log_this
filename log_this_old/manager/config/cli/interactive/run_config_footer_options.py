from prompt_toolkit.shortcuts import radiolist_dialog

from ..styler import dialog_style
from .dialogs import exit_interactive_mode
from .exceptions import ExitInteractiveMode


def run_config_footer_options(run_interactive_menu) -> None:
    """Spustí zobrazuje okno pro ukončení interaktivního režimu."""

    try:

        # Cyklus pro hlavní menu
        while True:

            # Načtení vstupu z hlavního menu
            result = radiolist_dialog(
                title='Vyberte požadovaný úkon:',
                values=[
                    ('menu', 'Hlavní menu'),
                    ('exit', 'Ukončit interaktivní režim')
                ],
                style=dialog_style
            ).run()

            # Pokud byl zadán požadavek na nápovědu
            if result == 'menu':
                run_interactive_menu(intro=False)

            # Pokud byl zadán požadavek na ukončení interaktivního režimu
            elif result == 'exit':
                ExitInteractiveMode()

    # Pokud došlo k přerušení interaktivního modu
    except ExitInteractiveMode as e:
        exit_interactive_mode(e.message)




