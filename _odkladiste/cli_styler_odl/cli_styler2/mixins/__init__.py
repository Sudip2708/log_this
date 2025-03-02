from .check_style_attributes import CheckStyleAttributesMixin
from .set_current_styles_attributes import SetCurrentStylesAttributesMixin
from .set_colors_mode import SetColorsModeMixin
from .set_sign_set import SetSignSetMixin

__all__ = [

    "CheckStyleAttributesMixin",  # Metoda pro kontzolu atributů
    # Přidává metody: check_style_attributes(styles_dict), get_style_attributes_set(), raise_attributes_error(attributes_set, styles_set)

    "SetCurrentStylesAttributesMixin",   # Metoda pro změnu/nastavení atributů pro styly
    # Přidává metody: set_current_styles_attributes(), get_current_styles_dict(), set_style_attributes(styles_dict)
    # Přidává atributy: _signs_sets, _current_signs_set, _colors_modes, _current_colors_mode
    # Používá metody: check_style_attributes(styles_dict)

    "SetColorsModeMixin",   # Metoda pro změnu barevného modu
    # Přidává metody: set_colors_mode(colors_mode), validate_colors_mode(colors_mode)
    # Používá metody: get_current_styles_attributes()
    # Používá atributy: _colors_modes, _current_colors_mode

    "SetSignSetMixin",   # Metoda pro změnu sady znaků
    # Přidává metody: set_sign_set(signs_set), validate_signs_set(signs_set)
    # Používá metody: get_current_styles_attributes()
    # Používá atributy: _signs_sets, _current_signs_set

]