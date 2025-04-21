from typing import OrderedDict
from collections import OrderedDict as OrderedDictOrigin

from .._base_mapping_validator import BaseMappingValidator
from .._base_type_variables import K, V


class OrderedDictValidator(BaseMappingValidator):
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
    ORIGIN = OrderedDictOrigin
