from typing import Any, Tuple, Union, Optional

from ..._exceptions import (
    HasHashableAttributeError,
    HasAttributeExpectedError,
    VerifyUnexpectedInternalError,
)


def has_attribute_validator_for_hashable(
    value: Any,
    annotation: str,
    bool_only: bool = False
) -> bool:

    try:

        # Pokud hodnota odpovídá očekávanému typu, vrať True
        if hasattr(value, "__hash__") and value.__hash__ is not None:
            return True

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak vyhoď výjimku pro nevalidní hodnotu
        raise HasHashableAttributeError(value, annotation)

    # Přeposlání vnitřní výjimky
    except HasHashableAttributeError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e




