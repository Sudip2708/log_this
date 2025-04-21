from typing import Callable, Optional, Type, Union
import inspect


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
        raise SafeVerifyError(
            f"Neočekávaná chyba funkce verify. "
            f"{e.__class__.__name__}: {str(e)}"
        )


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
            return _verify_message(message)

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
            f"Neočekávaná chyba funkce _get_error_message. "
            f"{e.__class__.__name__}: {str(e)}"
        )


def _verify_exception_type(
        exception_type: Type[Exception] = VerifyError
) -> bool:
    """
    Ověří validitu zadaného typu výjimky.

    Args:
        exception_type (Type[Exception]): Typ výjimky k ověření.

    Returns:
        bool: True, pokud je typ výjimky platný.

    Raises:
        SafeVerifyError: Pokud zadaný typ není platnou výjimkou.
    """
    try:
        if not isinstance(exception_type, type) or not issubclass(
                exception_type, Exception):
            raise SafeVerifyError(
                f"Zadaný exception_type {exception_type} není platná výjimka"
            )
        return True

    except TypeError:
        raise SafeVerifyError(
            f"Neplatný typ exception_type: {exception_type}"
        )
    except Exception as e:
        raise SafeVerifyError(
            f"Neočekávaná chyba funkce _verify_exception_type. "
            f"{e.__class__.__name__}: {str(e)}")


def _verify_message(message: Optional[str]) -> str:
    """
    Ověří platnost chybové zprávy.

    Args:
        message (Optional[str]): Zpráva k ověření.

    Returns:
        str: Ověřená zpráva.

    Raises:
        SafeVerifyError: Pokud zpráva nesplňuje požadavky.
    """
    try:

        # Převedení na řetězec (pro případ, že by někdo poslal něco jiného)
        message_str = str(message).strip()

        # Volitelné další kontroly, například maximální délka
        if len(message_str) > 500:  # Příklad omezení délky
            raise SafeVerifyError("Chybová zpráva je příliš dlouhá")

        # Kontrola znaků (volitelné)
        if not message_str:
            raise SafeVerifyError("Chybová zpráva nesmí být prázdná")

        return message_str

    except Exception as e:
        raise SafeVerifyError(
            f"Neočekávaná chyba funkce _verify_message. "
            f"{e.__class__.__name__}: {str(e)}")