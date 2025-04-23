from typing import OrderedDict
from collections import OrderedDict as OrderedDictOrigin

from ..._bases import BaseMappingValidator, K, V


class OrderedDictValidator(BaseMappingValidator):
    """
    Validátor pro typovou anotaci OrderedDict[K, V]

    OrderedDict reprezentuje slovník, který si pamatuje pořadí vkládání položek. Na rozdíl
    od běžného slovníku dict zachovává OrderedDict pořadí vložených prvků při iteraci,
    což je užitečné pro případy, kdy záleží na pořadí klíčů.

    Syntaxe:
        - OrderedDict[K, V]           # Vyžaduje import z typing
        - collections.OrderedDict[K, V] # Od Python 3.9+
        - collections.OrderedDict      # Obecný OrderedDict bez specifikace typů

    Příklady použití:
        - OrderedDict[str, int]       # OrderedDict s řetězcovými klíči a celočíselnými hodnotami
        - OrderedDict[int, List[str]] # OrderedDict s celočíselnými klíči a seznamy řetězců
        - OrderedDict[str, Any]       # OrderedDict s řetězcovými klíči a libovolnými hodnotami
        - OrderedDict[Hashable, T]    # OrderedDict s hashable klíči a hodnotami typu T

    Vnitřní typy:
        Anotace OrderedDict vyžaduje specifikaci dvou typových parametrů:
        - K: Typ klíčů (musí být hashable)
        - V: Typ hodnot (libovolný podporovaný typ)

    Validační proces:
        1. Ověří, zda hodnota je instance typu collections.OrderedDict
        2. Pokud je požadována hloubková kontrola, ověří typy všech klíčů a hodnot
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_config(config: OrderedDict[str, Any]) -> None
        - Pro návratové hodnoty: def get_sorted_items() -> OrderedDict[str, int]
        - Pro typování proměnných: priorities: OrderedDict[str, int] = OrderedDict([("high", 3), ("medium", 2), ("low", 1)])

    Srovnání s podobnými typy:
        - OrderedDict vs dict: Od Python 3.7 je i běžný dict uspořádaný, ale OrderedDict
          nabízí dodatečné metody jako move_to_end() a popitem(last=False)
        - OrderedDict vs TypedDict: TypedDict specifikuje typy pro konkrétní klíče,
          zatímco OrderedDict specifikuje jednotný typ pro všechny klíče

    Běžné chyby:
        - Zapomenutí importu: from typing import OrderedDict nebo from collections import OrderedDict
        - Záměna s běžným dict v případech, kdy záleží na metodách specifických pro OrderedDict
        - Použití nehashable typů jako klíčů (např. list)

    Reference:
        - https://docs.python.org/3/library/collections.html#collections.OrderedDict
        - https://docs.python.org/3/library/typing.html#typing.OrderedDict
        - https://peps.python.org/pep-0585/ (nativní generické typy)
    """

    VALIDATOR_KEY = "ordereddict"
    ANNOTATION = OrderedDict[K, V]
    INFO = "Definuje slovník typu OrderedDict s typovanými klíči a hodnotami."
    ORIGIN = OrderedDictOrigin