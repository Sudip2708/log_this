from typing import Counter, get_args
from collections import Counter as CounterOrigin

from ...._bases import DictionaryValidatorBase, K
from ...._validators import dictionary_validator_for_counter


class CounterValidator(DictionaryValidatorBase):
    """
    Validátor pro typovou anotaci Counter[K]

    Counter reprezentuje speciální typ slovníku určený k počítání výskytů prvků. Klíče
    reprezentují počítané prvky a hodnoty jejich četnost. Counter je podtřídou dict, která
    poskytuje dodatečné metody pro snadné počítání a manipulaci s četnostmi.

    Syntaxe:
        - Counter[K]                  # Vyžaduje import z typing
        - collections.Counter[K]      # Od Python 3.9+
        - collections.Counter         # Obecný Counter bez specifikace typu prvků

    Příklady použití:
        - Counter[str]                # Counter pro počítání výskytů řetězců
        - Counter[int]                # Counter pro počítání výskytů celých čísel
        - Counter[Tuple[str, int]]    # Counter pro počítání výskytů n-tic

    Vnitřní typy:
        Anotace Counter vyžaduje specifikaci pouze jednoho typového parametru:
        - K: Typ počítaných prvků (klíče v Counteru, musí být hashable)
        - Hodnoty jsou implicitně typu int a reprezentují počet výskytů

    Validační proces:
        1. Ověří, zda hodnota je instance typu collections.Counter
        2. Pokud je požadována hloubková kontrola:
           a) Ověří, že všechny klíče odpovídají specifikovanému typu K
           b) Ověří, že všechny hodnoty jsou typu int

    Použití v kódu:
        - Pro parametry funkcí: def analyze_word_frequency(counts: Counter[str]) -> None
        - Pro návratové hodnoty: def count_elements(items: List[T]) -> Counter[T]
        - Pro typování proměnných: letter_counts: Counter[str] = Counter("hello world")

    Srovnání s podobnými typy:
        - Counter vs dict: Counter automaticky inicializuje nové klíče s hodnotou 0
        - Counter vs DefaultDict[K, int]: Counter nabízí dodatečné metody pro práci s četnostmi
          jako elements(), most_common(), subtract() a další
        - Counter vs Mapping[K, int]: Counter je konkrétní implementace tohoto obecného protokolu

    Běžné vzory použití:
        - Analýza frekvence slov: Counter(text.split())
        - Počítání prvků: Counter(seznam)
        - Kombinování četností: counter1 + counter2, counter1 - counter2
        - Získání nejčastějších prvků: counter.most_common(n)

    Běžné chyby:
        - Zapomenutí importu: from typing import Counter nebo from collections import Counter
        - Pokus o použití nehashable objektů jako klíčů (např. seznamů)
        - Záměna s běžným slovníkem v případech, kdy jsou potřeba speciální metody Counteru

    Reference:
        - https://docs.python.org/3/library/collections.html#collections.Counter
        - https://docs.python.org/3/library/typing.html#typing.Counter
        - https://peps.python.org/pep-0585/ (nativní generické typy)
    """

    VALIDATOR_KEY = "counter"
    ANNOTATION = Counter[K]
    INFO = "Definuje Counter – klíče libovolného typu K, hodnoty vždy int."
    ORIGIN = CounterOrigin

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Přetížení metody __call__ pro validaci slovníkových struktur."""

        # Navrácení výstupu funkce pro validaci slovníkových objektů upravené pro Counter
        return dictionary_validator_for_counter(
            value, self.ORIGIN, annotation, depth_check, custom_types, bool_only
        )
