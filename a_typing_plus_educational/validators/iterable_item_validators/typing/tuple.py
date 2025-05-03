from typing import Tuple

from ...._bases import BaseIterableItemValidator,  T
from ...._verifiers import iterable_item_verifier_for_tuple


class TupleValidator(BaseIterableItemValidator):
    """
        Validátor pro typovou anotaci Tuple[T1, T2, ...] a Tuple[T, ...]

        Tuple reprezentuje neměnnou (immutable) sekvenci prvků, které mohou mít různé typy.
        Na rozdíl od seznamu (List) nelze po vytvoření měnit obsah n-tice a lze specifikovat
        přesné typy pro každou pozici. Existují dva základní způsoby anotace:
          1. Homogenní n-tice s variabilní délkou: Tuple[T, ...] - všechny prvky stejného typu
          2. Heterogenní n-tice s pevnou délkou: Tuple[T1, T2, T3] - různé typy na specifických pozicích

        Syntaxe:
            - Tuple[T1, T2, T3]    # Heterogenní n-tice (vyžaduje import z typing)
            - Tuple[T, ...]        # Homogenní n-tice s variabilní délkou
            - tuple[T1, T2, T3]    # Od Python 3.9+
            - tuple[T, ...]        # Od Python 3.9+
            - tuple                # Obecná n-tice bez specifikace typu prvků

        Příklady použití:
            - Tuple[int, str, bool]   # Trojice: celé číslo, řetězec, boolean
            - Tuple[int, ...]         # N-tice celých čísel libovolné délky
            - Tuple[str, int]         # Dvojice: řetězec a celé číslo
            - Tuple[Dict[str, Any], List[int]]  # Dvojice: slovník a seznam čísel

        Vnitřní typy:
            - Heterogenní n-tice: každá pozice může mít jiný typ
            - Homogenní n-tice: všechny prvky mají stejný typ, ale počet je variabilní

        Validační proces:
            1. Ověří, zda hodnota je instance typu tuple
            2. Rozpozná, zda jde o homogenní (variabilní) nebo heterogenní (fixní) n-tici
            3. Pro fixní n-tice ověří správný počet prvků a typ každé pozice
            4. Pro variabilní n-tice ověří stejný typ u všech prvků
            5. Rekurzivně validuje vnořené typy dle specifikace v depth_check

        Použití v kódu:
            - Pro parametry funkcí: def process_coordinates(point: Tuple[float, float]) -> None
            - Pro návratové hodnoty: def get_user_info() -> Tuple[str, int, bool]
            - Pro typování proměnných: position: Tuple[int, int, int] = (10, 20, 30)
            - Pro variabilní data: values: Tuple[int, ...] = (1, 2, 3, 4, 5)

        Kompatibilita:
            - Tuple je kompatibilní s Sequence a Iterable
            - Tuple není kompatibilní s List (ten je měnitelný)
            - Tuple může být použit jako klíč ve slovníku (Dict)
            - Tuple může být prvkem v množině (Set nebo FrozenSet)

        Výhody oproti List:
            - Může být použit jako klíč ve slovníku
            - Může být prvkem v množině
            - Jasně specifikuje počet a typy prvků (v případě heterogenní n-tice)
            - Garantuje neměnnost obsahu

        Běžné chyby:
            - Zapomenutí importu: from typing import Tuple
            - Záměna Tuple[T] (chybný zápis) a Tuple[T, ...] (správný zápis pro variabilní n-tici)
            - Použití nesprávné délky n-tice oproti definované anotaci
            - Zaměnění pořadí typů v heterogenní n-tici

        Reference:
            - https://docs.python.org/3/library/typing.html#typing.Tuple
            - https://mypy.readthedocs.io/en/stable/tuple_types.html
            - https://peps.python.org/pep-0585/ (nativní generické typy)
        """

    VALIDATOR_KEY = "tuple"
    ANNOTATION = Tuple[T, ...]

    IS_INSTANCE = tuple
    DUCK_TYPING = {
        "has_attr": ("__getitem__", "__iter__", "__len__"),
    }

    DESCRIPTION = "Vestavěná n-tice"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je typu tuple. Jedná se o neměnnou sekvenci prvků, "
            "které mohou být libovolného typu a mají pevnou délku po vytvoření."
        )


    def __call__(self, value, annotation, depth_check, custom_types, bool_only):

        return iterable_item_verifier_for_tuple(
            value, annotation, depth_check, custom_types, bool_only
        )