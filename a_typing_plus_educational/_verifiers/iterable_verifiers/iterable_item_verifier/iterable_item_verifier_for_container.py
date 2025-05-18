from typing import Any, Dict, Optional, Tuple, Union
from collections.abc import Iterable

from ...special_verifiers import duck_typing_verifier
from ...value_verifiers import is_instance_verifier
from ...typing_verifiers import typing_verifier
from ..._exceptions_base import (
    VerifyError,
    VerifyUnexpectedInternalError
)
from .._tools import reduce_depth_check, get_args_safe
from .._exceptions import VerifyInnerCheckError


def iterable_item_verifier_for_container(
        value: Any,
        expected_type: Union[type, Tuple[type, ...]],
        duck_typing_instructions: Dict[str, Any],
        annotation: Any = None,
        custom_types: Optional[dict] = None,
        inner_check: Union[bool, int] = True,
        duck_typing: bool = False,
        bool_only: bool = False
) -> bool:
    """Speciální verze iterovatelného validdátoru pro Container[T]"""

    # Definice parametru pro ověření typu
    base_type_result = None

    try:

        # Pokud je požadována kntrola přes duck typing logiku a anotace ji podporuje
        if duck_typing and duck_typing_instructions:
            base_type_result  = duck_typing_verifier(
                value,
                duck_typing_instructions,
                bool_only=bool_only
            )

        # Jinak proveď ověření na základě validace základního typu (např. list, set)
        else:
            base_type_result = is_instance_verifier(
                value,
                expected_type,
                bool_only=bool_only
            )

        # Kontrola zda je výsledek negativní
        # V tomto bodě, base_type_result musí být buď True nebo False (nebo je vyvolaná výjimka)
        if not base_type_result:
            return False

        # Pokud není požadována vnitřní validace, návrat
        if not inner_check:
            return True

        # Ověření a získání vnitřních typových anotací
        inner_args = get_args_safe(annotation)

        # Pokud nejsou specifikovány vnitřní typy, validace je považována za úspěšnou
        if not inner_args and not isinstance(value, Iterable):
            return True

        # Vytvoření kopie parametru definující hloubkovou kontrolu
        current_check = inner_check

        # Validace jednotlivých položek uvnitř struktury
        for item in value:

            # Snížení hloubky kontroly
            current_check = reduce_depth_check(current_check)

            # Rekurzivní validace hodnoty na základě vnitřního typu
            # Pokud je parametr bool_only=True, pak při negativním výsledku ukončení iterace
            if not typing_verifier(
                item,
                inner_args[0],
                custom_types,
                current_check,
                duck_typing,
                bool_only
            ):
                return False

            # Přerušení cyklu, pokud se dosáhne maximální hloubky
            if not current_check:
                break

        # Pokud vše projde navrácení úspěšné validace
        return True

    # Ošetření vnitřních výjimek
    except VerifyError as e:

        # Pokud první kontrola typu vrátila True
        if base_type_result:
            raise VerifyInnerCheckError(value, annotation, e)

        # Jinak vnitřní výjimky jen propaguj
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e
