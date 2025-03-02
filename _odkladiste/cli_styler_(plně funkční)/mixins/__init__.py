# cli_styler/mixins/__init__.py
from ._check_style_attributes import CheckStyleAttributesMixin
from ._apply_styles_to_attributes import ApplyStylesToAttributesMixin
from ._set_colors_mode import SetColorsModeMixin
from ._set_symbols_mode import SetSymbolsModeMixin
from ._get_current_ids import GetCurrentIdsMixin

__all__ = [

    "GetCurrentIdsMixin",
    # Mixin definující sety značek a mody barev
    # Přidává atributy: _symbols_modes, _current_symbols_mode, _colors_modes, _current_colors_mode
    # Přidává metody: _get_current_ids()

    "CheckStyleAttributesMixin",
    # Mixin pro kontrolu zda nahrávané styli odpovýdají atributům
    # Přidává metody: _check_style_attributes(styles_dict), _get_style_attributes_set(),
    # Používá utils: _raise_attributes_error(attributes_set, styles_set)

    "ApplyStylesToAttributesMixin",
    # Mixin pro změnu atributů na daný styl
    # Přidává metody: _apply_styles_to_attributes(), _set_style_attributes(styles_dict)
    # Přidává atributy: _symbols_modes, _current_symbols_mode, _colors_modes, _current_colors_mode
    # Používá metody: check_style_attributes(styles_dict)

    "SetColorsModeMixin",
    # Mixin pro změnu barevného modu
    # Přidává metody: set_colors_mode(colors_mode), _validate_colors_mode(colors_mode)
    # Používá metody: _apply_styles_to_attributes()
    # Používá atributy: _colors_modes, _current_colors_mode

    "SetSymbolsModeMixin",
    # Mixin pro změnu sady znaků
    # Přidává metody: set_symbols_mode(signs_set), _validate_symbols_mode(signs_set)
    # Používá metody: _apply_styles_to_attributes()
    # Používá atributy: _symbols_modes, _current_symbols_mode

]