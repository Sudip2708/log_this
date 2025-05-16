from typing import Any

from ..._exceptions import (
    LiteralValueError,
    VerifyUnexpectedInternalError
)
from .._tools import get_args_safe


def literal_verifier(
        value: Any,
        annotation: Any = None,
        bool_only: bool = False,
) -> bool:
    """
    Ověří, zda hodnota odpovídá některé z hodnot definovaných v `Literal`.

    Funkce získá možné povolené hodnoty z typové anotace `Literal`
    a ověří, zda předaná hodnota patří mezi ně.
    Pokud ano, vrací True. Pokud ne:
        - při zapnutém `bool_only` vrací False,
        - jinak vyhazuje výjimku `LiteralValueError`.

    Args:
        value (Any): Hodnota k ověření.
        annotation (Any, optional): Typová anotace typu `Literal`.
        bool_only (bool, optional): Pokud je True, vrací pouze True/False bez vyhazování výjimky.

    Returns:
        bool: Výsledek ověření (True pokud hodnota odpovídá některé hodnotě v `Literal`, jinak False při bool_only).

    Raises:
        LiteralValueError: Pokud hodnota není mezi povolenými a bool_only je False.
        VerifyUnexpectedInternalError: Pokud dojde k neočekávané chybě během ověřování.
    """

    try:

        # Získání tuple s vnitřními typy
        inner_args = get_args_safe(annotation)

        # Validace hodnoty vůči vnitřnímu typu
        if inner_args and value in inner_args:
            return True

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak vyhoď výjimku pro nevalidní hodnotu
        raise LiteralValueError(value)

    # Propagace vnitřní výjimky
    except LiteralValueError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e
