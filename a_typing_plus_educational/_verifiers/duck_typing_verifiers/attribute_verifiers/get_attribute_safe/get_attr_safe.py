from typing import Any

from ..._exceptions_base import VerifyUnexpectedInternalError
from .._exceptions import (
    VerifyAttributeNotFoundError,
    VerifyAttributeNotStrError,
    VerifyAttributeAccessError,
)

_MISSING = object()  # Sentinel pro detekci nezadaného defaultu


def get_attr_safe(
        obj: Any,
        attribute_name: str,
        default: Any = _MISSING
) -> Any:

    # Kontrola zda je jméno atributu zadán jako str
    if not isinstance(attribute_name, str):
        raise VerifyAttributeNotStrError(attribute_name)

    try:

        return (
            getattr(obj, attribute_name)
            if default is _MISSING
            else getattr(obj, attribute_name, default)
        )

    # Výjimka vyvolaná při nenalezení atributu a nezadané defaultní návratové hodnotě
    except AttributeError as e:
        raise VerifyAttributeNotFoundError(obj, attribute_name) from e

    # Výjimka vyvolaná při chybě přístupu k atributu objektu
    except TypeError as e:
        raise VerifyAttributeAccessError(obj, attribute_name, str(e)) from e

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e

