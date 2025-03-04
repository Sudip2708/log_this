# print("cli_styler/_symbols/symbol_scheme.py")
from abc_helper import AbcSingletonMeta
from ._symbols_definitions import symbols_definitions

class SymbolScheme(metaclass=AbcSingletonMeta):

    symbol_modes_choices = {
        "ascii": "Základní set symbolů",
        "emoji": "Obrázkové symboly",
        "no_symbols": "Symboly nezobrazovat"
    }

    symbols = None

    def __call__(self, mode: str):
        self.validate_mode(mode)
        self.symbols = {
            symbol: definitions.get(mode, "")
            for symbol, definitions
            in symbols_definitions.items()}
        return self.symbols

    def validate_mode(self, mode: str):
        if mode not in self.symbol_modes_choices:
            raise ValueError(
                f"Neplatný mod pro definici značek: {mode}. "
                f"Povolené mody: {', '.join(self.symbol_modes_choices)}"
            )

