from typing import Any

from .._abc_config_key import ConfigKey

class SymbolsSetKey(ConfigKey):
    """Konfigurační klíč pro odsazení"""

    INFO = "Nastavení sady značek používaných v interaktivním režimu."
    DEFAULT_VALUE = "ascii"
    LABEL = "Nastavit zobrazení značek"
    OPTIONS = (
        "Povolené hodnoty pro klíč 'symbols': ",
        "ascii (Základní set symbolů)",
        "emoji (Obrázkové symboly)",
        "no_symbols (Symboly nezobrazovat)"
    )
    HINT = (
        "Klíč 'symbols' nastavuje zda a jaké značky se mají používat pro CLI výpis do konzole. ",
        "Nastavením hodnoty 'ascii' získáme základní sadu značek vykreslených přes ascii sekvence. ",
        "Nastavením hodnoty 'emoji' získáme obrázkovou sadu značek. ",
        "Nastavením hodnoty 'no_symbols' skryjeme zobrazení značek. ",
    )
    VALUES_TITLE = "VYBERTE SET ZNAČEK:"
    VALUES_DICT = {
        "ascii": "Základní set symbolů",
        "emoji": "Obrázkové symboly",
        "no_symbols": "Symboly nezobrazovat"
    }
    CATEGORY = "interactive_cli"
