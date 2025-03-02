from abc import ABC
from abc_helper import abc_method
from ..settings import get_styles_dict
from .._style_class import StyleClass

class SetCurrentStylesAttributesMixin(ABC):

    check_style_attributes = abc_method("check_style_attributes")

    # Nastavení značek
    _signs_sets = {"set_a": 0, "set_b": 1, "native": 3}
    _current_signs_set  = "set_b"

    # Nastavení barevného modu
    _colors_modes = {"dark": 0, "light": 1, "native": 2}
    _current_colors_mode = "dark"

    def set_current_styles_attributes(self):
        """Metoda pro změnu/nastavení atributů pro styly"""
        styles_dict = self._get_current_styles_dict()
        self.check_style_attributes(styles_dict)
        self._set_style_attributes(styles_dict)

    def _get_current_styles_dict(self):
        """Metoda pro získání ID vybraného barevného režimu a sady značek"""
        sings_id = self._signs_sets[self._current_signs_set]
        colors_id = self._colors_modes[self._current_colors_mode]
        return get_styles_dict(sings_id, colors_id)

    def _set_style_attributes(self, styles_dict):
        """Metoda pro dianmické přidání/přepsání atributů"""
        for key, (sing, style) in styles_dict.items():
            setattr(self, key, StyleClass(sing, style))
