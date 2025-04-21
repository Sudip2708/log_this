from typing import Callable, Optional, Type, Union
import inspect


class VerifyError(Exception):
    """Vlastní výjimka pro selhání ověření."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class SafeVerifyError(Exception):
    """Interní výjimka pro bezpečné ověřování."""
    pass


def verify(
        condition: Union[bool, Callable[[], bool]],
        message: Optional[str] = None,
        exception_type: Type[Exception] = VerifyError
) -> bool:
    """
    Bezpečná interní metoda pro ověřování vstupů.

    :param condition: Podmínka k ověření (boolean nebo callable)
    :param message: Volitelná chybová zpráva
    :param exception_type: Typ výjimky (default VerifyError)
    :return: True pokud je podmínka splněna
    :raises: Specifikovaná výjimka při selhání
    """

    try:

        # Pokud je splněna podmínka vrať True
        if condition() if callable(condition) else condition:
            return True

        # Automatická tvorba zprávy pokud není poskytnuta
        if message is None:

            # Zjištění kontextu volání
            frame = inspect.currentframe().f_back
            caller_info = inspect.getframeinfo(frame)

            message = (
                f"Ověření selhalo v metodě {caller_info.function} "
                f"v souboru {caller_info.filename}:{caller_info.lineno}"
            )

        # Pokud podmínka nesplněna, vyvolej výjimku
        raise exception_type(message)

    except Exception as e:

        # Zachycení jakékoliv vnitřní chyby při ověřování
        raise SafeVerifyError(f"Chyba při ověřování: {str(e)}")

