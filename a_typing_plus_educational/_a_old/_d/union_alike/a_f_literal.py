from typing import Literal

from ._union_alike_base import UnionAlikeBase


class LiteralValidator(UnionAlikeBase):
    """
    Validátor pro zápis Literal["a", "b", "c"]

    Hint:
        Literal["a", "b", "c"] = Předdefinovaná množina hodnot
    """

    VALIDATOR_KEY = "literal"
    ANNOTATION = Literal["a", "b", "c"]
    INFO = "Definuje povolené hodnoty"
    GET_ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Získání tuple s vnitřními typy
        inner_args = self._get_all_args_as_tuple(annotation)

        # Validace hodnoty vůči vnitřnímu typu
        return self.validate_condition(value in inner_args)