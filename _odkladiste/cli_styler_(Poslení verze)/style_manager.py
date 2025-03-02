from abc_helper import AbcSingletonMeta
from ._colors import ColorScheme
from ._symbols import SymbolScheme
from ._cli_styler import CliStyler
from ._cli_printer import StylePrinter

class StyleManager(metaclass=AbcSingletonMeta):

    _colors = ColorScheme()
    _symbols = SymbolScheme()


    def __init__(self,
                 color_mode: str = "dark",
                 symbol_mode: str = "ascii"
                 ):

        # Kontrola zda již proběhla inicializace
        if not hasattr(self, "_initialized"):
            # Inicializace třídy
            self._colors(color_mode)
            self._symbols(symbol_mode)
            self._initialize_styler()
            # Potvrzení o proběhlé inicializaci
            self._initialized = True


    def _initialize_styler(self):
        """Inicializuje CLI styler a printer podle aktuálních módů."""
        self.cli_style = CliStyler(self._colors, self._symbols)
        self.cli_print = StylePrinter(self.cli_style)


    def set_mode(self, color_mode: str = None, symbol_mode: str = None):
        """Změní mód a znovu inicializuje styly."""
        if color_mode:
            self._colors(color_mode)
        if symbol_mode:
            self._symbols(symbol_mode)
        self._initialize_styler()  # Nová inicializace


# Použití StyleManageru
styler = StyleManager()
cli_print = styler.cli_print
cli_style = styler.cli_style

