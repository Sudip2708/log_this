# file: cli_styler.py
from ._style_class import StyleClass
from .utils import get_class_attributes_set, attributes_check
from .constants import styles_dict


class CLIStyler:
    """Třída obsahující definice všech stylů s kontrolou konzistence."""

    # Úvod a ukončení interaktivního režimu
    intro_title = None
    intro_end = None

    # Položky pro interaktivní menu
    menu_title = None
    menu_offer = None
    menu_selected = None

    # Položky nápovědy pro ovládání interaktivního menu
    hint_title = None
    hint_offer = None

    # Chybové oznamy
    error_title = None
    error_text = None

    # Varování
    warning_title = None
    warning_text = None

    # Informativní oznamy
    info_title = None
    info_text = None

    # Oznamy o úspěchu
    success_title = None
    success_text = None

    # Styl pro vstupní pole
    cli_input = None

    def __init__(self):
        """Inicializace třídy, dynamické přiřazení stylů a kontrola konzistence."""

        # Získáme seznam atributů třídy (jen ty, které jsou relevantní)
        attributes_set = get_class_attributes_set(dir(self))

        # Seznam dostupných stylů ve slovníku
        styles_set = set(styles_dict.keys())

        # Kontrola zda se shodují
        attributes_check(attributes_set, styles_set)

        # Dynamicky přiřadíme instance StyleClass ke všem atributům
        for key, (symbol, style) in styles_dict.items():
            setattr(self, key, StyleClass(symbol, style))


# Vytvoření instance CLIStyler
cs = CLIStyler()
# Vytvoření stylerů
intro_title = cs.intro_title
intro_end = cs.intro_end
menu_title = cs.menu_title
menu_offer = cs.menu_offer
menu_selected = cs.menu_selected
hint_title = cs.hint_title
hint_offer = cs.hint_offer
error_title = cs.error_title
error_text = cs.error_text
warning_title = cs.warning_title
warning_text = cs.warning_text
info_title = cs.info_title
info_text = cs.info_text
success_title = cs.success_title
success_text = cs.success_text
cli_input = cs.cli_input
