# cli_styler/cli_styler.py
from abc_helper import AbcSingletonMeta

from .mixins import (
    GetCurrentIdsMixin,
    CheckStyleAttributesMixin,
    ApplyStylesToAttributesMixin,
    SetColorsModeMixin,
    SetSymbolsModeMixin
)

class CLIStyler(

    GetCurrentIdsMixin,
    # Mixin definující sety značek a mody barev
    # Přidává atributy: _symbols_modes, _current_symbols_mode, _colors_modes, _current_colors_mode
    # Přidává metody: _get_current_ids()

    CheckStyleAttributesMixin,
    # Mixin pro kontrolu zda nahrávané styli odpovýdají atributům
    # Přidává metody: _check_style_attributes(styles_dict), _get_style_attributes_set(),
    # Používá utils: _raise_attributes_error(attributes_set, styles_set)

    ApplyStylesToAttributesMixin,
    # Mixin pro změnu atributů na daný styl
    # Přidává metody: _apply_styles_to_attributes(), _set_style_attributes(styles_dict)
    # Přidává atributy: _symbols_modes, _current_symbols_mode, _colors_modes, _current_colors_mode
    # Používá metody: check_style_attributes(styles_dict)

    SetColorsModeMixin,
    # Mixin pro změnu barevného modu
    # Přidává metody: set_colors_mode(colors_mode), _validate_colors_mode(colors_mode)
    # Používá metody: _apply_styles_to_attributes()
    # Používá atributy: _colors_modes, _current_colors_mode

    SetSymbolsModeMixin,
    # Mixin pro změnu sady znaků
    # Přidává metody: set_symbols_mode(signs_set), _validate_symbols_mode(signs_set)
    # Používá metody: _apply_styles_to_attributes()
    # Používá atributy: _symbols_modes, _current_symbols_mode

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
    hint_text = None

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
        """
        Inicializace třídy dle singleton vzoru.

        Pokud třída ještě není inicializovaná,
        volá se metoda která přepíše všechny atributy pro styl
        na instance třídy StyleClass obsahující nastavení stylů
        a metody pro navrácení stylu jako tuple (styl, text),
        a metody pro vytisknutí stylu do konzole.
        """

        # Kontrola zda je třída již inicializovaná
        if not hasattr(self, "_initialized"):

            # Volání metody pro přiřazení stylů k atributům
            self._apply_styles_to_attributes()

            # Zaznamenání provedené inicializace
            self._initialized = True




