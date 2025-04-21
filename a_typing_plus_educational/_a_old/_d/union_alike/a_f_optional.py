from typing import Any, Optional, Union

from ._union_alike_base import UnionAlikeBase

T = T1 = T2 = Any


class OptionalValidator(UnionAlikeBase):
    """
    Validátor pro zápis Optional[T]

    Optional[T] je jen zkrácená forma zápisu Union[T, None]
    a pro obě shodně metoda get_origin vrací Union,
    takže jsou obě zpracovávané pře Union.

    Hint:
        Optional[T] = Zkrácený zápis Union[X, None]
    """

    VALIDATOR_KEY = "optional"
    ANNOTATION = Optional[T]
    INFO = "Definuje, že hodnota musí odpovídat alespoň jedné vnitřní definici, nebo mít hodnotu None."
    GET_ORIGIN = Union