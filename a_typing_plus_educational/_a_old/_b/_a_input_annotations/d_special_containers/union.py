from typing import Union

from .._base_union_validator import BaseUnionValidator
from .._base_type_variables import T1, T2


class UnionValidator(BaseUnionValidator):
    """
    Validátor pro zápis Union[T1,T2,...]

    Hint:
        Union[T1,T2,...] = Více typů současně
    """

    VALIDATOR_KEY = "union"
    ANNOTATION = Union[T1,T2,...]
    INFO = "Definuje, že hodnota musí odpovídat alespoň jedné vnitřní definici."
    GET_ORIGIN = Union

