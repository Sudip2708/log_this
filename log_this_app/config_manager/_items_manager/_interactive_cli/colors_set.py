from typing import Any

from .._abc_config_key import ConfigKey

class ColorsSetKey(ConfigKey):
    """Konfigurační klíč pro odsazení"""

    INFO = "Nastavení barevného modu pro interaktivní režim."
    DEFAULT_VALUE = "dark"
    LABEL = "Nastavit barevný mod"
    OPTIONS = (
        "Povolené hodnoty pro klíč 'colors': ",
        "light (Mod pro světlý režim)",
        "dark (Mod pro tmavý režim)",
        "native (Bez barev - nativní vzhled)"
    )
    HINT = (
        "Klíč 'colors' nastavuje jaký barevný mod se má používat pro CLI výpis do konzole. ",
        "Nastavením hodnoty 'light' získáme barevnou sadu určenou pro světlé pozadí. ",
        "Nastavením hodnoty 'dark' získáme barevnou sadu určenou pro tmavé pozadí. ",
        "Nastavením hodnoty 'native' nastavíme nativní vzhled (bez přidaných barev). ",
    )
    VALUES_TITLE = "VYBERTE BAREVNÝ MOD:"
    VALUES_DICT = {
        "light": "Mod pro světlý režim",
        "dark": "Mod pro tmavý režim",
        "native": "Bez barev - nativní vzhled"
    }
    CATEGORY = "interactive_cli"
