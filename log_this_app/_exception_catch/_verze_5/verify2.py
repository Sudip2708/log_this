from typing import Callable, Optional, Type, Union
import inspect


class VerifyError(Exception):
    """Vlastní výjimka pro selhání ověření."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class SafeVerifyError(Exception):
    """Interní výjimka pro bezpečné ověřování."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def verify(
        condition: Union[bool, Callable[[], bool]],
        message: Optional[str] = None,
        exception_type: Type[Exception] = VerifyError
) -> bool:
    try:
        if callable(condition):
            return verify_call(condition, message, exception_type)
        return verify_bool(condition, message, exception_type)

    except Exception as e:
        raise SafeVerifyError(f"Chyba při ověřování: {str(e)}")


def verify_call(
        condition: Callable[[], bool],
        message: Optional[str] = None,
        exception_type: Type[Exception] = VerifyError
) -> bool:
    """
     Universální metoda pro ověřování podmínek.

    :param condition: Podmínka k ověření callable
    :param message: Volitelná chybová zpráva
    :param exception_type: Typ výjimky (default VerifyError)
    :return: True pokud je podmínka splněna
    :raises: Specifikovaná výjimka při selhání
    """

    try:

        # Pokud je splněna podmínka vrať True
        if condition():
            return True

        # Pokud podmínka nesplněna, vyvolej výjimku
        raise exception_type(_get_error_message(message))

    except Exception as e:
        raise SafeVerifyError(f"Chyba při ověřování callable: {str(e)}")


def verify_bool(
        condition: bool,
        message: Optional[str] = None,
        exception_type: Type[Exception] = VerifyError
) -> bool:
    """
    Bezpečná interní metoda pro ověřování vstupů.

    :param condition: Podmínka k ověření boolean
    :param message: Volitelná chybová zpráva
    :param exception_type: Typ výjimky (default VerifyError)
    :return: True pokud je podmínka splněna
    :raises: Specifikovaná výjimka při selhání
    """

    try:

        # Pokud je splněna podmínka vrať True
        if condition:
            return True

        # Pokud podmínka nesplněna, vyvolej výjimku
        raise exception_type(_get_error_message(message))

    except Exception as e:
        raise SafeVerifyError(f"Chyba při ověřování boolean: {str(e)}")


def _get_error_message(
        message: Optional[str] = None,
):
    """
    Získání chybového oznamu

    :param message: Volitelná chybová zpráva
    :return: Chybová zpráva
    :raises: Specifikovaná výjimka při selhání
    """

    try:

        # Pokud je zpráva definovaná, vrať definovanou
        if message:
            return message

        # Zjištění kontextu volání
        frame = inspect.currentframe().f_back
        caller_info = inspect.getframeinfo(frame)

        return (
            f"Ověření selhalo v metodě {caller_info.function} "
            f"v souboru {caller_info.filename}:{caller_info.lineno}"
        )

    except Exception as e:
        raise SafeVerifyError(f"Chyba při vytváření chybové zprávy: {str(e)}")