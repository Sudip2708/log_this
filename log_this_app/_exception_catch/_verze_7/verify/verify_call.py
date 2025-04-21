from typing import Callable, Optional, Type

from ._exceptions import SafeVerifyError, VerifyError
from ._get_error_message import _get_error_message
from ._verify_exception_type import _verify_exception_type


def verify_call(
        condition: Callable[[], bool],
        message: Optional[str] = None,
        exception_type: Type[Exception] = VerifyError
) -> bool:
    """
    Ověření callable (volatelné) podmínky.

    Args:
        condition (Callable[[], bool]): Callable výraz vracející boolean.
        message (Optional[str], optional): Volitelná uživatelská chybová zpráva.
        exception_type (Type[Exception], optional): Typ výjimky pro selhání. Defaults to VerifyError.

    Returns:
        bool: True, pokud je callable splněno.

    Raises:
        SafeVerifyError: Při vnitřní chybě volání.
        exception_type: Při nesplnění callable podmínky.
    """
    try:
        # Zachycení potenciálních chyb při volání funkce
        try:
            result = condition()
        except Exception as e:
            raise SafeVerifyError(
                f"Chyba při volání ověřovací funkce uvnitř verify_call. "
                f"{e.__class__.__name__}: {str(e)}"
            )

        # Kontrola výsledku volání
        if result is True:
            return True

        _verify_exception_type(exception_type)
        raise exception_type(_get_error_message(message))

    except TypeError as e:
        raise SafeVerifyError(f"Neplatný typ při ověřování callable: {str(e)}")
    except Exception as e:
        raise SafeVerifyError(
            f"Neočekávaná chyba funkce verify_call. "
            f"{e.__class__.__name__}: {str(e)}"
        )