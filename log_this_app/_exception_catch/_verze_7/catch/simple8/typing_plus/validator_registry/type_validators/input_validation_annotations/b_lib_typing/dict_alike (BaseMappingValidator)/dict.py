from typing import Dict

from ...._bases import BaseMappingValidator, K, V


class DictValidator(BaseMappingValidator):
    """
    Validátor pro typovou anotaci Dict[K, V]

    Dict reprezentuje slovník, který mapuje klíče typu K na hodnoty typu V. Jedná se o
    hashovatelnou kolekci, kde každý klíč musí být unikátní a hashovatelný. Na rozdíl od
    jiných kolekcí umožňuje rychlý přístup k hodnotám na základě klíčů.

    Syntaxe:
        - Dict[K, V]           # Preferovaný zápis (vyžaduje import z typing)
        - dict[K, V]           # Od Python 3.9+
        - dict                 # Obecný slovník bez specifikace typu klíčů a hodnot

    Příklady použití:
        - Dict[str, int]       # Slovník mapující řetězce na celá čísla
        - Dict[int, List[str]] # Slovník mapující celá čísla na seznamy řetězců
        - Dict[str, Any]       # Slovník s řetězcovými klíči a libovolnými hodnotami
        - Dict[Tuple[str, int], bool] # Slovník s klíči typu (řetězec, číslo) a boolean hodnotami

    Vnitřní typy:
        Anotace Dict vyžaduje specifikaci dvou typů:
        - K: typ klíčů (musí být hashovatelný - immutable)
        - V: typ hodnot (může být libovolný)

    Validační proces:
        1. Ověří, zda hodnota je instance typu dict
        2. Pokud je požadována hloubková kontrola, ověří typy všech klíčů a hodnot
        3. Pro každý pár klíč-hodnota validuje klíč proti typu K a hodnotu proti typu V
        4. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_config(config: Dict[str, Any]) -> None
        - Pro návratové hodnoty: def get_user_stats() -> Dict[str, int]
        - Pro typování proměnných: user_data: Dict[str, str] = {"name": "Alice", "email": "alice@example.com"}

    Kompatibilita:
        - Dict je kompatibilní s Mapping a MutableMapping
        - Dict je specifickou implementací obecnějšího rozhraní Mapping
        - Dict není kompatibilní s List nebo Tuple
        - Dict může být použit jako typ hodnot v jiném slovníku

    Související typy:
        - DefaultDict: slovník s výchozí hodnotou pro neexistující klíče
        - OrderedDict: slovník s garantovaným pořadím vkládání
        - Mapping: read-only rozhraní pro slovníky
        - MutableMapping: měnitelné rozhraní pro slovníky

    Omezení:
        - Klíče musí být hashovatelné (immutable) - např. str, int, tuple, frozenset
        - Nelze použít měnitelné typy jako list, dict nebo set jako klíče
        - Klíče musí být unikátní v rámci slovníku

    Běžné chyby:
        - Zapomenutí importu: from typing import Dict
        - Pokus o použití nehashable typu jako klíče (např. list, dict)
        - Záměna pořadí typů v anotaci (Dict[hodnota, klíč] místo Dict[klíč, hodnota])
        - Spoléhání na pořadí klíčů v slovníku (není garantováno před Python 3.7)

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Dict
        - https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
        - https://peps.python.org/pep-0585/ (nativní generické typy)
    """

    VALIDATOR_KEY = "dict"
    ANNOTATION = Dict[K, V], dict[K, V], dict
    INFO = "Definuje slovník"
    ORIGIN = dict
