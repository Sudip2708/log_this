from typing import Any, Tuple, Union

from ..._exceptions import (
    IsInstanceValueError,
    IsInstanceExpectedError,
    InternalUnexpectedError
)


def is_instance_validator(
        value: Any,
        expected: Union[type, Tuple[type, ...]],
        bool_only: bool = False
) -> bool:
    """
    Ověří, zda daná hodnota odpovídá zadanému typu nebo skupině typů.

    Pokud hodnota není instancí očekávaného typu a parametr `bool_only` je
    nastaven na `False`, je vyhozena výjimka `IsInstanceValueError`.

    Args:
        value (Any): Hodnota, kterou chceme ověřit.
        expected (type | tuple[type, ...]): Očekávaný typ nebo n-tice typů.
        bool_only (bool, optional): Pokud je `True`, funkce pouze vrací
            `True` nebo `False` bez vyhazování výjimek. Výchozí je `False`.

    Returns:
        bool: True, pokud hodnota odpovídá očekávanému typu. Jinak False,
              pokud je `bool_only=True`.

    Raises:
        IsInstanceValueError: Pokud hodnota neodpovídá typu a `bool_only=False`.
        IsInstanceExpectedError: Pokud je očekávaný typ špatně zadaný (např. není typ).
        InternalUnexpectedError: Pokud nastane jiná neočekávaná výjimka.
    """

    try:

        # Pokud hodnota odpovídá očekávanému typu, vrať True
        if isinstance(value, expected):
            return True

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak vyhoď výjimku pro nevalidní hodnotu
        raise IsInstanceValueError(value, expected)

    # Přeposlání vnitřní výjimky
    except IsInstanceValueError:
        raise

    # Ošetření špatného zadání parametru `expected`
    except TypeError as e:
        raise IsInstanceExpectedError(expected) from e

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise InternalUnexpectedError(e) from e
