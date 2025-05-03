from typing import Deque
from collections import deque

from ...._bases import BaseIterableItemValidator, T


class DequeValidator(BaseIterableItemValidator):
    """
    Validátor pro typovou anotaci Deque[T]

    Deque reprezentuje oboustrannou frontu (double-ended queue), která umožňuje efektivní
    přidávání a odebírání prvků z obou konců kolekce. Jde o optimalizovanou datovou strukturu
    pro operace na začátku a konci sekvence.

    Syntaxe:
        - Deque[T]           # Preferovaný zápis (vyžaduje import z typing)
        - collections.deque  # Konkrétní implementace z modulu collections

    Příklady použití:
        - Deque[int]         # Oboustranná fronta celých čísel
        - Deque[str]         # Oboustranná fronta řetězců
        - Deque[Dict[str, Any]]  # Oboustranná fronta slovníků

    Vnitřní typy:
        Deque vyžaduje specifikaci typu T pro své prvky, kde T může být
        libovolný podporovaný typ.

    Validační proces:
        1. Ověří, zda hodnota je instance třídy collections.deque
        2. Pokud je požadována hloubková kontrola, ověří typy všech prvků v deque
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_queue(queue: Deque[str]) -> None
        - Pro návratové hodnoty: def get_history() -> Deque[int]
        - Pro typové anotace proměnných: history: Deque[str] = deque(["a", "b", "c"], maxlen=10)

    Specifické vlastnosti:
        - Volitelný parametr maxlen pro omezení maximální velikosti
        - O(1) operace pro append a pop na obou koncích (na rozdíl od list, kde je O(n) na začátku)
        - Podpora indexování, ale pomalejší než u seznamu
        - Implementuje rozhraní Sequence a tedy podporuje všechny operace jako list

    Běžné operace:
        - append() / appendleft() - Přidání prvku na konec/začátek
        - pop() / popleft() - Odebrání prvku z konce/začátku
        - rotate() - Rotace prvků v deque
        - extend() / extendleft() - Rozšíření o multiple prvků

    Kompatibilita:
        - Deque implementuje MutableSequence rozhraní
        - Je součástí standardní knihovny collections

    Kdy použít:
        - Pro FIFO (First-In-First-Out) nebo LIFO (Last-In-First-Out) fronty
        - Pro implementaci vyrovnávacích pamětí (bufferů)
        - Pro udržování historie posledních N položek (pomocí maxlen)
        - Pro implementaci algoritmů vyžadujících efektivní operace na obou koncích

    Běžné chyby:
        - Záměna s obyčejným seznamem, kde začáteční operace nejsou efektivní
        - Nepochopení chování maxlen parametru (při překročení se automaticky zahazují staré hodnoty)
        - Zapomenutí importu: from collections import deque, from typing import Deque

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Deque
        - https://docs.python.org/3/library/collections.html#collections.deque
    """

    VALIDATOR_KEY = "deque"
    ANNOTATION = Deque[T]

    IS_INSTANCE = deque
    DUCK_TYPING = {
        "has_attr": (
            "__iter__", "__len__",
            "append", "appendleft", "pop", "popleft"
        ),
    }

    DESCRIPTION = "Obousměrná fronta"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí collections.deque, "
            "tedy fronty s rychlým přístupem z obou stran."
        )
