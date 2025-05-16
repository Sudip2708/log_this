from typing import Any, Tuple, Union
from collections.abc import Iterable

from ..end_verifiers import is_instance_verifier
from ..typing_validator import validate_typing
from .._tools import reduce_depth_check, get_args_safe
from ..._exceptions import (
    VerifyError,
    VerifyUnexpectedInternalError
)


def base_verifier(
    value: Any,
    expected: Union[type, Tuple[type, ...]],
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: dict = None,
    bool_only: bool = False
) -> bool:
    """
    Základní validátor, první úrovně.
    """

    try:

        # Kontrola zda je zadaná požadavek na duck typing kontrolu
        if duck_typing:


        # Validace základního typu (např. list, set)
        is_instance_verifier(value, expected)


        # Pokud vše projde navrácení úspěšné validace
        return True

    # Propagace všech již ošetřených výjimek
    except VerifyError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e
)