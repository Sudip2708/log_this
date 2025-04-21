from typing import Callable, Optional, Type, Union, Any
import inspect
import sys


class VerifyError(Exception):
    """
    Vlastní výjimka pro selhání ověřovacích kontrol.

    Args:
        message (str): Detailní popis důvodu selhání ověření.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class SafeVerifyError(Exception):
    """
    Interní výjimka pro bezpečné zachytávání chyb během ověřování.

    Args:
        message (str): Interní chybová zpráva zachycující technické detaily selhání.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


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
        raise SafeVerifyError(f"Neočekávaná chyba při ověřování: {str(e)}")


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
        except Exception as call_error:
            raise SafeVerifyError(
                f"Chyba při volání ověřovací funkce: {str(call_error)}")

        # Kontrola výsledku volání
        if result is True:
            return True

        raise exception_type(_get_error_message(message))

    except TypeError as e:
        raise SafeVerifyError(f"Neplatný typ při ověřování callable: {str(e)}")
    except Exception as e:
        raise SafeVerifyError(
            f"Neočekávaná chyba při ověřování callable: {str(e)}")


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

        raise exception_type(_get_error_message(message))

    except TypeError as e:
        raise SafeVerifyError(f"Neplatný typ boolean hodnoty: {str(e)}")
    except Exception as e:
        raise SafeVerifyError(
            f"Neočekávaná chyba při ověřování boolean: {str(e)}")


def _get_error_message(
        message: Optional[str] = None,
) -> str:
    """
    Generování kontextové chybové zprávy.

    Args:
        message (Optional[str], optional): Volitelná uživatelská chybová zpráva.

    Returns:
        str: Detailní chybová zpráva.

    Raises:
        SafeVerifyError: Při problémech s extrakcí kontextových informací.
    """
    try:
        # Preferovaná uživatelská zpráva
        if message:
            return message

        # Extrakce informací o volání
        frame = inspect.currentframe()
        try:
            caller_frame = frame.f_back
            if caller_frame:
                caller_info = inspect.getframeinfo(caller_frame)
                return (
                    f"Ověření selhalo v metodě {caller_info.function} "
                    f"v souboru {caller_info.filename}:{caller_info.lineno}"
                )
            return "Ověření selhalo v neznámém kontextu"

        finally:
            # Explicitní smazání reference na frame
            del frame

    except Exception as e:
        raise SafeVerifyError(
            f"Kritická chyba při generování chybové zprávy: {str(e)}")