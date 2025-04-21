from typing import AbstractSet, Any
from collections.abc import Set as SetOrigin

from ._set_alike_base import SetAlikeBase

T = Any


class AbstractSetValidator(SetAlikeBase):
    """
    Validátor pro zápis AbstractSet[T]

    Hint:
        AbstractSet[T] = Rozhraní pro množinové struktury
    """

    VALIDATOR_KEY = "abstractset"
    ANNOTATION = AbstractSet[T]
    INFO = "Definuje abstraktní rozhraní množiny"
    GET_ORIGIN = SetOrigin
