from typing import ValuesView
from collections.abc import ValuesView as ValuesViewOrigin

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import V


class ValuesViewValidator(BaseIterableValidator):
    """
    Validátor pro zápis ValuesView[V]

    ValuesView reprezentuje pohled na hodnoty mapování,
    získaný pomocí metody dict.values() nebo podobné metody jiných mapování.

    Hint:
        ValuesView[V] = Pohled na hodnoty v mapování

    Reprezentuje pohled na hodnoty:
        ValuesView je druh MappingView, který poskytuje pohled na hodnoty z mapování.
        Na rozdíl od KeysView, neimplementuje rozhraní Set, protože hodnoty
        v mapování nemusí být unikátní.

    Základní operace:
        * Iterace přes hodnoty: for v in mapping.values()
        * Testování členství: value in mapping.values()
        * Zjištění délky: len(mapping.values())

    Specifické chování:
        * Neimplementuje set-like operace, protože hodnoty nemusí být unikátní
        * Podporuje pouze základní operace Collection (iterace, členství, délka)

    Příklady:
        dict_values a podobné objekty z ostatních implementací mapování

    Použití v typových anotacích:
        Používá se k označení, že funkce nebo proměnná očekává výsledek metody values()
        ze slovníku nebo jiného mapování.
    """

    VALIDATOR_KEY = "values_view"
    ANNOTATION = ValuesView[V]
    INFO = "Definuje pohled na hodnoty v mapování."
    GET_ORIGIN = ValuesViewOrigin