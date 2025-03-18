# print("cli_styler/cli_styler.py")
from abc_helper import AbcSingletonMeta
from ._colors import ColorScheme
from ._symbols import SymbolScheme
from ._styles_settings import StylesManager
from ._style_printer import StylePrinter
from .utils.get_method_hierarchy import get_method_hierarchy

class CliStyler(metaclass=AbcSingletonMeta):

    _color_scheme = ColorScheme()
    _symbol_scheme = SymbolScheme()


    def __init__(self,
                 color_mode: str = "dark",
                 symbol_mode: str = "ascii"
                 ):

        # Kontrola zda již proběhla inicializace
        if not hasattr(self, "_initialized"):

            # Inicializace barevného režimu
            # Načtení barevného schématu
            self._colors = self._color_scheme(color_mode)
            # Atribut pro slovník s klíči a labely jednotlivých modů
            self.color_modes = self._color_scheme.color_modes_choices
            # Aktuálně zvolený mod (jako klíč k slovníku color_modes)
            self.color_mode = color_mode

            # Inicializace setu značek
            self._symbols = self._symbol_scheme(symbol_mode)
            self.symbol_modes = self._symbol_scheme.symbol_modes_choices
            self.symbol_mode = symbol_mode

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
        if color_mode in self.color_modes:
            self._colors = self._color_scheme(color_mode)
            self.color_mode = color_mode
            self._initialize_styler()
        else:
            raise ValueError(
                f"Byl zadán nepodporovaný barevný mod: {color_mode}"
                f"Podporované mody: {', '.join(self.color_modes)}"
            )

    def set_symbol_mode(self, symbol_mode: str = None):
        """Změní mód a znovu inicializuje styly."""
        if symbol_mode in self.symbol_modes:
            self._symbols = self._symbol_scheme(symbol_mode)
            self.symbol_mode = symbol_mode
            self._initialize_styler()
        else:
            raise ValueError(
                f"Byl zadán nepodporovaný mod pro značky: {symbol_mode}"
                f"Podporované mody: {', '.join(self.symbol_modes)}"
            )


    def get_current_color_mode_id(self):
        """Metoda pro získání id klíče modu barev"""
        mode_keys_list = list(self.color_modes.keys())
        return mode_keys_list.index(self.color_mode) if (
                self.color_mode in mode_keys_list) else 0


    def get_current_symbol_mode_id(self):
        """Metoda pro získání id klíče modu barev"""
        mode_keys_list = list(self.symbol_modes.keys())
        return mode_keys_list.index(self.symbol_mode) if (
                self.symbol_mode in mode_keys_list) else 0


# Použití StyleManageru
styler = CliStyler()
cli_print = styler.cli_print
get_style = styler.get_style
set_colors_mode = styler.set_color_mode
set_symbols_mode = styler.set_symbol_mode


