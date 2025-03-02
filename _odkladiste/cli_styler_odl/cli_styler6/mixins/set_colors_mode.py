from abc import ABC
from abc_helper import abc_method, abc_property

class SetColorsModeMixin(ABC):

    _colors_modes = abc_property("_colors_modes")
    _current_colors_mode = abc_property("_current_colors_mode")
    set_current_styles_attributes = abc_method("set_current_styles_attributes")


    def _validate_colors_mode(self, colors_mode):
        """Metoda pro validaci barevného režimu"""
        if not colors_mode in self._colors_modes.keys():
            raise ValueError(f"Byl zadán neplatný set barvy. "
                             f"Povolené sety: {self._colors_modes.keys()}")


    def set_colors_mode(self, colors_mode):
        """
        Metoda pro změnu barevného modu

        Metoda nejprve se pokusí změnit barevný mod ve třídě CLIColor
        - pokud bude zadaný neplatný barevný mod metoda change_mode vyvolá výjimku

        Následně metoda spustí metodu pro změnu hodnot atributů této třídy
        """
        self._validate_colors_mode(colors_mode)
        self._current_colors_mode = self._colors_modes[colors_mode]
        self.set_current_styles_attributes()
