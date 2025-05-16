from typing import Any, Tuple, Union

from ..._exceptions import (
    IsSubclassValueError,
    IsSubclassExpectedError,
    VerifyUnexpectedInternalError
)


def is_subclass_verifier(
        value: Any,
        expected: Union[type, Tuple[type, ...]],
        bool_only: bool = False,
        duck_typing: bool = False
) -> bool:
    """
    Ověří, zda je hodnota podtřídou požadovaného typu, nebo zda odpovídá duck typování.

    Args:
        value (Any): Hodnota, která má být ověřena.
        expected (Union[type, Tuple[type, ...]]): Očekávaný typ nebo n-tice typů, proti nimž se provádí ověření.
        bool_only (bool, optional): Pokud True, funkce vrátí False místo vyvolání výjimky při nevalidní hodnotě.
        duck_typing (bool, optional): Pokud True, místo podtřídy provádí ověření pomocí duck typing (ověření metod/atributů).

    Returns:
        bool: True, pokud hodnota odpovídá požadovanému typu (nebo duck typování), jinak False.

    Raises:
        IsSubclassValueError: Pokud hodnota není podtřídou očekávané třídy.
        IsSubclassExpectedError: Pokud je zadaný neplatný očekávaný typ.
        VerifyUnexpectedInternalError: Pokud dojde k jiné neočekávané chybě.
    """

    try:

        # Pokud hodnota odpovídá očekávané třídě, vrať True
        if issubclass(value, expected):
            return True

        # Pokud je nastaveno duck_typing
        if duck_typing:
            pass

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak vyhoď výjimku pro nevalidní hodnotu
        raise IsSubclassValueError(value, expected)

    # Propagace vnitřní výjimky
    except IsSubclassValueError:
        raise

    # Ošetření špatného zadání parametru `expected`
    except TypeError as e:
        raise IsSubclassExpectedError(expected) from e

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e
