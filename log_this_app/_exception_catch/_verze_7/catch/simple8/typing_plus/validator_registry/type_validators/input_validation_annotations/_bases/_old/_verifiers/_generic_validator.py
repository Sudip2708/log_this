from typing import get_args

from ._base_type_validator import BaseTypeValidator


class BaseGenericValidator(BaseTypeValidator):
    """
    Základní třídy pro seskupující generické anotace.
    """

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Získání tuple s vnitřními typi
        inner_args = get_args(annotation)

        # Pouze přeposílá dál, depth_check zůstává beze změny
        return self.validate_typing(
            value, inner_args, depth_check, custom_types, bool_only
        )

