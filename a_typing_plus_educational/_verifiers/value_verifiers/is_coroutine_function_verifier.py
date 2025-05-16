from typing import Any
from inspect import iscoroutinefunction

from .._exceptions_base import VerifyUnexpectedInternalError
from ._exceptions import VerifyNotCoroutineFunctionError


def is_coroutine_function_verifier(
        obj: Any,
        bool_only: bool = False
) -> bool:

    try:

        # Pokud je objekt coroutine function, vrať True
        if iscoroutinefunction(obj):
            return True

        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
        if bool_only:
            return False

        # Jinak vyhoď výjimku pro nevalidní hodnotu
        raise VerifyNotCoroutineFunctionError(obj)

    # Propagace vnitřní výjimky
    except VerifyNotCoroutineFunctionError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e


# Přejmenování funkce pro vnější výstup
verify_coroutine_function = is_coroutine_function_verifier