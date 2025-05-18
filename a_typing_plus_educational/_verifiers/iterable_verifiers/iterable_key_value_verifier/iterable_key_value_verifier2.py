from typing import Any, Dict, Optional, Tuple, Union

from ..._exceptions_base import (
    VerifyError,
    VerifyUnexpectedInternalError
)
from .._exceptions import VerifyInnerCheckError
from .._tools import (
    get_args_safe,
    get_key_value_safe,
    verify_base_type,
    verify_key_value_pairs
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
    Validuje, zda hodnota odpovídá slovníku daného typu a případně rekurzivně kontroluje klíče a hodnoty.

    Nejprve ověří, zda hodnota odpovídá typu `dict` (nebo jeho variantám jako `OrderedDict`, pokud jsou uvedeny).
    Pokud je zapnuta hloubková kontrola (`depth_check`), provede se validace každého klíče a hodnoty
    podle zadané anotace (např. `dict[str, int]`).
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

        # Ověření a získání vnitřních typových anotací pro klíč a hodnotu
        inner_args = get_args_safe(annotation)

        # Pokud nemáme specifikované typy pro klíče a hodnoty, vrátíme True
        if not inner_args:
            return True

        # Načtení klíče a hodnoty
        key_type, value_type = get_key_value_safe(inner_args, annotation)

        return verify_key_value_pairs(
            value.items(),
            key_type,
            value_type,
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