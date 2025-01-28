from prompt_toolkit.shortcuts import radiolist_dialog
from log_this.manager.config.styler import dialog_style

from log_this.manager.config.styler import cli_print
from ..dialogs import exit_interactive_mode, show_help
from ..exceptions import ExitInteractiveMode
from ..runners import run_config_settings


def run_main_menu(self) -> None:
    """Spustí interaktivní režim a zobrazí hlavní menu."""

    # Intro
    cli_print( "title"
        "Vítejte v interaktivním režimu konfigurace LogThis!\n"
    )

    try:

        # Cyklus pro hlavní menu
        while True:

            # Načtení vstupu z hlavního menu
            result = radiolist_dialog(
                title='Hlavní menu',
                text='Vyberte požadovaný úkon:',
                values=[
                    ('config', 'Změnit konfiguraci'),
                    ('help', 'Zobrazit nápovědu'),
                    ('exit', 'Ukončit interaktivní režim')
                ],
                style=dialog_style
            ).run()

            # Pokud byl zadán požadavek na změnu konfigurace
            if result == 'config':
                run_config_settings()

            # Pokud byl zadán požadavek na nápovědu
            elif result == 'help':
                show_help()

            # Pokud byl zadán požadavek na ukončení interaktivního režimu
            if result == 'exit':
                ExitInteractiveMode()

    # Pokud došlo k přerušení interaktivního modu
    except ExitInteractiveMode as e:
        exit_interactive_mode(e.message)




