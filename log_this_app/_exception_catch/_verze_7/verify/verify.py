from typing import Callable, Optional, Type, Union

from ._exceptions import SafeVerifyError, VerifyError
from .verify_bool import verify_bool
from .verify_call import verify_call


def verify(
        condition: Union[bool, Callable[[], bool]],
        message: Optional[str] = None,
        exception_type: Type[Exception] = VerifyError
) -> bool:
    """
    Hlavní ověřovací funkce pro flexibilní kontrolu podmínek.

    Args:
        condition (Union[bool, Callable[[], bool]]): Podmínka k ověření.
        message (Optional[str], optional): Volitelná uživatelská chybová zpráva.
        exception_type (Type[Exception], optional): Typ výjimky pro selhání. Defaults to VerifyError.

    Returns:
        bool: True, pokud je podmínka splněna.

    Raises:
        SafeVerifyError: Při jakékoli vnitřní chybě během ověřování.
        exception_type: Při nesplnění zadané podmínky.
    """
    try:
        if callable(condition):
            return verify_call(condition, message, exception_type)
        return verify_bool(condition, message, exception_type)

    except (TypeError, ValueError) as e:
        raise SafeVerifyError(
            f"Neplatný typ nebo hodnota při ověřování: {str(e)}")
    except Exception as e:
        raise SafeVerifyError(
            f"Neočekávaná chyba funkce verify. "
            f"{e.__class__.__name__}: {str(e)}"
        )
