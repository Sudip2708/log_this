from typing import Optional, Type

from ._exceptions import SafeVerifyError, VerifyError
from ._get_error_message import _get_error_message
from ._verify_exception_type import _verify_exception_type


def verify_bool(
        condition: bool,
        message: Optional[str] = None,
        exception_type: Type[Exception] = VerifyError
) -> bool:
    """
    Ověření boolean podmínky.

    Args:
        condition (bool): Boolean hodnota k ověření.
        message (Optional[str], optional): Volitelná uživatelská chybová zpráva.
        exception_type (Type[Exception], optional): Typ výjimky pro selhání. Defaults to VerifyError.

    Returns:
        bool: True, pokud je boolean splněn.

    Raises:
        SafeVerifyError: Při vnitřní chybě ověřování.
        exception_type: Při nesplnění boolean podmínky.
    """
    try:
        if condition is True:
            return True

        _verify_exception_type(exception_type)
        raise exception_type(_get_error_message(message))

    except TypeError as e:
        raise SafeVerifyError(f"Neplatný typ boolean hodnoty: {str(e)}")
    except Exception as e:
        raise SafeVerifyError(
            f"Neočekávaná chyba funkce verify_bool. "
            f"{e.__class__.__name__}: {str(e)}"
        )
