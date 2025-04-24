from typing import Any, Tuple, Union
from collections.abc import Iterable

from ..end_verifiers import is_instance_validator
from ..typing_validator import validate_typing
from .._tools import reduce_depth_check, get_args_safe
from ..._exceptions import (
    VerifyError,
    InternalUnexpectedError
)


def iterable_validator_for_container(
    value: Any,
    expected: Union[type, Tuple[type, ...]],
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: Tuple[Any, ...] = None,
    bool_only: bool = False
) -> bool:
    """Speciální verze iterovatelného validdátoru pro Container[T]"""


    try:

        # Validace základního typu (např. list, set)
        is_instance_validator(value, expected)

        # Pokud není požadována vnitřní validace, návrat
        if not depth_check:
            return True

        # Ověření a získání vnitřních typových anotací
        inner_args = get_args_safe(annotation)

        # Pokud nejsou specifikovány vnitřní typy, validace je považována za úspěšnou
        if not inner_args and not isinstance(value, Iterable):
            return True

        # Validace jednotlivých položek uvnitř struktury
        for item in value:

            # Snížení hloubky kontroly
            depth_check = reduce_depth_check(depth_check)

            # Rekurzivní validace hodnoty na základě vnitřního typu
            validate_typing(
                item, inner_args[0], depth_check, custom_types, bool_only
            )

            # Přerušení cyklu, pokud se dosáhne maximální hloubky
            if not depth_check:
                break

        # Pokud vše projde navrácení úspěšné validace
        return True

    # Propagace všech již ošetřených výjimek
    except VerifyError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise InternalUnexpectedError(e) from e
