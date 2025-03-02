from abc_helper import AbcSingletonMeta
from ._symbols_definitions import symbols_definitions

class SymbolScheme(metaclass=AbcSingletonMeta):

    symbols_modes_choices = [
        "ascii",
        "emoji",
        "no_symbols"
    ]

    colors = None

    def __call__(self, mode: str):
        self.validate_mode(mode)
        self.colors = {
            color: definitions.get(mode, "")
            for color, definitions
            in symbols_definitions.items()}
        return self.colors

    def validate_mode(self, mode: str):
        if mode not in self.symbols_modes_choices:
            raise ValueError(
                f"Neplatný mod pro definici značek: {mode}. "
                f"Povolené mody: {', '.join(self.symbols_modes_choices)}"
            )

