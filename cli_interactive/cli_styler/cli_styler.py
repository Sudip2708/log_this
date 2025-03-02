# print("cli_styler/cli_styler.py")
from abc_helper import AbcSingletonMeta
from ._colors import ColorScheme
from ._symbols import SymbolScheme
from ._styles_settings import StylesManager
from ._style_printer import StylePrinter

class CliStyler(metaclass=AbcSingletonMeta):

    _colors_scheme = ColorScheme()
    _symbols_scheme = SymbolScheme()


    def __init__(self,
                 color_mode: str = "dark",
                 symbol_mode: str = "ascii"
                 ):

        # Kontrola zda již proběhla inicializace
        if not hasattr(self, "_initialized"):
            # Inicializace třídy
            self._colors = self._colors_scheme(color_mode)
            self.colors_modes = self._colors_scheme.colors_modes_choices
            self._symbols = self._symbols_scheme(symbol_mode)
            self.symbols_modes = self._symbols_scheme.symbols_modes_choices
            self._initialize_styler()
            # Potvrzení o proběhlé inicializaci
            self._initialized = True


    def _initialize_styler(self):
        """Inicializuje CLI styler a printer podle aktuálních módů."""
        self.get_style = StylesManager(self._colors, self._symbols)
        self.cli_print = StylePrinter(self.get_style)


    def set_colors_mode(self, color_mode: str = None):
        """Změní mód a znovu inicializuje styly."""
        if color_mode in self.colors_modes:
            self._colors = self._colors_scheme(color_mode)
            self._initialize_styler()
        else:
            raise ValueError(
                f"Byl zadán nepodporovaný barevný mod: {color_mode}"
                f"Podporované mody: {', '.join(self.colors_modes)}"
            )

    def set_symbols_mode(self, symbol_mode: str = None):
        """Změní mód a znovu inicializuje styly."""
        if symbol_mode in self.symbols_modes:
            self._symbols = self._symbols_scheme(symbol_mode)
            self._initialize_styler()
        else:
            raise ValueError(
                f"Byl zadán nepodporovaný mod pro značky: {symbol_mode}"
                f"Podporované mody: {', '.join(self.symbols_modes)}"
            )


# Použití StyleManageru
styler = CliStyler()
cli_print = styler.cli_print
get_style = styler.get_style
set_colors_mode = styler.set_colors_mode
set_symbols_mode = styler.set_symbols_mode

