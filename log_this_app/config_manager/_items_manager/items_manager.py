# print("_menus_settings/menus_manager.py")
from typing import Dict, Union


from ._apperance import (
    IndentKey,
    BlankLinesKey,
    DocstringLinesKey,
    MaxDepthKey,
)
from ._mode_settings import (
    SkipThisKey,
    OneLineKey,
    SimpleKey,
    DetailedKey,
    ReportKey,
    TrueKey,
    FalseKey,
    NoneKey,
    EmptyKey
)

from ._interactive_cli import (
    ColorsSetKey,
    SymbolsSetKey
)

"""

Napojit na interaktivní režim výpis a natsavení hodnot

Udělat to samé i pro CLI příkazy - při chybě aktivovat interaktivná mod.

Dopsat logiku pro změnu interaktivního režimu s uložením do souboru

Vymyslet, kde by měli být centralizované funkce pro CLI a sjednotit výstup

Pořešit chbové oznami jakožto CLI komunikace

Zamyslet se nad tím, zd a cli_styler pouze importovat 
a inicializovat pouze jednou při startu knihovny?

"""

from ._load_config_mixin import LoadConfigMixin

class ConfigItemsManager(LoadConfigMixin):
    """Spravuje jednotlivé třídy pro konfigurace"""

    cm = None

    KEYS_DATA = {

        # Nastavení chování
        'indent': IndentKey(),
        'blank_lines': BlankLinesKey(),
        'docstring_lines': DocstringLinesKey(),
        'max_depth': MaxDepthKey(),

        # Nastavení módů
        'skip_this': SkipThisKey(),
        'one_line': OneLineKey(),
        'simple': SimpleKey(),
        'detailed': DetailedKey(),
        'report': ReportKey(),
        'true': TrueKey(),
        'false': FalseKey(),
        'none': NoneKey(),
        'empty': EmptyKey(),

        # Nastavení interaktivního režimu
        'colors': ColorsSetKey(),
        'symbols': SymbolsSetKey(),

        # Ostatní nastavení

    }

    def __init__(self, config_manager):

        # Načtení přístupu k hlavní třídě
        self.cm = config_manager


    def value_validation(self, key, value):
        if key in self.KEYS_DATA.keys():
            return self.KEYS_DATA[key].validate(value)
        else:
            raise KeyError(
                f"Byl zadán neplatný klíč pro validaci: {key}"
                f"Podporované klíče: {', '.join(self.KEYS_DATA.keys())}"
            )


    def default_values(self) -> Dict[str, Union[int, str, bool]]:
        """Vrátí slovník s výchozími hodnotami konfigurace."""
        return {
            key: config_key.DEFAULT_VALUE
            for key, config_key in self.KEYS_DATA.items()
        }

    def all_keys_with_descriptions(self) -> list:
        """Vrátí seznam všech klíčů s popisem."""
        outcome = []
        for key, config_key in self.KEYS_DATA.items():
            outcome.append(f"'{key}' - {config_key.info}")
        return outcome


    def get_key_class_for_category(self, category: str) -> dict:
        """Vrátí seznam klíčů pro danou kategorii"""
        # return [key for key in self.KEYS_DATA.values() if key.CATEGORY == category]
        return {
            key: key_class
            for key, key_class in self.KEYS_DATA.items()
            if key_class.CATEGORY == category
        }


