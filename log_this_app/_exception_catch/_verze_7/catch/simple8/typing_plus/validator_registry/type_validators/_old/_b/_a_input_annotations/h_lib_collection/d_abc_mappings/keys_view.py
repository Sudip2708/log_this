from typing import KeysView
from collections.abc import KeysView as KeysViewOrigin

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import K


class KeysViewValidator(BaseIterableValidator):
    """
    Validátor pro zápis KeysView[K]

    KeysView reprezentuje pohled na klíče mapování,
    získaný pomocí metody dict.keys() nebo podobné metody jiných mapování.

    Hint:
        KeysView[K] = Pohled na klíče v mapování

    Reprezentuje pohled na klíče:
        KeysView je druh MappingView, který poskytuje pohled na klíče z mapování.
        Implementuje rozhraní Set, takže podporuje operace jako průnik, sjednocení, atd.

    Základní operace:
        * Iterace přes klíče: for k in mapping.keys()
        * Testování členství: key in mapping.keys()
        * Zjištění délky: len(mapping.keys())

    Specifické chování:
        * Jelikož implementuje Set, podporuje množinové operace jako |, &, -, ^
        * Umožňuje rychlé porovnání s jinými množinami klíčů

    Příklady:
        dict_keys a podobné objekty z ostatních implementací mapování

    Použití v typových anotacích:
        Používá se k označení, že funkce nebo proměnná očekává výsledek metody keys()
        ze slovníku nebo jiného mapování.
    """

    VALIDATOR_KEY = "keys_view"
    ANNOTATION = KeysView[K]
    INFO = "Definuje pohled na klíče v mapování."
    GET_ORIGIN = KeysViewOrigin