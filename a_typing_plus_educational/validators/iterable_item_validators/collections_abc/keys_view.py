from typing import KeysView
from collections.abc import KeysView as KeysViewOrigin

from ..._bases3 import BaseIterableValidator, K


class KeysViewValidator(BaseIterableValidator):
    """
    Validátor pro typovou anotaci KeysView[K]

    KeysView reprezentuje pohled (view) na klíče mapování, jako je slovník.
    Jde o dynamický, neměnitelný objekt podobný množině, který poskytuje přístup
    ke klíčům původního mapování bez kopírování dat. Jakékoliv změny v původním
    mapování se automaticky projeví i v pohledu.

    Syntaxe:
        - KeysView[K]            # Vyžaduje import z typing
        - collections.abc.KeysView[K]  # Od Python 3.9+

    Příklady použití:
        - KeysView[str]          # Pohled na řetězcové klíče ve slovníku
        - KeysView[int]          # Pohled na celočíselné klíče ve slovníku
        - KeysView[Hashable]     # Pohled na libovolné hashovatelné klíče

    Vnitřní typy:
        KeysView parametrizujeme typem K, který specifikuje typ klíčů v mapování.
        K musí být hashovatelný typ (implementující __hash__).

    Validační proces:
        1. Ověření, zda hodnota je instance collections.abc.KeysView
        2. Při hloubkové kontrole ověření typů všech klíčů v pohledu
        3. Rekurzivní validace vnořených typů podle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_keys(keys: KeysView[str]) -> None
        - Pro návratové hodnoty: def get_keys() -> KeysView[int]
        - Praktické použití: keys: KeysView[str] = my_dict.keys()

    Vztah k jiným typům:
        - KeysView implementuje rozhraní Set, Collection, Iterable a Container
        - Podobný ValuesView (pohled na hodnoty) a ItemsView (pohled na páry klíč-hodnota)
        - Na rozdíl od množiny (set), podporuje operace jako průnik či sjednocení s jinými množinami
        - Obsahuje jen hashovatelné prvky

    Běžné chyby:
        - Předpokládání, že KeysView je nezávislá kopie klíčů (jde pouze o pohled)
        - Pokus o přímou modifikaci pohledu (KeysView je neměnný)
        - Zapomenutí, že pohled ztrácí validitu, pokud se původní mapování změní
        - Použití operací jako discard() nebo add(), které nejsou podporovány

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.KeysView
        - https://docs.python.org/3/library/collections.abc.html#collections.abc.KeysView
        - https://peps.python.org/pep-0585/ (nativní generické typy)
    """

    VALIDATOR_KEY = "keys_view"
    ANNOTATION = KeysView[K]

    IS_INSTANCE = KeysViewOrigin
    HAS_ATTRS = "mapping", "__iter__", "__len__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Pohled na klíče ve slovníku"
    LONG_DESCRIPTION = (
            "Validuje, že objekt odpovídá typu KeysView, "
            "který reprezentuje dynamický pohled na klíče slovníku, "
            "s podporou množinových operací."
        )
