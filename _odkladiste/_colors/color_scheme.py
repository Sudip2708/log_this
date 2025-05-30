# print("cli_styler/_colors/color_scheme.py")
from abc_helper import AbcSingletonMeta
from ._colors_definitions import colors_definitions

class ColorScheme(metaclass=AbcSingletonMeta):


    color_modes = ("light", "dark", "native")

    def __call__(self, mode: str):
        self.validate_mode(mode)
        self.colors = {
            color: definitions.get(mode, "")
            for color, definitions
            in colors_definitions.items()}
        return self.colors

    def validate_mode(self, mode: str):
        if mode not in self.color_modes:
            raise ValueError(
                f"Neplatný mod pro barevný režim: {mode}. "
                f"Povolené mody: {', '.join(self.color_modes)}"
            )

