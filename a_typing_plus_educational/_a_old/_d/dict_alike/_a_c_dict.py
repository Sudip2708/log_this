from typing import Dict, Any

from ._dict_alike_base import DictAlikeBase

K = V = Any

class DictValidator(DictAlikeBase):
    """
    Validátor pro zápis Dict[K, V]

    Z této třídy dědí logyku následující třídy:
        DefaultDict[K, V] -  jako dict, ale s výchozí hodnotou
        OrderedDict[K, V] -  slovník s garantovaným pořadím
        Mapping[K, V] -  read-only dictionary interface
        MutableMapping[K, V] -  mutable interface

    Hint:
        Dict[K, V] = Slovník s klíči typu K a hodnotami typu V
    """

    VALIDATOR_KEY = "dict"
    ANNOTATION = Dict[K, V]
    INFO = "Definuje slovník"
    GET_ORIGIN = dict
