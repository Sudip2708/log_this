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
    warning_direction = None

    # Informativní oznamy
    info_title = None
    info_text = None

    # Oznamy o úspěchu
    success_title = None
    success_text = None

    # Styl pro vstupní pole
    prompt_input = None

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
# Printy
print_intro_title = cs.intro_title.print_styled
print_intro_end = cs.intro_end.print_styled

print_error_title = cs.error_title.print_styled
print_error_text = cs.error_text.print_styled

print_warning_title = cs.warning_title.print_styled
print_warning_text = cs.warning_text.print_styled
print_warning_direction = cs.warning_direction.print_styled

print_info_title = cs.info_title.print_styled
print_info_text = cs.info_text.print_styled

print_success_title = cs.success_title.print_styled
print_success_text = cs.success_text.print_styled

# Styly
get_menu_title = cs.menu_title.get_styled
get_menu_offer = cs.menu_offer.get_styled
get_menu_selected = cs.menu_selected.get_styled

get_hint_title = cs.hint_title.get_styled
get_hint_offer = cs.hint_offer.get_styled

get_prompt_input = cs.prompt_input.get_styled

