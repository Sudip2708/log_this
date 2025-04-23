from typing import ValuesView
from collections.abc import ValuesView as ValuesViewOrigin

from ..._bases import BaseIterableValidator, V


class ValuesViewValidator(BaseIterableValidator):
    """
    Validátor pro typovou anotaci ValuesView[V]

    ValuesView reprezentuje pohled (view) na hodnoty mapování, například slovníku.
    Jde o lehkou sekvenci podobnou objektu, který neprovádí kopírování dat, ale poskytuje
    přístup k hodnotám původního mapování. Změny v původním mapování se projeví i v pohledu.

    Syntaxe:
        - ValuesView[V]           # Vyžaduje import z typing
        - collections.abc.ValuesView[V]  # Od Python 3.9+

    Příklady použití:
        - ValuesView[int]         # Pohled na celočíselné hodnoty ve slovníku
        - ValuesView[str]         # Pohled na řetězcové hodnoty ve slovníku
        - ValuesView[Any]         # Pohled na libovolné hodnoty ve slovníku

    Vnitřní typy:
        ValuesView parametrizujeme typem V, který specifikuje typ hodnot v mapování.
        V může být libovolný validní typ.

    Validační proces:
        1. Ověření, zda hodnota je instance collections.abc.ValuesView
        2. Při hloubkové kontrole ověření typů všech hodnot v pohledu
        3. Rekurzivní validace vnořených typů podle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def sum_values(values: ValuesView[int]) -> int
        - Pro návratové hodnoty: def get_values() -> ValuesView[str]
        - Praktické použití: values: ValuesView[int] = my_dict.values()

    Vztah k jiným typům:
        - ValuesView je podtypem Collection, Iterable a Container
        - Podobný KeysView (pohled na klíče) a ItemsView (pohled na páry klíč-hodnota)
        - Na rozdíl od listu a jiných kontejnerů, pohled odráží změny v původním mapování

    Běžné chyby:
        - Předpokládání, že ValuesView je nezávislá kopie hodnot (jde pouze o pohled)
        - Pokus o modifikaci pohledu (ValuesView je neměnný)
        - Zapomenutí, že pohled ztrácí validitu, pokud se původní mapování změní

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.ValuesView
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.ValuesView
        - https://peps.python.org/pep-0585/ (nativní generické typy)
    """

    VALIDATOR_KEY = "values_view"
    ANNOTATION = ValuesView[V]
    INFO = "Definuje pohled na hodnoty v mapování."
    ORIGIN = ValuesViewOrigin