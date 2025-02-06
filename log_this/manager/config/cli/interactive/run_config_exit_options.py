from prompt_toolkit.shortcuts import radiolist_dialog

from log_this.manager.config.cli.styler import cli_print, dialog_style
from log_this.manager.config.cli.interactive.dialogs import exit_interactive_mode, show_help
from log_this.manager.config.cli.interactive.exceptions import ExitInteractiveMode
from ..runners import run_config_settings, run_main_menu

def run_config_exit_options(messagge = None) -> None:
    """Spustí zobrazuje okno pro ukončení interaktivního režimu."""

    try:

        # Cyklus pro hlavní menu
        while True:

            # Načtení vstupu z hlavního menu
            result = radiolist_dialog(
                title='',
                text='Vyberte požadovaný úkon:',
                values=[
                    ('config', 'Změnit konfiguraci'),
                    ('menu', 'Hlavní menu'),
                    ('help', 'Zobrazit nápovědu'),
                    ('exit', 'Ukončit interaktivní režim')
                ],
                style=dialog_style
            ).run()

            # Pokud byl zadán požadavek na změnu konfigurace
            if result == 'config':
                run_config_settings()

            # Pokud byl zadán požadavek na nápovědu
            elif result == 'menu':
                run_main_menu()

            # Pokud byl zadán požadavek na nápovědu
            elif result == 'help':
                show_help()

            # Pokud byl zadán požadavek na ukončení interaktivního režimu
            if result == 'exit':
                ExitInteractiveMode()

    # Pokud došlo k přerušení interaktivního modu
    except ExitInteractiveMode as e:
        exit_interactive_mode(e.message)




run_config_exit_options()