from ._abc_config_key import ConfigKey
from typing import Any

class ModeConfigKey(ConfigKey):
    """Základní třída pro konfigurační klíče reprezentující módy"""

    OPTIONS = (
        "Povolené hodnoty pro mod: \n"
        "- 0 (Nastavuje přeskočení logování.) \n"
        "- 1 (Nastavuje jednořádkový výpis.) \n"
        "- 2 (Nastavuje základní výpis (4 řádky).) \n"
        "- 3 (Nastavuje rozšířený výpis (6 řádky).) \n"
        "- 4 (Nastavuje podrobný výpis (10+ řádků).)"
    )

    HINT = (
        "Klíč nastavuje chování logování. "
        "Pro dočasnou celopločnou změnu chování. \n"
        "Doporučuje se ponechat defaultní hodnotu."
    )
    VALUES_DICT = {
        0: "Bez logování",
        1: "Jednořádkový výstup",
        2: "Základní výpis (4 řádky)",
        3: "Rozšířený výpis (6 řádek)",
        4: "Report (10+ řádek)"
    }

    def validate(self, value: Any) -> bool:
        return (
                value in (0, 1, 2, 3, 4)
                and not isinstance(value, bool)
        )


class SkipThisKey(ModeConfigKey):
    """Konfigurační klíč pro přeskočení logování"""
    INFO = "Slovní definice modu pro přeskočení logování."
    DEFAULT_VALUE = 0


class OneLineKey(ModeConfigKey):
    """Konfigurační klíč pro jednořádkové logování"""
    INFO = "Slovní definice modu pro jednořádkové logování."
    DEFAULT_VALUE = 1


class SimpleKey(ModeConfigKey):
    """Konfigurační klíč pro základní logování"""
    INFO = "Slovní definice modu pro základní mod umožňující vnořené logování (4 řádky)."
    DEFAULT_VALUE = 2


class DetailedKey(ModeConfigKey):
    """Konfigurační klíč pro rozšířené logování"""
    INFO = "Slovní definice modu pro rozšířený mod umožňující vnořené logování (6 řádky)."
    DEFAULT_VALUE = 3


class ReportKey(ModeConfigKey):
    """Konfigurační klíč pro podrobné logování"""
    INFO = "Slovní definice modu pro podrobný výpis logování (10+ řádků)."
    DEFAULT_VALUE = 4


class TrueKey(ModeConfigKey):
    """Konfigurační klíč pro kladnou boolean hodnotu"""
    INFO = "Nastavení pro zadání modu jako kladné boolean hodnoty True."
    DEFAULT_VALUE = 1


class FalseKey(ModeConfigKey):
    """Konfigurační klíč pro zápornou boolean hodnotu"""
    INFO = "Nastavení pro zadání modu jako záporné boolean hodnoty False."
    DEFAULT_VALUE = 0


class NoneKey(ModeConfigKey):
    """Konfigurační klíč pro None hodnotu"""
    INFO = "Nastavení pro zadání modu jako None hodnoty."
    DEFAULT_VALUE = 0


class EmptyKey(ModeConfigKey):
    """Konfigurační klíč pro prázdnou hodnotu"""
    INFO = "Nastavení pro výchozí chování, pokud mod není zadán."
    DEFAULT_VALUE = 0