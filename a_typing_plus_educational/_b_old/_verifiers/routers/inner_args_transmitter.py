from typing import Any, Tuple, Union

from ..._exceptions import (
    VerifyError,
    VerifyUnexpectedInternalError
)
from ..typing_validator import validate_typing
from .._tools import get_args_safe


def inner_args_transmitter(
    value: Any,
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: dict = None,
    bool_only: bool = False
) -> bool:
    """Transmits inner type arguments for recursive type validation.

    This function retrieves the inner types from the given annotation
    and re-validates the value against them by calling `validate_typing`.
    It acts mainly as a relay and does not perform validation logic itself.

    Args:
        value (Any): The value to be validated.
        annotation (Any, optional): Type annotation which may contain inner types.
        depth_check (Union[bool, int], optional): Depth control for recursive validation.
        custom_types (dict): Dict of custom accepted types.
        bool_only (bool, optional): If True, function returns only a boolean without raising errors.

    Returns:
        bool: True if the value is valid according to the provided typing rules, otherwise False.

    Raises:
        VerifyError: If the value does not meet the expected typing constraints.
        VerifyUnexpectedInternalError: If an unexpected error occurs during validation.

    Example:
        >>> inner_args_transmitter(5, Union[int, str])
        True

        >>> inner_args_transmitter(5, Union[str, float])
        # Raises VerifyError
    """
    try:
        # Ověření a získání vnitřních typových anotací
        inner_args = get_args_safe(annotation)

        # Rekurzivní validace
        return validate_typing(value, inner_args, depth_check, custom_types, bool_only)

    # Propagace všech již ošetřených výjimek
    except VerifyError:
        raise

    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e
