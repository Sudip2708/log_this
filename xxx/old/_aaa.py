from prompt_toolkit.shortcuts import radiolist_dialog, button_dialog
from prompt_toolkit.styles import Style

def run_interactive_teaser() -> None:
    """Spustí interaktivní režim a zobrazí hlavní menu."""

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
                # Nastavení pozadí kolem dialogového okna
                "dialog": "bg:black",
                # Nastavení pozadí a barvy textu v dialogovém okně
                "dialog.body": "fg:grey bg:black",
                # Nastavení ohraničení kolem dialogového okna
                "frame": "fg:black",
                # Nastavení barvy textu nabídky
                "radio": "fg:yellow",
                # Nastavení barvy pozadí a textu tlačítek OK a Cancel
                "button": "bg:blue",
                # Nastavení barvy pozadí a textu při výběru
                "button.focused": "fg:yellow bold",
            }),

        ).run()


        print(f'Vybraná možnost: {result}')
        break

run_interactive_teaser()


