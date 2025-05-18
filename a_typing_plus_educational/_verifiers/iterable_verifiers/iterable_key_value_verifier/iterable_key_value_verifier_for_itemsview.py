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

def iterable_key_value_verifier_for_itemsview(
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
    Validuje, zda hodnota odpovídá typu `ItemsView[K, V]` a případně rekurzivně kontroluje její klíče a hodnoty.

    Tato funkce je varianta standardní validační logiky pro `dict`, upravená pro `ItemsView`, což je pohled na
    dvojice `(key, value)` poskytované metodou `.items()` u slovníku. Hodnota musí být iterovatelná,
    přičemž každý prvek musí být dvojice (2-tuple) odpovídající dané anotaci `ItemsView[K, V]`.

    V porovnání s běžnou validací pro `dict[K, V]` se mění pouze způsob iterace: místo přímého přístupu přes `.items()`
    je očekáváno, že `value` je samotný `ItemsView`, tedy již iterovatelné dvojice `(key, value)`.

    """


    # Definice parametru pro ověření typu
    base_type_result = None

    try:

        # Pokud je požadována kontrola přes duck typing a anotace ji podporuje
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

        # Ověření a získání vnitřních typových anotací pro klíč a hodnotu
        inner_args = get_args_safe(annotation)

        # Pokud nemáme specifikované typy pro klíče a hodnoty, vrátíme True
        if not inner_args:
            return True

        # Načtení klíče a hodnoty
        key_type, value_type = get_key_value_safe(inner_args)

        # Vytvoření kopie parametru definující hloubkovou kontrolu
        current_check = inner_check

        # Validace každého klíče a hodnoty
        for key, val in value:  # ItemsView poskytuje páry (key, value)

            # Snížení hloubky kontroly
            current_check = reduce_depth_check(current_check)

            # Rekurzivní validace hodnoty na základě vnitřního typu
            # Pokud je parametr bool_only=True, pak při negativním výsledku ukončení iterace
            if not typing_verifier(
                key,
                key_type,
                custom_types,
                current_check,
                duck_typing,
                bool_only
            ):
                return False

            # Rekurzivní validace hodnoty
            # Pokud je parametr bool_only=True, pak při negativním výsledku ukončení iterace
            if not typing_verifier(
                val,
                value_type,
                custom_types,
                current_check,
                duck_typing,
                bool_only
            ):
                return False

            # Přerušení cyklu, pokud se dosáhne maximální hloubky
            # Tato poslední iterace s current_check == 0 ještě proběhne,
            # ale dále již nebude následovat žádná hlubší kontrola.
            # Proto po této iteraci přerušíme cyklus.
            if not current_check:
                break

        # Pokud vše proběhne v pořádku a bez chyb
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