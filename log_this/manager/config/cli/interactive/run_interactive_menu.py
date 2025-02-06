from prompt_toolkit.shortcuts import radiolist_dialog

from ..styler import cli_print, dialog_style
from .dialogs import exit_interactive_mode, show_help
from .exceptions import ExitInteractiveMode
from .run_config_settings import run_config_settings
from .run_config_footer_options import run_config_footer_options

from log_this.manager.config import (
    print_current_settings,
    reset_default,
    reset_previous,
    export_config_to_file,
    import_config_from_file,
)

from ..pickers import input_path


def run_interactive_menu(intro=True) -> None:
    """Spustí interaktivní režim a zobrazí hlavní menu."""

    # Intro
    if intro:
        cli_print(
            "title"
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
                    ('show-current', 'Ukázat aktuální konfiguraci s popisem'),
                    ('set', 'Změnit konfiguraci zadáním klíče a hodnoty'),
                    ('reset-previous', 'Změnit konfiguraci na předešlou'),
                    ('reset-default', 'Změnit konfiguraci na defaultní hodnoty'),
                    ('export', 'Uložit aktuální konfiguraci do souboru'),
                    ('import', 'Načíst konfigurace ze souboru'),
                    ('help', 'Zobrazit nápovědu'),
                    ('exit', 'Ukončit interaktivní režim')
                ],
                style=dialog_style
            ).run()

            # Pokud byl zadán požadavek na výpis aktuální konfigurace
            if result == 'show-current':
                print_current_settings()

            # Pokud byl zadán požadavek na změnu konfigurace zadáním klíče a hodnoty
            elif result == 'set':
                run_config_settings()

            # Pokud byl zadán požadavek na změnu konfigurace na předešlou
            elif result == 'reset-previous':
                reset_previous()

            # Pokud byl zadán požadavek na změnu konfigurace na defaultní hodnoty
            elif result == 'reset-default':
                reset_default()

            # Pokud byl zadán požadavek na expost konfigurace do souboru
            elif result == 'export':
                path = input_path()
                export_config_to_file(path)

            # Pokud byl zadán požadavek na načtení konfigurace ze souboru
            elif result == 'import':
                path = input_path()
                import_config_from_file(path)

            # Pokud byl zadán požadavek na nápovědu
            elif result == 'help':
                show_help()

            # Pokud byl zadán požadavek na ukončení interaktivního režimu
            elif result == 'exit':
                ExitInteractiveMode()

            # Patička s nabítkou hlavního menu nebo ukončení interaktivního režimu
            run_config_footer_options(run_interactive_menu)

    # Pokud došlo k přerušení interaktivního modu
    except ExitInteractiveMode as e:
        exit_interactive_mode(e.message)




