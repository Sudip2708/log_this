from typing import Any

from ..._exceptions import (
    CallableValueError,
    InternalUnexpectedError
)


def callable_verifier(
        value: Any,
        bool_only: bool = False,
        duck_typing: bool = False
) -> bool:
    """
    Ověří, zda je hodnota volatelná (`callable`).

    Funkce ověřuje, zda předaná hodnota splňuje kritérium volatelnosti.
    Pokud ano, vrací True. Pokud ne:
        - při zapnutém `bool_only` vrací False,
        - jinak vyhazuje výjimku `CallableValueError`.
    V budoucnu je možné rozšířit o podporu duck typing kontroly.

    Args:
        value (Any): Hodnota k ověření.
        bool_only (bool, optional): Pokud je True, vrací pouze True/False bez vyhazování výjimky.
        duck_typing (bool, optional): Rezervováno pro budoucí podporu duck typingu. Výchozí False.

    Returns:
        bool: Výsledek ověření (True pokud volatelná, jinak False při bool_only).

    Raises:
        CallableValueError: Pokud hodnota není volatelná a bool_only je False.
        InternalUnexpectedError: Pokud dojde k neočekávané chybě.
    """

    try:

        # Pokud je hodnota volatelná, vrať True
        if callable(value):
            return True

        # Pokud je nastaveno duck_typing
        if duck_typing:
            pass

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak vyhoď výjimku pro nevalidní hodnotu
        raise CallableValueError(value)

    # Propagace vnitřní výjimky
    except CallableValueError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise InternalUnexpectedError(e) from e
