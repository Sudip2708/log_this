# print("cli_styler/cli_styler.py")
from abc_helper import AbcSingletonMeta
from ._colors import ColorScheme
from ._symbols import SymbolScheme
from ._styles_settings import StylesManager
from ._style_printer import StylePrinter
from .utils.get_method_hierarchy import get_method_hierarchy

class CliStyler(metaclass=AbcSingletonMeta):

    # _color_scheme = ColorScheme()
    # _symbol_scheme = SymbolScheme()
    # VALID_KEYS = "colors", "symbols"
    VALID_KEYS = {
        "colors": ColorScheme(),
        "symbols": SymbolScheme()
    }

    def __init__(self,
                 color_mode: str = "dark",
                 symbol_mode: str = "ascii"
                 ):

        # Kontrola zda již proběhla inicializace
        if not hasattr(self, "_initialized"):

            # Inicializace barevného režimu
            self._colors = self.VALID_KEYS["colors"](color_mode)

            # Inicializace setu značek
            self._symbols = self.VALID_KEYS["symbols"](symbol_mode)

            # Inicializace třídy
            self._initialize_styler()

            # Potvrzení o proběhlé inicializaci
            self._initialized = True


    def _initialize_styler(self):
        """Inicializuje CLI styler a printer podle aktuálních módů."""
        self.get_style = StylesManager(self._colors, self._symbols)
        self.cli_print = StylePrinter(self.get_style)

    def multiple_input(self, style_method, *lines):
        """Vytiskne více řádků s uživatelem zadaným stylem."""
        try:
            for line in lines:
                style_method(line)
        except AttributeError:
            print(f"Chyba: Neplatný styl: {style_method}")
            print(f"Diagnostika zápisu:")
            self._check_style_method(style_method)
            print("Možné řešení: Opravte zápis stylu.")

        except Exception as e:
            print(f"Neočekávaná chyba: {e}")

    def _check_style_method(self, style_method):
        """
        Ověří, zda metoda stylování existuje.
        """
        hierarchy = get_method_hierarchy(style_method)

        # Ověříme první úroveň (musí být `styler`)
        if hierarchy[0] != "CliStyler":
            print(f"Neplatný kořen stylu: {hierarchy[0]}.")

        # Ověření `cli_print` nebo `get_style`
        if hierarchy[1] not in ["cli_print", "get_style"]:
            print(f"Neplatný hlavní styler: {hierarchy[1]}.")

        # Ověření názvu stylu
        if not hasattr(getattr(self, hierarchy[1]), hierarchy[2]):
            print(f"Styl '{hierarchy[2]}' neexistuje v {hierarchy[1]}.")

        # Ověření položky stylu
        style_instance = getattr(getattr(self, hierarchy[1]), hierarchy[2])
        if not hasattr(style_instance, hierarchy[3]):
            print(f"Položka '{hierarchy[3]}' neexistuje ve stylu '{hierarchy[2]}'.")

    def set_color_mode(self, color_mode: str = None):
        """Změní mód a znovu inicializuje styly."""
        if color_mode in self._color_scheme.color_modes:
            self._colors = self._color_scheme(color_mode)
            self._initialize_styler()
        else:
            raise ValueError(
                f"Byl zadán nepodporovaný barevný mod: {color_mode}"
                f"Podporované mody: {', '.join(self._color_scheme.color_modes)}"
            )

    def set_symbol_mode(self, symbol_mode: str = None):
        """Změní mód a znovu inicializuje styly."""
        if symbol_mode in self._symbol_scheme.symbol_modes:
            self._symbols = self._symbol_scheme(symbol_mode)
            self._initialize_styler()
        else:
            raise ValueError(
                f"Byl zadán nepodporovaný mod pro značky: {symbol_mode}"
                f"Podporované mody: {', '.join(self._symbol_scheme.symbol_modes)}"
            )

    def change_mode(self, key, mode):
        self.validate_key(key)




    def validate_key(self, key):
        if key not in self.VALID_KEYS:
            raise ValueError(
                f"Byl zadán nepodporovaný klíč: {key}"
                f"Podporované klíče: {', '.join(self.VALID_KEYS)}"
            )

    def validate_value(self, key, value):
        self.validate_key(key)








# Použití StyleManageru
styler = CliStyler()
cli_print = styler.cli_print
get_style = styler.get_style
set_colors_mode = styler.set_color_mode
set_symbols_mode = styler.set_symbol_mode


