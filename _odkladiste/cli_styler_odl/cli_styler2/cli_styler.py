# file: cli_styler.py
from ..abc_helper import AbcSingletonMeta

from .mixins import (
    CheckStyleAttributesMixin,
    SetCurrentStylesAttributesMixin,
    SetColorsModeMixin,
    SetSignSetMixin
)

class CLIStyler(

    CheckStyleAttributesMixin,  # Metoda pro kontzolu atributů
    # Přidává metody: check_style_attributes(styles_dict), get_style_attributes_set(), raise_attributes_error(attributes_set, styles_set)

    SetCurrentStylesAttributesMixin,
    # Metoda pro změnu/nastavení atributů pro styly
    # Přidává metody: set_current_styles_attributes(), get_current_styles_dict(), set_style_attributes(styles_dict)
    # Přidává atributy: _signs_sets, _current_signs_set, _colors_modes, _current_colors_mode
    # Používá metody: check_style_attributes(styles_dict)

    SetColorsModeMixin,  # Metoda pro změnu barevného modu
    # Přidává metody: set_colors_mode(colors_mode), validate_colors_mode(colors_mode)
    # Používá metody: get_current_styles_attributes()
    # Používá atributy: _colors_modes, _current_colors_mode

    SetSignSetMixin,  # Metoda pro změnu sady znaků
    # Přidává metody: set_sign_set(signs_set), validate_signs_set(signs_set)
    # Používá metody: get_current_styles_attributes()
    # Používá atributy: _signs_sets, _current_signs_set

    metaclass=AbcSingletonMeta
):
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
        """Dinamické načtení atributů a inicializace singleton vzoru"""
        if not hasattr(self, "_initialized"):
            self.set_current_styles_attributes()
            self._initialized = True




