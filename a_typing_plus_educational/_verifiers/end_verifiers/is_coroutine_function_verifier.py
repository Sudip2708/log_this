from typing import Any, Tuple, Union, Optional
from inspect import iscoroutinefunction

from ..._exceptions import (
    IsCoroutineFunctionValueError,
    InternalUnexpectedError,
)
from .._tools import get_attr_safe


def is_coroutine_function_verifier(
    value: Any,
    expected: Optional[str, Tuple[str, ...]],
    annotation: Any,
    bool_only: bool = False
) -> bool:

    try:

        attributes = get_attr_safe(value, expected, annotation)

        # Pokud hodnota odpovídá očekávanému typu, vrať True
        if all(iscoroutinefunction(attr) for attr in attributes):
            return True

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak vyhoď výjimku pro nevalidní hodnotu
        raise IsCoroutineFunctionValueError(attributes)

    # Přeposlání vnitřní výjimky
    except IsCoroutineFunctionValueError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise InternalUnexpectedError(e) from e




