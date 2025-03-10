from typing import Any

from .._abc_config_key import ConfigKey
from .._config_category import ConfigCategory


class BlankLinesKey(ConfigKey):
    """Konfigurační klíč pro prázdné řádky"""

    INFO = "Nastavení, zda se mají mezi jednotlivými logy zobrazovat prázdné řádky."
    DEFAULT_VALUE = True
    OPTIONS = (
        "Povolené hodnoty pro klíč 'blank_lines': \n"
        "- True (Nastavuje zobrazení prázdné řádky mezi jednotlivými logy.) \n"
        "- False (Nastavuje aby jednotlivé logy nebyli oddělené prázdnou řádkou.)"
    )
    HINT = (
        "Klíč 'blank_lines' nastavuje zobrazení/skrytí prázdné řádky mezi jednotlivými logy. "
        "Pro jednořádkové výpisy je přehlednější výstup bez prázdné řádky (hodnota: False). \n"
        "Pro víceřádkové výpisy je přehlednější výstup s prázdnou řádkou (hodnota: True)."
    )
    VALUES_DICT = {
        True: "Zobrazit mezi logy prázdný řádek",
        False: "Nezobrazovat mezi logy prázdný řádek",
    }
    CATEGORY = ConfigCategory.APPEARANCE
