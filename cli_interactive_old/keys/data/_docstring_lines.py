from ._abc_config_key import ConfigKey
from typing import Any

class DocstringLinesKey(ConfigKey):
    """Konfigurační klíč pro počet řádků z docstringu"""

    INFO = "Nastavení zobrazení docstringu v plném výpisu logování."
    DEFAULT_VALUE = 3
    OPTIONS = (
        "Povolené hodnoty pro klíč 'docstring_lines': \n"
        "- Celé kladné číslo (Nastavuje počet řádků z docstringu, které se mají ve modu 'report' objevit.) \n"
        "- 'all' (Nastavuje aby se při výpisu modu 'report' zobrazoval celý obsah docstringu.)"
    )
    HINT = (
        "Klíč 'docstring_lines' nastavuje zobrazení docstringu ve výstupu pro mod 'report'. \n"
        "Pokud je zadaná hodnota celé číslo, vztahuje se pouze na řádky s textem. Prázdné řádky jsou vynechány. \n"
        "Pokud je zadaná hodnota 'all' docstring se objeví v podobě v jaké je zapsán."
    )
    VALUES_DICT = {
        1: "Pouze první řádek obsahující text",
        3: "3 první řádky obsahující text",
        10: "10 řádků obsahujících text",
        "all": "Přepis celého docstringu v nezměněnné podobě",
        "input": "Nastavení vlastní hodnoty"
    }

    def validate(self, value: Any) -> bool:
        return (
                value == 'all'
                or (isinstance(value, int)
                    and not isinstance(value, bool)
                    and value >= 0)
        )