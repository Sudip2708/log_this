from typing import Any, Tuple, Union

from ._base_verifier import BaseVerifier


class BaseCustomLogicValidator(BaseVerifier):
    """
    Základní třída pro validační třídy, které definují vlastní validační logiku
    """

    def __call__(
        self,
        value: Any,
        annotation: Any,
        inner_check: Union[bool, int],
        custom_types: dict = None,
        bool_only: bool
    ) -> Union[bool, Any]:
        pass
