from ._abc_config_key import ConfigKey
from typing import Any

class MaxDepthKey(ConfigKey):
    """Konfigurační klíč pro maximální hloubku rekurze"""

    INFO = "Nastavení úrovně maximální rekurze pro serializaci dat."
    DEFAULT_VALUE = 100
    OPTIONS = (
        "Povolené hodnoty pro klíč 'max_depth': \n"
        "- Celé kladné číslo (Nastavuje maximální počet vnitřní rekurze při serializaci dat.)"
    )
    HINT = (
        "Klíč 'max_depth' nastavuje limit rekurze pro serializaci (bezpečnou extrakci obsahu) pro data uložená v zanořených sekvencích. \n"
        "- Tato kontrola se hodí, pokud máte zájem zjistit zda nedochází v kodu k nadměrné rekurzi vnitřního volání. \n"
        "- Defaultně je nastavena na hodnotu 100, kde je již velká pravděpodobnost že se jedná o chybu rekurze. \n"
        "- Pro detailnější analýzu kodu se však někdy mohou hodit i velmi malé hodnoty. \n"
        "- Upozornění: Pokud necháte nastavenou malou hodnotu, může se vám stát, že bude hlášen falešný error pro kód který je v pořádku."
    )
    VALUES_DICT = {
        0: "Bez možnosti rekurze - pro ladění jednoho kodu",
        3: "3 rekurzní volání - pro ladění jednoho kodu",
        10: "10 rekurzních volání - pro detekci hlubší rekurze",
        100: "100 rekurzních volání - pro bezpečný chod aplikace",
        "input": "Nastavení vlastní hodnoty"
    }

    def validate(self, value: Any) -> bool:
        return (
                isinstance(value, int)
                and not isinstance(value, bool)
                and value >= 0
        )