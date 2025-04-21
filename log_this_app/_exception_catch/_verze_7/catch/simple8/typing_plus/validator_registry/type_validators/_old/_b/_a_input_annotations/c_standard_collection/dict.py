from typing import Dict

from .._base_mapping_validator import BaseMappingValidator
from .._base_type_variables import K, V


class DictValidator(BaseMappingValidator):
    """
    Validátor pro zápis Dict[K, V]

    Hint:
        Dict[K, V] = Slovník s klíči typu K a hodnotami typu V
    """

    VALIDATOR_KEY = "dict"
    ANNOTATION = Dict[K, V], dict[K, V], dict
    INFO = "Definuje slovník"
    GET_ORIGIN = dict
