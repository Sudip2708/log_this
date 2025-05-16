from typing import Any, Union, Callable, Concatenate, get_args, get_origin

from ..._exceptions import VerifyError, VerifyUnexpectedInternalError
from .callable_verifier import callable_verifier
from .._tools import function_signature_check, get_args_safe


def concatenate_verifier(
        value: Any,
        expected: type,
        annotation: Any = None,
        depth_check: Union[bool, int] = True,
        custom_types: dict = None,
        bool_only: bool = False
) -> bool:
    """
    Validuje, zda hodnota odpovídá typu specifikovanému pomocí Concatenate.

    Poznámka: Plná validace typů v Concatenate vyžaduje pokročilou analýzu signatury funkce,
    která je mimo rozsah této validační funkce. Provádí se tedy zjednodušená kontrola.

    Args:
        value (Any): Hodnota, která má být validována.
        expected (type): Očekávaný typ (Concatenate).
        annotation (Any, optional): Typová anotace, např. Concatenate[P, int, str].
        depth_check (Union[bool, int], optional): Hloubková kontrola.
        custom_types (dict, optional): Vlastní typy.
        bool_only (bool, optional): Pokud True, vrací pouze True/False.

    Returns:
        bool: True, pokud hodnota projde validací.

    Raises:
        VerifyError: Pokud hodnota není funkcí nebo nemá odpovídající signaturu.
    """
    try:

        # Základní kontrola - hodnota musí být volatelná (callable)
        callable_verifier(value)

        # Pokud není požadována hloubková kontrola nebo nemáme anotaci
        if not depth_check or not annotation:
            return True

        # Získání argumentů z anotace Concatenate[P, Arg1, Arg2, ...]
        concat_args = get_args_safe(annotation)

        # Pokud nemáme argumenty, nemůžeme pokračovat v kontrole
        if not concat_args or len(concat_args) < 2:
            return True

        # Kontrola argumentů
        function_signature_check(concat_args, value, bool_only)

    except VerifyError:
        raise

    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e