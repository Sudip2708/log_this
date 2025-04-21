from typing import List

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class ListValidator(BaseIterableValidator):
    """
    Validátor pro zápis List[T]

    Hint:
        List[T] = Seznam položek
    """

    VALIDATOR_KEY = "list"
    ANNOTATION = List[T]
    INFO = "Definuje seznam položek"
    GET_ORIGIN = list
