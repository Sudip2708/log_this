from typing import Any, Tuple, Union

from .base_validator import BaseValidator
from ..a_validators import has_attribute_validator


class HasAttributeValidatorBase(BaseValidator):
    """
    Základní třída pro validační třídy, které provádějí validaci na základě atributu.
    """

    def __call__(
        self,
        value: Any,
        annotation: Any,
        inner_check: Union[bool, int],
        custom_types: dict = None,
        bool_only: bool
    ) -> Union[bool, Any]:

        return has_attribute_validator(
            value, self.ORIGIN, self.ANNOTATION, bool_only
        )
