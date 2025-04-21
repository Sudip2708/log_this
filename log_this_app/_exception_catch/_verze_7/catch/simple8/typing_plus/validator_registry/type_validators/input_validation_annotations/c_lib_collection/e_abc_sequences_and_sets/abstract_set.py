from typing import AbstractSet
from collections.abc import Set as SetOrigin

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class AbstractSetValidator(BaseIterableValidator):
    """
    Validátor pro zápis AbstractSet[T]

    Hint:
        AbstractSet[T] = Rozhraní pro množinové struktury
    """

    VALIDATOR_KEY = "abstractset"
    ANNOTATION = AbstractSet[T]
    INFO = "Definuje abstraktní rozhraní množiny"
    ORIGIN = SetOrigin
