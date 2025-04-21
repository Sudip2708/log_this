from typing import Any, get_args

from .._iterable_validator_base import IterableValidatorBase


class UnionAlikeBase(IterableValidatorBase):
    """
    Základní třídy pro seskupující generické anotace.
    """

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Získání tuple s vnitřními typi
        inner_args = self._get_all_args_as_tuple(annotation)

        # Pouze přeposílá dál, depth_check zůstává beze změny
        return self.validate_typing(
            value, inner_args, depth_check, custom_types, bool_only
        )

