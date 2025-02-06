from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.styles import Style

# from log_this.manager.config.cli.styler import dialog_style
from log_this.manager.config.cli.interactive.dialogs._exit_interactive_mode import exit_interactive_mode
from log_this.manager.config.cli.interactive.dialogs._show_help import show_help
from log_this.manager.config.cli.interactive.exceptions._exit_interactive_mode import ExitInteractiveMode
from log_this.manager.config.cli.interactive.run_interactive_menu import run_interactive_menu

from .run_interactive_menu import run_interactive_menu


def run_interactive_teaser() -> None:
    """Spustí interaktivní režim a zobrazí hlavní menu."""

    try:

        # Cyklus pro hlavní menu
        while True:

            # Načtení vstupu z hlavního menu
            result = radiolist_dialog(
                title='Chcete pokračovat skrze interaktivní režim?',
                text='Vyberte jednu z následujících možností:',
                values=[
                    ('interactive', 'Zpustit interaktivní režim'),
                    ('help', 'Zobrazit nápovědu'),
                    ('exit', 'Opustit tento dialog')
                ],
                style=Style.from_dict({
                    'dialog':           'fg:white bg:blue',
                    'dialog.body':      'fg:white bg:black',
                    'dialog.border':    'fg:green',
                    'selected':         'fg:black bg:white',
                    'key.name':         'fg:bold italic',
                    'key.info':         'fg:gray'
                })
            ).run()

            # Pokud byl zadán požadavek na změnu konfigurace
            if result == 'interactive':
                run_interactive_menu()

            # Pokud byl zadán požadavek na nápovědu
            elif result == 'help':
                show_help()

            # Pokud byl zadán požadavek na ukončení interaktivního režimu
            if result == 'exit':
                ExitInteractiveMode()

    # Pokud došlo k přerušení interaktivního modu
    except ExitInteractiveMode as e:
        exit_interactive_mode(e.message)




