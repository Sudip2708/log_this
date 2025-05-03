from typing import Mapping
from collections.abc import Mapping as MappingOrigin

from ...._bases import BaseIterableKeyValueValidator, K, V


class MappingValidator(BaseIterableKeyValueValidator):
    """
    Validátor pro typovou anotaci Mapping[K, V]

    Mapping reprezentuje abstraktní základní třídu pro všechny mapovací (slovníkové) datové
    struktury, které podporují přístup ke klíčům, iteraci a obsahují metody jako keys(),
    items() a values(). Na rozdíl od konkrétních implementací jako Dict nebo OrderedDict je
    Mapping obecný protokol definující pouze čtecí operace.

    Syntaxe:
        - Mapping[K, V]              # Vyžaduje import z typing
        - collections.abc.Mapping[K, V] # Od Python 3.9+
        - collections.abc.Mapping    # Obecný mapping bez specifikace typů

    Příklady použití:
        - Mapping[str, int]          # Mapování řetězcových klíčů na celočíselné hodnoty
        - Mapping[int, str]          # Mapování celých čísel na řetězce
        - Mapping[str, Any]          # Mapování řetězcových klíčů na libovolné hodnoty
        - Mapping[K, List[V]]        # Mapování klíčů typu K na seznamy typu V

    Vnitřní typy:
        Anotace Mapping vyžaduje specifikaci dvou typových parametrů:
        - K: Typ klíčů (musí být hashable)
        - V: Typ hodnot (libovolný podporovaný typ)

    Validační proces:
        1. Ověří, zda hodnota implementuje protokol collections.abc.Mapping
        2. Pokud je požadována hloubková kontrola, ověří typy všech klíčů a hodnot
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_data(data: Mapping[str, Any]) -> None
        - Pro návratové hodnoty: def get_config() -> Mapping[str, str]
        - Pro typování proměnných: settings: Mapping[str, int] = {"timeout": 30, "retries": 3}

    Srovnání s podobnými typy:
        - Mapping vs Dict: Mapping definuje pouze rozhraní pro čtení, zatímco Dict
          umožňuje i modifikaci
        - Mapping vs MutableMapping: Mapping nepodporuje změny obsahu, MutableMapping ano
        - Mapping vs Sequence: Mapping používá klíče pro přístup k prvkům, Sequence používá indexy

    Běžné vzory použití:
        - Funkce akceptující jakýkoliv slovníkový objekt: def process(data: Mapping[str, Any])
        - Neměnné datové struktury v API: def get_config() -> Mapping[str, str]
        - Abstraktní definice rozhraní: class ConfigStore(Protocol): def get_all(self) -> Mapping[str, Any]

    Běžné chyby:
        - Zapomenutí importu: from typing import Mapping nebo from collections.abc import Mapping
        - Pokus o modifikaci Mapping objektu (pro modifikaci je určen MutableMapping)
        - Použití nehashable typů jako klíčů (např. list)
        - Záměna s Dict v případech, kdy je třeba zdůraznit pouze čtecí přístup

    Reference:
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping
        - https://docs.python.org/3/library/typing.html#typing.Mapping
        - https://peps.python.org/pep-0544/ (protokoly a strukturální podtypy)
    """

    VALIDATOR_KEY = "mapping"
    ANNOTATION = Mapping[K, V]

    IS_INSTANCE = MappingOrigin
    DUCK_TYPING = {
        "has_attr": ("__getitem__", "__iter__", "__len__"),
    }

    DESCRIPTION = "Mapovací rozhraní (slovník)"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje rozhraní Mapping z collections.abc, "
            "tedy že je neměnnou mapou s metodami jako __getitem__, __iter__ a __len__."
        )
