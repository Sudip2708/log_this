from typing import Any, Dict, Optional, Tuple, Union

from ...special_verifiers import duck_typing_verifier
from ...value_verifiers import is_instance_verifier
from ...typing_verifiers import typing_verifier
from ..._exceptions_base import (
    VerifyError,
    VerifyUnexpectedInternalError
)
from .._exceptions import VerifyInnerCheckError
from .._tools import (
    reduce_depth_check,
    get_args_safe,
    get_key_value_safe
)

def iterable_key_value_verifier(
    value: Any,
    expected_type: Union[type, Tuple[type, ...]],
    duck_typing_instructions: Dict[str, Any],
    annotation: Any = None,
    custom_types: Optional[dict] = None,
    inner_check: Union[bool, int] = True,
    duck_typing: bool = False,
    bool_only: bool = False
) -> bool:
    """
    Validátor pro NamedTuple.

    Tento validátor ověřuje, zda hodnota odpovídá typu `NamedTuple` a pokud ano,
    provádí rekurzivní validaci jednotlivých položek podle jejich anotovaných typů.

    V případě, že není požadována rekurzivní validace (parametr `depth_check`),
    validace se provádí pouze na základní úroveň.

    """

    try:

        # Validace základního typu
        is_named_tuple(value)

        # Pokud není požadována vnitřní validace, návrat
        if not depth_check:
            return True

        # Získání anotací
        field_types = get_attr_safe(annotation, "__annotations__", None)

        # Kontola zda jsou uvedené nějaké anotace
        if not field_types:
            return True

        # Cyklus kontrolující vnitřní typy
        for field_name, expected_type in field_types.items():

            # Získání hodnoty (dle jména)
            field_value = get_attr_safe(value, field_name)

            # Snížení hloubky
            depth_check = reduce_depth_check(depth_check)

            # Validace hodnoty v poli
            validate_typing(
                field_value, expected_type, depth_check, custom_types, bool_only
            )

            # Přerušení cyklu, pokud se dosáhne maximální hloubky
            if not depth_check:
                break

        # Pokud vše proběhne v pořádku a bez chyb
        return True

    # Propagace všech již ošetřených výjimek
    except VerifyError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e