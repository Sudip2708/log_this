from typing import Any, Mapping
from collections.abc import Mapping as MappingOrigin

from ._dict_alike_base import DictAlikeBase

K = V = Any

class MappingValidator(DictAlikeBase):
    """
    Validátor pro zápis Mapping[K, V]

    Přebírá logiku validace slovníku – validuje klíče a hodnoty.

    Mapping reprezentuje jakékoli mapování (dict, defaultdict, OrderedDict, atd.),
    které podporuje přístup ke klíčům a metodám jako keys(), items(), atd.

    Hint:
        Mapping[K, V] = Neměnný slovník nebo čitelná mapovací struktura.
    """

    VALIDATOR_KEY = "mapping"
    ANNOTATION = Mapping[K, V]
    INFO = "Definuje mapovací strukturu typu Mapping s typovanými klíči a hodnotami."
    GET_ORIGIN = MappingOrigin  # collections.abc.Mapping
