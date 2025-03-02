print("cli_styler/cli_styler.py")
from abc_helper import AbcSingletonMeta
from ._colors import ColorScheme
from ._symbols import SymbolScheme
from ._styles_settings import CLIPrint, GetStyles


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
            self._symbols = self._symbols_scheme(symbol_mode)
            self._initialize()
            # Potvrzení o proběhlé inicializaci
            self._initialized = True


    def _initialize(self):
        """Inicializuje CLI styler a printer podle aktuálních módů."""
        self.get_style = GetStyles(self._colors, self._symbols)
        self.cli_print = CLIPrint(self._colors, self._symbols)


    def set_mode(self, color_mode: str = None, symbol_mode: str = None):
        """Změní mód a znovu inicializuje styly."""
        if color_mode:
            self._colors = self._colors_scheme(color_mode)
        if symbol_mode:
            self._symbols = self._symbols_scheme(symbol_mode)
        self._initialize()


# Použití StyleManageru
styler = CliStyler()
cli_print = styler.cli_print
get_style = styler.get_style

