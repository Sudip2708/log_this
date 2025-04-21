from typing import Any, MutableMapping
from collections.abc import MutableMapping as MutableMappingOrigin

from ._dict_alike_base import DictAlikeBase

K = V = Any

class MutableMappingValidator(DictAlikeBase):
    """
    Validátor pro zápis MutableMapping[K, V]

    Přebírá logiku validace slovníku – validuje klíče a hodnoty.

    MutableMapping reprezentuje jakékoli měnitelné mapování (dict, defaultdict, atd.),
    které podporuje přidávání a odebírání klíčů.

    MutableMapping reprezentuje mapovací strukturu, která podporuje jak čtení,
    tak zápis dat, včetně metod jako keys(), items(), __setitem__(), atd.
    Typickým příkladem je klasický dict.

    Hint:
        MutableMapping[K, V] = Měnitelný slovník.
    """

    VALIDATOR_KEY = "mutablemapping"
    ANNOTATION = MutableMapping[K, V]
    INFO = "Definuje mapovací strukturu typu MutableMapping s typovanými klíči a hodnotami."
    GET_ORIGIN = MutableMappingOrigin  # collections.abc.MutableMapping
