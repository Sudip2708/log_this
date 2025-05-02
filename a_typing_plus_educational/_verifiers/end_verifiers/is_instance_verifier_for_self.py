from typing import Any, Tuple, Union

from ..._exceptions import (
    IsInstanceValueError,
    VerifyError,
    InternalUnexpectedError
)
from .._tools import get_self_class

def is_instance_verifier_for_self(
        value: Any,
        expected: Union[type, Tuple[type, ...]],
        custom_types: dict = None,
        bool_only: bool = False,
        duck_typing: bool = False
) -> bool:
    """
    Ověří, zda daná hodnota odpovídá zadanému typu nebo skupině typů.

    Pokud hodnota není instancí očekávaného typu a parametr `bool_only` je
    nastaven na `False`, je vyhozena výjimka `IsInstanceValueError`.

    Args:
        value (Any): Hodnota, kterou chceme ověřit.
        expected (type | tuple[type, ...]): Očekávaný typ nebo n-tice typů.
        custom_types (dict): Kontextový slovník, kde `expected` slouží jako klíč
            a odpovídající hodnota obsahuje instanci, z níž bude získána třída.
        bool_only (bool, optional): Pokud je `True`, funkce pouze vrací
            `True` nebo `False` bez vyhazování výjimek. Výchozí je `False`.
        duck_typing (bool, optional) Pokud je True a neprojde validace na isinstance, pak se provede ještě validace dle atributů

    Returns:
        bool: True, pokud hodnota odpovídá očekávanému typu. Jinak False,
              pokud je `bool_only=True`.

    Raises:
        IsInstanceValueError: Pokud hodnota neodpovídá typu a `bool_only=False`.
        InternalUnexpectedError: Pokud nastane jiná neočekávaná výjimka.
    """

    try:

        # Získání odkazu na self
        self_class = get_self_class(expected, custom_types)

        # Pokud hodnota odpovídá očekávanému typu, vrať True
        if isinstance(value, self_class):
            return True

        # Pokud je nastaveno duck_typing
        if duck_typing:
            pass

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak vyhoď výjimku pro nevalidní hodnotu
        raise IsInstanceValueError(value, self_class)

    # Propagace vnitřní výjimky
    except VerifyError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise InternalUnexpectedError(e) from e
