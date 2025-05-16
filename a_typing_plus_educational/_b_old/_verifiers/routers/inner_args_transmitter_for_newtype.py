from typing import Any, Tuple, Union

from ..._exceptions import (
    VerifyError,
    VerifyUnexpectedInternalError
)
from ..typing_validator import validate_typing
from .._tools import get_supertype_safe


def inner_args_transmitter_for_newtype(
    value: Any,
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: dict = None,
    bool_only: bool = False
) -> bool:
    """Transmits inner type arguments for recursive type validation."""
    try:

        # Získání nadřazeného typu z NewType anotace
        supertype = get_supertype_safe(annotation)

        # Rekurzivní validace
        return validate_typing(value, supertype, depth_check, custom_types, bool_only)

    # Propagace všech již ošetřených výjimek
    except VerifyError:
        raise

    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e
