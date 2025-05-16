from typing import Any, Dict, Optional, Tuple, Union

from ...special_verifiers import duck_typing_verifier
from ...value_verifiers import is_instance_verifier
from ...typing_verifiers import typing_verifier
from .._tools import reduce_depth_check, get_args_safe
from ..._exceptions_base import (
    VerifyError,
    VerifyUnexpectedInternalError
)
from .._exceptions import VerifyInnerCheckError


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

        # Pokud nemáme specifikované vnitřní typy, vrátíme True
        if not inner_args:
            return True

        # Zjištění, zda se jedná o variabilní n-tici (Tuple[T, ...])
        is_variable_tuple = len(inner_args) == 2 and inner_args[1] == Ellipsis

        # Variabilní n-tice (Tuple[T, ...])
        if is_variable_tuple:

            # Načtení typu
            item_type = inner_args[0]

            # Vytvoření kopie parametru definující hloubkovou kontrolu
            current_check = inner_check

            # Kontrola všech položek proti stejnému typu
            for item in value:

                # Snížení hloubky kontroly
                current_check = reduce_depth_check(current_check)

                # Rekurzivní validace hodnoty na základě vnitřního typu
                typing_verifier(
                    item,
                    item_type,
                    custom_types,
                    current_check,
                    duck_typing,
                    bool_only
                )

                # Přerušení cyklu, pokud se dosáhne maximální hloubky
                if not current_check:
                    break

        # Fixní n-tice (Tuple[T1, T2, ...])
        else:

            # Kontrola délky
            if len(value) != len(inner_args):
                raise ValueError(
                    f"Očekávaná délka n-tice {len(inner_args)}, ale obdrženo {len(value)}")

            # Vytvoření kopie parametru definující hloubkovou kontrolu
            current_check = inner_check

            # Kontrola typu každé položky na dané pozici
            for i, (item, item_type) in enumerate(zip(value, inner_args)):

                # Snížení hloubky kontroly
                current_check = reduce_depth_check(current_check)

                # Rekurzivní validace hodnoty na základě vnitřního typu
                typing_verifier(
                    item,
                    item_type,
                    custom_types,
                    current_check,
                    duck_typing,
                    bool_only
                )

                # Přerušení cyklu, pokud se dosáhne maximální hloubky
                if not current_check:
                    break

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
