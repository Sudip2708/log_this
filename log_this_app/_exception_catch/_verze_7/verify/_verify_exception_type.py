from typing import Type

from ._exceptions import SafeVerifyError, VerifyError


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