from abc_helper import AbcSingletonMeta
from ._colors_definitions import colors_definitions

class ColorScheme(metaclass=AbcSingletonMeta):

    colors_modes_choices = [
        "light",
        "dark",
        "native_mode"
    ]

    colors = None

    def __call__(self, mode: str):
        self.validate_mode(mode)
        self.colors = {
            color: definitions.get(mode, "")
            for color, definitions
            in colors_definitions.items()}
        return self.colors

    def validate_mode(self, mode: str):
        if mode not in self.colors_modes_choices:
            raise ValueError(
                f"Neplatný mod pro barevný režim: {mode}. "
                f"Povolené mody: {', '.join(self.colors_modes_choices)}"
            )

