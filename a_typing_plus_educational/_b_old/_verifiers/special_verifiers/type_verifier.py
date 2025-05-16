from typing import Any, Tuple, Union

from ..._exceptions import (
    VerifyError,
    TypeValueError,
    TypeExpectedError,
    VerifyUnexpectedInternalError
)
from ..end_verifiers import is_instance_verifier, is_subclass_verifier
from .._tools import get_args_safe


def type_verifier(
        value: Any,
        expected: Union[type, Tuple[type, ...]],
        annotation: Any = None,
        depth_check: Union[bool, int] = True,
        bool_only: bool = False
) -> bool:
    try:

        # Validace sebe sama (origin)
        is_instance_verifier(value, expected)

        # Kontrola zda je požadavek i na vnitřní validaci
        if not depth_check:
            return True

        # Načtení vnitřních anotací
        inner_args = get_args_safe(annotation)

        # Pokud není specifikován konkrétní typ, vrátíme True
        if inner_args is None or inner_args == Ellipsis:
            return True

        # Kontrola, zda je třída podtřídou specifikované třídy
        if is_subclass_verifier(value, inner_args):
            return True

        # Kontrola zda odpověď má být bool
        if bool_only:
            return False

        # Vyvolání výjimky s oznamem o nevalidní hodnotě
        raise TypeValueError(value, inner_args)

    # Propagace již ošetřených výjimek
    except VerifyError:
        raise

    # Ošetření špatného zadání parametru `expected`
    except TypeError as e:
        raise TypeExpectedError(expected) from e

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e
