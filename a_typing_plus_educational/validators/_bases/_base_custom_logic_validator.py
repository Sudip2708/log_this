from typing import Any, Tuple, Union

from .base_validator import BaseValidator


class BaseCustomLogicValidator(BaseValidator):
    """
    Základní třída pro validační třídy, které definují vlastní validační logiku
    """

    def __call__(
            self,
            value: Any,
            annotation: Any,
            custom_types: Optional[dict] = None,
            inner_check: Union[bool, int] = True,
            duck_typing: bool = False,
            bool_only: bool = False
    ) -> Union[bool, Any]:
        pass
