from typing import Any

from .._abc_config_key import ConfigKey
from .._config_category import ConfigCategory

class IndentKey(ConfigKey):
    """Konfigurační klíč pro odsazení"""

    INFO = "Nastavení počtu mezer odsazení od kraje pro zanořené logování."
    DEFAULT_VALUE = 2
    OPTIONS = (
        "Povolené hodnoty pro klíč 'indent': ",
        "0 (Skrytí odsazení.) ",
        "od 1 do 4 (Počet mezer pro jedno odsazení.) "
    )
    HINT = (
        "Klíč 'indent' nastavuje počet mezer odsazení od kraje pro zanořené logování. ",
        "Pro skrytí odsazení slouží hodnota 0. ",
        "Více než 4 mezery pro jedno odsazení nelze zadat. "
    )
    VALUES_DICT = {
        0: "Bez odsazení",
        1: "Odsazení o 1 mezeru",
        2: "Odsazení o 2 mezery",
        3: "Odsazení o 3 mezery",
        4: "Odsazení o 4 mezery"
    }
    CATEGORY = ConfigCategory.APPEARANCE
