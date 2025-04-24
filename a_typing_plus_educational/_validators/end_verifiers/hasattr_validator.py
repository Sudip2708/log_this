from typing import Any, Tuple, Union, Optional

from ..._exceptions import (
    HasAttributeValueError,
    HasAttributeExpectedError,
    InternalUnexpectedError,
)


def has_attribute_validator(
    value: Any,
    expected: Optional[str, Tuple[str, ...]],
    annotation: str,
    bool_only: bool = False
) -> bool:

    try:

        # Pokud hodnota odpovídá očekávanému typu, vrať True
        if all(hasattr(value, attr) for attr in expected):
            return True

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak načti chybějící atributy a vyhoď výjimku pro nevalidní hodnotu
        missing = [attr for attr in expected if not hasattr(value, attr)]
        raise HasAttributeValueError(value, annotation, missing)

    # Přeposlání vnitřní výjimky
    except HasAttributeValueError:
        raise

    # Ošetření špatného zadání parametru `expected`
    except TypeError as e:
        raise HasAttributeExpectedError(expected) from e

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise InternalUnexpectedError(e) from e




