from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

from .all_mixins import AllMixins
from log_this.manager.config import config
from .styler import ConfigStyler


class InteractiveMode(AllMixins):
    """
    Třída pro správu interaktivního režimu konfigurace LogThis.

    Poskytuje uživatelské rozhraní pro:
    - Prohlížení a úpravu konfiguračních hodnot
    - Zobrazení nápovědy
    - Navigaci pomocí šipek a potvrzení entrem
    """

    def __init__(self):
        """
        Inicializace instance interaktivního režimu.
        """
        self.config_inst = config
        self.keys_data = config.keys_data
        self.session = PromptSession()
        self.styler = ConfigStyler()


"""
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl

# 1. Základní definice stylů
custom_style = Style.from_dict({
    # Základní styly pro dialogy
    'dialog': 'bg:#4444aa #ffffff',
    'dialog.body': 'bg:#000000 #ffffff',
    'dialog.border': '#004400',
    
    # Styly pro různé stavy
    'selected': 'bg:#ffffff #000000',
    'error': 'bg:#ff0000 #ffffff bold',
    
    # Vlastní třídy pro použití v textu
    'custom.warning': 'fg:#ff8800 italic',
    'custom.success': 'fg:#00ff00',
    
    # Styly pro specifické komponenty
    'button': 'bg:#888888 #ffffff',
    'button.focused': 'bg:#aaaaaa #000000',
})

# 2. Použití s formátovaným textem
formatted_text = FormattedText([
    ('class:custom.warning', 'Varování: '),
    ('class:dialog.body', 'Toto je běžný text'),
    ('class:custom.success', ' (OK)'),
])

# 3. Funkce pro stylovaný výstup
def print_styled_text():
    # Použití HTML-like syntaxe
    print_formatted_text(
        HTML('<custom.warning>Varování</custom.warning>: '
             'Nějaký <dialog.body>důležitý text</dialog.body>'),
        style=custom_style
    )
    
    # Přímé použití FormattedText
    print_formatted_text(formatted_text, style=custom_style)

# 4. Použití v UI komponentách
def create_styled_window():
    return Window(
        content=FormattedTextControl(formatted_text),
        style='class:dialog.body'
    )

# 5. Příklad použití v dialogu
def show_styled_dialog():
    from prompt_toolkit.shortcuts import radiolist_dialog
    
    result = radiolist_dialog(
        title='Výběr možnosti',
        text='Vyberte jednu z následujících možností:',
        values=[
            ('opt1', 'První možnost'),
            ('opt2', 'Druhá možnost'),
        ],
        style=custom_style
    ).run()
    
    return result
"""