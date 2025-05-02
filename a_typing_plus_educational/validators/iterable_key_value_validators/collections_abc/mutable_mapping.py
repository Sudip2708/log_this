from typing import MutableMapping
from collections.abc import MutableMapping as MutableMappingOrigin

from ...._bases import DictionaryValidatorBase, K, V


class MutableMappingValidator(DictionaryValidatorBase):
    """
    Validátor pro typovou anotaci MutableMapping[K, V]

    MutableMapping reprezentuje abstraktní základní třídu pro všechny mapovací (slovníkové)
    datové struktury, které jsou měnitelné a podporují jak čtení, tak zápis dat. Rozšiřuje
    protokol Mapping o operace pro modifikaci obsahu jako __setitem__(), __delitem__(),
    clear(), update() a pop().

    Syntaxe:
        - MutableMapping[K, V]              # Vyžaduje import z typing
        - collections.abc.MutableMapping[K, V] # Od Python 3.9+
        - collections.abc.MutableMapping    # Obecný mutable mapping bez specifikace typů

    Příklady použití:
        - MutableMapping[str, int]          # Měnitelné mapování řetězců na celá čísla
        - MutableMapping[int, List[str]]    # Měnitelné mapování celých čísel na seznamy řetězců
        - MutableMapping[str, Any]          # Měnitelné mapování řetězců na libovolné hodnoty
        - MutableMapping[K, Dict[str, V]]   # Měnitelné mapování klíčů K na slovníky

    Vnitřní typy:
        Anotace MutableMapping vyžaduje specifikaci dvou typových parametrů:
        - K: Typ klíčů (musí být hashable)
        - V: Typ hodnot (libovolný podporovaný typ)

    Validační proces:
        1. Ověří, zda hodnota implementuje protokol collections.abc.MutableMapping
        2. Pokud je požadována hloubková kontrola, ověří typy všech klíčů a hodnot
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def update_config(settings: MutableMapping[str, Any]) -> None
        - Pro návratové hodnoty: def create_cache() -> MutableMapping[str, bytes]
        - Pro typování proměnných: cache: MutableMapping[str, int] = {}

    Srovnání s podobnými typy:
        - MutableMapping vs Mapping: MutableMapping podporuje modifikaci obsahu, Mapping pouze čtení
        - MutableMapping vs Dict: MutableMapping je abstraktní protokol, Dict je konkrétní implementace
        - MutableMapping vs defaultdict/OrderedDict: MutableMapping je nadřazený protokol pro tyto
          specializované implementace

    Běžné vzory použití:
        - Funkce modifikující obsah slovníku: def update_settings(config: MutableMapping[str, Any])
        - Cache systémy: cache: MutableMapping[str, bytes] = {}
        - Vlastní implementace slovníkových struktur: class MyCache(MutableMapping[K, V])
        - Adaptéry a proxy objekty pro databáze: class DbDict(MutableMapping[str, JSON])

    Běžné chyby:
        - Zapomenutí importu: from typing import MutableMapping nebo from collections.abc import MutableMapping
        - Implementace vlastních tříd bez všech požadovaných metod rozhraní
        - Záměna s Mapping v případech, kdy je potřeba zdůraznit měnitelnost
        - Použití nehashable typů jako klíčů (např. list)

    Reference:
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping
        - https://docs.python.org/3/library/typing.html#typing.MutableMapping
        - https://peps.python.org/pep-0544/ (protokoly a strukturální podtypy)
    """

    VALIDATOR_KEY = "mutablemapping"
    ANNOTATION = MutableMapping[K, V]

    IS_INSTANCE = MutableMappingOrigin
    HAS_ATTRS =  "__getitem__", "__setitem__", "__delitem__", "__iter__", "__len__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Změnitelná mapa (slovník)"
    LONG_DESCRIPTION = (
            "Validuje, že objekt implementuje MutableMapping z collections.abc, "
            "tedy že podporuje změnu položek, přidávání a mazání klíčů."
        )
