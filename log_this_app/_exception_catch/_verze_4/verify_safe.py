import inspect
from typing import Callable, Optional, Type, Union


class SafeVerifyError(Exception):
    """Interní výjimka pro bezpečné ověřování."""
    pass


def safe_verify(
        condition: Union[bool, Callable[[], bool]],
        message: Optional[str] = None,
        exception_type: Type[Exception] = SafeVerifyError
) -> bool:
    """
    Bezpečná interní metoda pro ověřování vstupů.

    :param condition: Podmínka k ověření (boolean nebo callable)
    :param message: Volitelná chybová zpráva
    :param exception_type: Typ výjimky (default SafeVerifyError)
    :return: True pokud je podmínka splněna
    :raises: Specifikovaná výjimka při selhání
    """
    try:
        # Pokud je condition callable, vyvolej ji
        check = condition() if callable(condition) else condition

        # Automatická tvorba zprávy
        if message is None:
            frame = inspect.currentframe().f_back
            caller_info = inspect.getframeinfo(frame)
            message = (
                f"Ověření selhalo v metodě {caller_info.function} "
                f"v souboru {caller_info.filename}:{caller_info.lineno}"
            )

        # Kontrola podmínky
        if not check:
            raise exception_type(message)

        return True

    except Exception as e:
        # Zachycení jakékoliv vnitřní chyby při ověřování
        raise SafeVerifyError(f"Chyba při ověřování: {str(e)}")