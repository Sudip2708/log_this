from typing import Mapping
from collections.abc import Mapping as MappingOrigin

from .._base_mapping_validator import BaseMappingValidator
from .._base_type_variables import K, V


class MappingValidator(BaseMappingValidator):
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
    ORIGIN = MappingOrigin
