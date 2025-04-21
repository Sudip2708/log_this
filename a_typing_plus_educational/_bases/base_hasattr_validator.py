from typing import Any, Tuple, Union

from ._base_validator import BaseValidator
from .._validators import validate_has_attribute


class BaseHasAttrValidator(BaseValidator):
    """
    Základní třída pro validační třídy, které provádějí validaci na základě atributu.
    """

    validate_has_attribute = validate_has_attribute

    def __call__(
        self,
        value: Any,
        annotation: Any,
        inner_check: Union[bool, int],
        custom_types: Tuple[Any, ...],
        bool_only: bool
    ) -> Union[bool, Any]:

        return self.validate_has_attribute(
            value, self.ORIGIN, self.ANNOTATION, bool_only
        )
