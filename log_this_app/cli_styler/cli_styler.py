# print("cli_styler/cli_styler.py")
from abc_helper import AbcSingletonMeta
from ._styles_settings import StylesManager
from ._style_printer import StylePrinter
from .utils.get_method_hierarchy import get_method_hierarchy

from ._colors_definitions import COLOR_MODES, COLOR_DEFINITIONS
from ._symbols_definitions import SYMBOL_MODES, SYMBOL_DEFINITIONS

class CliStyler(metaclass=AbcSingletonMeta):


    VALID_KEYS = {
        "colors": {
            "modes": COLOR_MODES,
            "definitions": COLOR_DEFINITIONS
        },
        "symbols": {
            "modes": SYMBOL_MODES,
            "definitions": SYMBOL_DEFINITIONS
        },
    }
    _colors = None
    _symbols = None

    def __init__(self,
                 color_mode: str = "dark",
                 symbol_mode: str = "ascii"
                 ):

        # Kontrola zda již proběhla inicializace
        if not hasattr(self, "_initialized"):

            # Inicializace barevného režimu
            self._initialize_colors(color_mode)
            self._initialize_symbols(symbol_mode)

            # Inicializace třídy
            self._initialize_styler()

            # Potvrzení o proběhlé inicializaci
            self._initialized = True


    # Inicializace barevného režimu
    def _initialize_colors(self, color_mode):
        self._colors = self.get_current_style("colors", color_mode)

    # Inicializace setu značek
    def _initialize_symbols(self, symbol_mode):
        self._symbols = self.get_current_style("symbols", symbol_mode)

    # Pomocná metorda pro inicializaci výstupních hodnot
    def _initialize_styler(self):
        """Inicializuje CLI styler a printer podle aktuálních módů."""
        self.get_style = StylesManager(self._colors, self._symbols)
        self.cli_print = StylePrinter(self.get_style)

    # Pomocná metoda pro validaci klíče
    def _validate_key(self, key):
        valid_keys = self.VALID_KEYS.keys()
        if key not in valid_keys:
            raise ValueError(
                f"Byl zadán nepodporovaný klíč: {key}"
                f"Podporované klíče: {', '.join(valid_keys)}"
            )

    # Metoda pro validaci klíče a hodnoty
    def validate_key_and_value(self, key, value):
        self._validate_key(key)
        valid_modes = self.VALID_KEYS[key]["modes"].keys()
        if not value in valid_modes:
            raise ValueError(
                f"Pro klíč '{key}' byla zadána nepodporovaná hodnota: {value}"
                f"Podporované hodnoty: {', '.join(valid_modes)}"
            )

    # Metoda pro získání modu
    def get_current_style(self, key, value):

        # Validace klíče a hodnoty
        self.validate_key_and_value(key, value)

        # Načtení stylů
        definitions = self.VALID_KEYS[key]["definitions"]

        # Vrácení slovníku aktuálního stylu
        return {
            color_name: color_sets.get(value, "")
            for color_name, color_sets in definitions.items()
        }

    # Metoda pro změnu modu
    def change_mode(self, key, value):
        # Validace klíče a hodnoty
        self.validate_key_and_value(key, value)

        # Změna modu
        if key == "colors":
            self._initialize_colors(value)
        elif key == "symbols":
            self._initialize_symbols(value)

        # Reinicializace třídy
        self._initialize_styler()

    # Metoda pro zadání více řádků
    def multiple_input(self, style_method, *lines):
        """Vytiskne více řádků s uživatelem zadaným stylem."""
        try:
            for line in lines:
                # print("### line", line)
                style_method(line)
        except AttributeError:
            print(f"Chyba: Neplatný styl: {style_method}")
            print(f"Diagnostika zápisu:")
            self._check_style_method(style_method)
            print("Možné řešení: Opravte zápis stylu.")

        except Exception as e:
            print(f"Neočekávaná chyba: {e}")

    # Pomocná metoda pro diagnostiku chyb
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



# Použití StyleManageru
styler = CliStyler()
cli_print = styler.cli_print
get_style = styler.get_style



