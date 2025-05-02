from typing import DefaultDict
from collections import defaultdict

from ...._bases import DictionaryValidatorBase, K, V


class DefaultDictValidator(DictionaryValidatorBase):
    """
    Validátor pro typovou anotaci DefaultDict[K, V]

    DefaultDict reprezentuje slovník, který automaticky vytváří výchozí hodnoty pro neexistující klíče
    prostřednictvím zadané tovární funkce. Na rozdíl od běžného slovníku nevyvolává výjimku KeyError
    při přístupu k neexistujícímu klíči, ale místo toho vytvoří novou položku s výchozí hodnotou.

    Syntaxe:
        - DefaultDict[K, V]           # Vyžaduje import z typing
        - collections.defaultdict[K, V] # Od Python 3.9+
        - collections.defaultdict      # Obecný defaultdict bez specifikace typů

    Příklady použití:
        - DefaultDict[str, int]       # DefaultDict s řetězcovými klíči a celočíselnými hodnotami
        - DefaultDict[str, List[int]] # DefaultDict s řetězcovými klíči a seznamy celých čísel
        - DefaultDict[int, str]       # DefaultDict s celočíselnými klíči a řetězcovými hodnotami
        - DefaultDict[K, set]         # DefaultDict vracející prázdné množiny pro nové klíče

    Vnitřní typy:
        Anotace DefaultDict vyžaduje specifikaci dvou typových parametrů:
        - K: Typ klíčů (musí být hashable)
        - V: Typ hodnot (také specifikuje typ výchozí hodnoty)

    Validační proces:
        1. Ověří, zda hodnota je instance typu collections.defaultdict
        2. Pokud je požadována hloubková kontrola, ověří typy všech klíčů a hodnot
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def count_words(text: str) -> DefaultDict[str, int]
        - Pro návratové hodnoty: def group_by_category() -> DefaultDict[str, List[Item]]
        - Pro typování proměnných: word_counts: DefaultDict[str, int] = defaultdict(int)

    Srovnání s podobnými typy:
        - DefaultDict vs dict: DefaultDict automaticky vytváří výchozí hodnoty, zatímco dict vyvolává KeyError
        - DefaultDict vs Counter: Counter je specializovaný typ defaultdict s výchozí hodnotou 0, optimalizovaný pro počítání
        - DefaultDict vs OrderedDict: DefaultDict generuje výchozí hodnoty, OrderedDict zachovává pořadí vložení

    Běžné vzory použití:
        - Počítání výskytů: defaultdict(int)
        - Seskupování prvků: defaultdict(list)
        - Vytváření vnořených struktur: defaultdict(lambda: defaultdict(int))
        - Zajištění výchozích hodnot: defaultdict(lambda: "N/A")

    Běžné chyby:
        - Zapomenutí importu: from typing import DefaultDict nebo from collections import defaultdict
        - Neuvedení factory funkce při vytváření instance: defaultdict bez parametru způsobí TypeError
        - Záměna pořadí typu klíče a hodnoty v anotaci
        - Nerespektování konzistence typu výchozí hodnoty s typem V

    Reference:
        - https://docs.python.org/3/library/collections.html#collections.defaultdict
        - https://docs.python.org/3/library/typing.html#typing.DefaultDict
        - https://peps.python.org/pep-0585/ (nativní generické typy)
    """

    VALIDATOR_KEY = "defaultdict"
    ANNOTATION = DefaultDict[K,V]

    IS_INSTANCE = defaultdict
    HAS_ATTRS = "__getitem__", "__setitem__", "__delitem__", "__iter__", "__len__", "default_factory"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Slovník s výchozí hodnotou"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí defaultdict z knihovny collections. "
            "Umožňuje nastavit výchozí hodnotu pro nové klíče."
        )
