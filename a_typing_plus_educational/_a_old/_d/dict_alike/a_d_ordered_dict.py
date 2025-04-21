# validators/collections/ordered_dict_validator.py

from typing import Any, OrderedDict
from collections import OrderedDict as OrderedDictOrigin

from ._dict_alike_base import DictAlikeBase

K = V = Any

class OrderedDictValidator(DictAlikeBase):
    """
    Validátor pro zápis collections.OrderedDict[K, V]

    Přebírá logiku validace slovníku – validuje klíče a hodnoty.

    OrderedDict reprezentuje slovník, který si pamatuje pořadí vkládaných položek.
    Chová se jako běžný dict, ale při iteraci zachovává pořadí.

    Hint:
        OrderedDict[K, V] = Slovník, který si pamatuje pořadí vložených prvků.
    """

    VALIDATOR_KEY = "ordereddict"
    ANNOTATION = OrderedDict[K, V]
    INFO = "Definuje slovník typu OrderedDict s typovanými klíči a hodnotami."
    GET_ORIGIN = OrderedDictOrigin  # collections.OrderedDict
