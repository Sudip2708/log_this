from typing import Any

from ..._exceptions_base import VerifyUnexpectedInternalError
from .._exceptions import (
    VerifyAttributeNotFoundError,
    VerifyAttributeNotStrError,
    VerifyAttributeAccessError,
)


def has_attr_verifier(
    obj: Any,
    attribute_name: str,
    bool_only: bool = False
) -> bool:

    # Kontrola zda je jméno atributu zadán jako str
    if not isinstance(attribute_name, str):
        raise VerifyAttributeNotStrError(attribute_name)

    try:

        # Pokud hodnota odpovídá očekávanému typu, vrať True
        if hasattr(obj, attribute_name):
            return True

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak vyhoď výjimku pro nevalidní hodnotu
        raise VerifyAttributeNotFoundError(obj, attribute_name)

    # Přeposlání vnitřní výjimky
    except VerifyAttributeNotFoundError:
        raise

    # Výjimka vyvolaná při chybě přístupu k atributu objektu
    except TypeError as e:
        raise VerifyAttributeAccessError(obj, attribute_name, str(e)) from e

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e
