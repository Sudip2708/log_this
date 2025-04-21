from typing import List, Any

from ._list_alike_base import ListAlikeBase

T = Any

class ListValidator(ListAlikeBase):
    """
    Validátor pro zápis List[T]

    Hint:
        List[T] = Seznam položek
    """

    VALIDATOR_KEY = "list"
    ANNOTATION = List[T]
    INFO = "Definuje seznam položek"
    GET_ORIGIN = list
