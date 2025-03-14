from abc import ABC, abstractmethod
from typing import Any

from .._abc_config_key import ConfigKey

class ModeConfigKey(ConfigKey):
    """Základní třída pro konfigurační klíče reprezentující módy"""

    INFO = None
    DEFAULT_VALUE = None
    LABEL = None
    OPTIONS = (
        "Povolené hodnoty pro mod:",
        "0 (Nastavuje přeskočení logování.)",
        "1 (Nastavuje jednořádkový výpis.)",
        "2 (Nastavuje základní výpis (4 řádky).)",
        "3 (Nastavuje rozšířený výpis (6 řádky).)",
        "4 (Nastavuje podrobný výpis (10+ řádků).)"
    )
    HINT = (
        "Klíč nastavuje chování logování. ",
        "Pro dočasnou celopločnou změnu chování.",
        "Doporučuje se ponechat defaultní hodnotu."
    )
    VALUES_DICT = {
        0: "Bez logování",
        1: "Jednořádkový výstup",
        2: "Základní výpis (4 řádky)",
        3: "Rozšířený výpis (6 řádek)",
        4: "Report (10+ řádek)"
    }
    CATEGORY = "log_this_modes"



class SkipThisKey(ModeConfigKey):
    """Konfigurační klíč pro přeskočení logování"""
    INFO = "Slovní definice modu pro přeskočení logování."
    DEFAULT_VALUE = 0
    LABEL = "Nastavení modu 'skip_this'"


class OneLineKey(ModeConfigKey):
    """Konfigurační klíč pro jednořádkové logování"""
    INFO = "Slovní definice modu pro jednořádkové logování."
    DEFAULT_VALUE = 1
    LABEL = "Nastavení modu 'one_line'"


class SimpleKey(ModeConfigKey):
    """Konfigurační klíč pro základní logování"""
    INFO = "Slovní definice modu pro základní mod umožňující vnořené logování (4 řádky)."
    DEFAULT_VALUE = 2
    LABEL = "Nastavení modu 'simple'"


class DetailedKey(ModeConfigKey):
    """Konfigurační klíč pro rozšířené logování"""
    INFO = "Slovní definice modu pro rozšířený mod umožňující vnořené logování (6 řádky)."
    DEFAULT_VALUE = 3
    LABEL = "Nastavení modu 'detailed'"

class ReportKey(ModeConfigKey):
    """Konfigurační klíč pro podrobné logování"""
    INFO = "Slovní definice modu pro podrobný výpis logování (10+ řádků)."
    DEFAULT_VALUE = 4
    LABEL = "Nastavení modu 'report'"

class TrueKey(ModeConfigKey):
    """Konfigurační klíč pro kladnou boolean hodnotu"""
    INFO = "Nastavení pro zadání modu jako kladné boolean hodnoty True."
    DEFAULT_VALUE = 1
    LABEL = "Nastavení modu True"

class FalseKey(ModeConfigKey):
    """Konfigurační klíč pro zápornou boolean hodnotu"""
    INFO = "Nastavení pro zadání modu jako záporné boolean hodnoty False."
    DEFAULT_VALUE = 0
    LABEL = "Nastavení modu False"

class NoneKey(ModeConfigKey):
    """Konfigurační klíč pro None hodnotu"""
    INFO = "Nastavení pro zadání modu jako None hodnoty."
    DEFAULT_VALUE = 0
    LABEL = "Nastavení modu None"

class EmptyKey(ModeConfigKey):
    """Konfigurační klíč pro prázdnou hodnotu"""
    INFO = "Nastavení pro výchozí chování, pokud mod není zadán."
    DEFAULT_VALUE = 0
    LABEL = "Nastavení když mod není uveden"