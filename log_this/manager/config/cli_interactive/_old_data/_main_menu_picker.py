from prompt_toolkit.shortcuts import radiolist_dialog
from log_this.manager.config.styler import dialog_style

def main_menu_picker() -> str:
    """
    Zobrazí hlavní menu s možnostmi výběru.

    Returns:
        str: Klíč vybrané akce
    """

    # Vytvoření pickeru
    return radiolist_dialog(
        title='Hlavní menu',
        text='Vyberte požadovaný úkon:',
        values=[
            ('config', 'Změnit konfiguraci'),
            ('help', 'Zobrazit nápovědu'),
            ('exit', 'Ukončit interaktivní režim')
        ],
        style=dialog_style
    ).run()