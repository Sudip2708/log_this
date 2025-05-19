from typing import Any, Dict, Optional, Tuple, Union
from collections.abc import Iterable

from ..._exceptions_base import (
    VerifyError,
    VerifyUnexpectedInternalError
)
from .._exceptions import VerifyInnerCheckError
from .._tools import (
    get_args_safe,
    verify_base_type,
    verify_iterable_items
)


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

        # Pokud nejsou specifikovány vnitřní typy, validace je považována za úspěšnou
        if not inner_args and not isinstance(value, Iterable):
            return True

        # Kontrola vnitřních položek
        return verify_iterable_items(
            value,
            inner_args[0],
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
