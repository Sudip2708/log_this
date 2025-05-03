from typing import NamedTuple
from collections import namedtuple

from ...._bases import BaseIterableKeyValueValidator
from ...._verifiers import iterable_key_value_verifier_for_namedtuple


class NamedTupleValidator(BaseIterableKeyValueValidator):
    """
    Validátor pro typovou anotaci NamedTuple

    NamedTuple reprezentuje n-tici s pojmenovanými položkami, která kombinuje výhody
    tuples (immutabilita, rychlost) a objektů (přístup k prvkům pomocí jmen). Je to
    efektivní způsob, jak definovat jednoduché imutabilní datové třídy s typovou kontrolou.

    Syntaxe:
        - Deklarace pomocí dědičnosti (moderní zápis):
          class Point(NamedTuple):
              x: int
              y: int
              label: str = ""  # s výchozí hodnotou

        - Deklarace pomocí funkčního zápisu (starší způsob):
          Point = namedtuple('Point', ['x', 'y', 'label'], defaults=[""])

    Příklady použití:
        - class Person(NamedTuple):
              name: str
              age: int
              email: Optional[str] = None

        - # Použití jako typová anotace
          def process_point(point: Point) -> float: ...

        - # Vytvoření instance
          user = Person(name="Alice", age=30)
          print(user.name)  # přístup pomocí atributu
          print(user[0])    # přístup pomocí indexu

    Validační proces:
        1. Ověří, zda hodnota je instance namedtuple
        2. Pokud je požadována hloubková kontrola, získá typové anotace z třídy
        3. Pro každé pole ověří:
           - zda hodnota pole odpovídá očekávanému typu
        4. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def plot(point: Point) -> None
        - Pro návratové hodnoty: def get_user() -> Person
        - Pro typování proměnných: coordinates: Point = Point(10, 20, "marker")

    Kompatibilita:
        - NamedTuple je na runtime úrovni běžnou n-ticí (tuple)
        - NamedTuple je podtřídou tuple, lze použít všechny operace pro tuple
        - NamedTuple instance jsou immutable (nelze měnit po vytvoření)
        - NamedTuple instance jsou hashable a lze je použít jako klíče ve slovníku

    Související typy:
        - Tuple: jednodušší n-tice bez pojmenovaných položek
        - TypedDict: podobný koncept pro slovníky místo n-tic
        - dataclasses: flexibilnější alternativa (může být mutable)
        - @attrs: komplexnější alternativa s více funkcemi

    Vlastnosti:
        - Immutabilita: hodnoty nelze měnit po vytvoření instance
        - Přístup k prvkům jak pomocí jmen (.name), tak indexů ([0])
        - Podpora pro výchozí hodnoty (od Python 3.7+)
        - Automatické generování metod __repr__, __eq__, __hash__
        - Přístup ke všem hodnotám jako k tuple pomocí metody _asdict()

    Běžné chyby:
        - Pokus o modifikaci hodnot v instanci NamedTuple (jsou immutable)
        - Záměna s dataclasses, které mohou být mutabilní
        - Nepředání všech povinných parametrů při vytváření instance
        - Záměna pořadí parametrů při vytváření instance

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.NamedTuple
        - https://docs.python.org/3/library/collections.html#collections.namedtuple
        - https://peps.python.org/pep-0484/ (typové anotace)
    """

    VALIDATOR_KEY = "namedtuple"
    ANNOTATION = NamedTuple  # Symbolický zápis, není konkrétní typ jako Tuple[int, str]

    IS_INSTANCE = namedtuple  # Nedá se použít na ověření typu - jedná se o funkci pro vytváření jednoduchých tříd podobných strukturám nebo záznamům - ověření typu je prováděno dle vlastní funkce _is_named_tuple()
    DUCK_TYPING = None

    DESCRIPTION = "Pojmenovaná n-tice"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je podtřídou NamedTuple z modulu typing nebo collections. "
            "Umožňuje přístup k položkám podle jména."
        )


    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Přetížení metody __call__ pro validaci slovníkových struktur."""

        # Navrácení výstupu funkce pro validaci slovníkových objektů upravené pro namedtuple
        return iterable_key_value_verifier_for_namedtuple(
            value, annotation, depth_check, custom_types, bool_only
        )