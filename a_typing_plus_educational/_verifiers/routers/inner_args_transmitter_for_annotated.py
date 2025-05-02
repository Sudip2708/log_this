from typing import Any, Tuple, Union

from ..._exceptions import (
    VerifyError,
    InternalUnexpectedError
)
from ..typing_validator import validate_typing
from .._tools import get_args_safe


def inner_args_transmitter_for_annotated(
    value: Any,
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: dict = None,
    bool_only: bool = False
) -> bool:
    """Transmits filtered inner types for Annotated type validation.

    This function is specifically designed for handling Annotated types.
    It filters out any metadata (typically strings) from the annotation
    and re-validates the value against the core typing structure.

    Args:
        value (Any): The value to be validated.
        annotation (Any, optional): Annotated type containing the base type and metadata.
        depth_check (Union[bool, int], optional): Depth control for recursive validation.
        custom_types (Tuple[Any, ...], optional): Tuple of custom accepted types.
        bool_only (bool, optional): If True, function returns only a boolean without raising errors.

    Returns:
        bool: True if the value is valid according to the provided typing rules, otherwise False.

    Raises:
        VerifyError: If the value does not meet the expected typing constraints.
        InternalUnexpectedError: If an unexpected error occurs during validation.

    Example:
        >>> from typing import Annotated
        >>> inner_args_transmitter_for_annotated(5, Annotated[int, "This is metadata"])
        True

        >>> inner_args_transmitter_for_annotated(5, Annotated[str, "Info"])
        # Raises VerifyError
    """
    try:
        # Ověření a získání vnitřních typových anotací
        inner_args = get_args_safe(annotation)

        # Odstranění všech řetězcových metadat (informačních popisků)
        filtered_args = tuple(arg for arg in inner_args if not isinstance(arg, str))

        # Pokud zůstala jen jedna položka, předáváme ji přímo,
        # jinak předáváme celý tuple všech ověřitelných prvků
        prepared_annotation = filtered_args[0] if len(filtered_args) == 1 else filtered_args

        # Rekurzivní validace
        return validate_typing(value, prepared_annotation, depth_check, custom_types, bool_only)

    # Propagace všech již ošetřených výjimek
    except VerifyError:
        raise

    except Exception as e:
        raise InternalUnexpectedError(e) from e
