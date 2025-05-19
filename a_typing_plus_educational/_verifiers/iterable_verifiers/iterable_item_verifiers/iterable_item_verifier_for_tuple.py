from typing import Any, Dict, Optional, Tuple, Union

from ..._exceptions_base import (
    VerifyError,
    VerifyUnexpectedInternalError
)
from .._exceptions import VerifyInnerCheckError
from .._tools import (
    get_args_safe,
    verify_base_type,
    verify_iterable_items,
    verify_fixed_tuple_items
)

def iterable_item_verifier_for_tuple(
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
    Validuje, zda je hodnota iterovatelná a případně rekurzivně kontroluje vnitřní typy.

    Používá se pro kontrolu struktur jako `list`, `set`, `tuple`, atd. Nejprve se ověří,
    zda objekt odpovídá požadovanému základnímu typu (např. `list`, `set`). Pokud je povolena
    hloubková validace (`depth_check`), zkoumají se i vnitřní typy dle anotace.

    """

    # Definice parametru pro ověření typu
    base_type_result = None

    try:

        # Kontrola základního typu
        base_type_result = verify_base_type(
            value,
            expected_type,
            duck_typing_instructions,
            duck_typing,
            bool_only
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

        # Pokud nemáme specifikované vnitřní typy, vrátíme True
        if not inner_args:
            return True

        # Zjištění, zda se jedná o variabilní n-tici (Tuple[T, ...])
        is_variable_tuple = len(inner_args) == 2 and inner_args[1] == Ellipsis

        # Variabilní n-tice (Tuple[T, ...])
        if is_variable_tuple:

            # Kontrola vnitřních položek
            return verify_iterable_items(
                value,
                inner_args[0],
                custom_types,
                inner_check,
                duck_typing,
                bool_only
            )

        # Fixní n-tice (Tuple[T1, T2, ...])
        else:

            # Kontrola vnitřních položek
            return verify_fixed_tuple_items(
                value,
                inner_args,
                custom_types,
                inner_check,
                duck_typing,
                bool_only
            )

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
