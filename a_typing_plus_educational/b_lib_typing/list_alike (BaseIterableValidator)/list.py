from typing import List

from ..._bases import BaseIterableValidator, T


class ListValidator(BaseIterableValidator):
    """
    Validátor pro typovou anotaci List[T]

    List reprezentuje seznam (kolekci) prvků stejného typu. Na rozdíl od množiny (Set)
    zachovává pořadí prvků a umožňuje duplicitní hodnoty.

    Syntaxe:
        - List[T]               # Preferovaný zápis (vyžaduje import z typing)
        - list[T]               # Od Python 3.9+
        - list                  # Obecný seznam bez specifikace typu prvků

    Příklady použití:
        - List[int]             # Seznam celých čísel
        - List[str]             # Seznam řetězců
        - List[Dict[str, int]]  # Seznam slovníků mapujících řetězce na celá čísla
        - List[Union[int, str]] # Seznam prvků, které jsou buď celá čísla nebo řetězce

    Vnitřní typy:
        Anotace List vyžaduje specifikaci typu vnitřních prvků T, kde T může být
        libovolný podporovaný typ včetně složených typů.

    Validační proces:
        1. Ověří, zda hodnota je instance typu list
        2. Pokud je požadována hloubková kontrola, ověří typy všech prvků seznamu
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_items(items: List[int]) -> None
        - Pro návratové hodnoty: def get_names() -> List[str]
        - Pro typování proměnných: names: List[str] = ["Alice", "Bob"]

    Kompatibilita:
        - List je kompatibilní s Sequence a Iterable
        - List není kompatibilní s Tuple (ten má pevnou délku)
        - List není kompatibilní s Set (ten nemá duplicity)

    Běžné chyby:
        - Zapomenutí importu: from typing import List
        - Použití tuple místo List pro proměnnou délku sekvence
        - Míchání různých typů v seznamu, kde je očekáván jeden typ

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.List
        - https://peps.python.org/pep-0585/ (nativní generické typy)
    """

    VALIDATOR_KEY = "list"
    ANNOTATION = List[T], list[T], list
    INFO = "Definuje seznam položek"
    ORIGIN = list
