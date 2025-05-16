from typing import Any

from ..._exceptions import NoReturnValueError


def no_return_verifier(value: Any, bool_only: bool = False) -> bool:
    """
    Ověřuje, že hodnota není přítomna – což je požadavek typu NoReturn.

    Args:
        value (Any): Hodnota, která by neměla být nikdy vrácena.
        bool_only (bool): Pokud je True, vrací jen False bez výjimky.

    Returns:
        bool: False – pokud je hodnota přítomna, není to platný NoReturn.

    Raises:
        NoReturnValueError: Pokud bool_only=False, vyvolá informativní výjimku.
    """
    if bool_only:
        return False
    raise NoReturnValueError(value)
