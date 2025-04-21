from typing import Any, Optional, Union

from ._union_alike_base import UnionAlikeBase

T = T1 = T2 = Any


class UnionValidator(UnionAlikeBase):
    """
    Validátor pro zápis Union[T1,T2,...]

    Hint:
        Union[T1,T2,...] = Více typů současně
    """

    VALIDATOR_KEY = "union"
    ANNOTATION = Union[T1,T2,...]
    INFO = "Definuje, že hodnota musí odpovídat alespoň jedné vnitřní definici."
    GET_ORIGIN = Union
