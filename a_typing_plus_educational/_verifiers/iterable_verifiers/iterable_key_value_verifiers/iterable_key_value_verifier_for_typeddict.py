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
    Validuje hodnotu vůči anotaci typu `TypedDict` a jejímu vnitřnímu rozložení.

    Tato funkce rozšiřuje základní logiku validace slovníku o specifika `TypedDict`:
    kontroluje typy hodnot podle anotace atributů a případně přítomnost či nepřítomnost klíčů
    v závislosti na totalitě (`__total__`) typu.

    - Pokud je `TypedDict` totalitní (`__total__=True`), ověřuje se:
        - že slovník má přesně všechny požadované klíče,
        - že žádný klíč nechybí ani nepřebývá,
        - a že všechny hodnoty odpovídají definovaným typům.
    - Pokud není totalitní (`__total__=False`), ověřuje se:
        - že slovník obsahuje minimálně všechny povinné klíče,
        - a že definované klíče (pokud existují v hodnotě) odpovídají svému typu.

    Hloubková kontrola (`depth_check`) umožňuje rekurzivní validaci hodnot uvnitř `TypedDict`.
    Stejně jako u běžného slovníku lze kontrolovat typy klíčů a hodnot do zvolené hloubky.
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

        # Ověření a získání vnitřních typových anotací pro klíče a hodnoty
        type_hints = get_type_hints_safe(annotation)

        # Pokud nemáme žádné anotace, vrátíme True
        if not type_hints:
            return True

        # Získání informací o totalitě (všechny klíče jsou povinné)
        is_total = get_attr_safe(annotation, "__total__", True)

        # Pokud je hlavní třída total (potomek musí přesně korespondovat)
        if is_total:

            # Kontrola zda oba slovníky obsahují shodné klíče
            compare_dicts_keys(type_hints, value)

            # Kopije hodnoty zanoření
            inner_depth = depth_check

            # Kontrola typů u existujících klíčů
            for key, val in value.items():

                # Odpočet zanoření pro další kontrolu
                inner_depth = reduce_depth_check(inner_depth)

                # Kontrola na očekávaný typ
                expected_type = type_hints[key]

                # Validace hodnoty a typu
                validate_typing(
                    val, expected_type, inner_depth, custom_types, bool_only
                )

                # Kontrola zanoření
                if not inner_depth:
                    break

        # Pokud hlavní třída není total (potomek nemusí mýt všechny klíče a může mít i klíče navíc)
        else:

            # Kontrola zda slovník obsahuje poviné klíče
            check_required_keys(type_hints, value)

            # Kopije hodnoty zanoření
            inner_depth = depth_check

            # Validace každého klíče a hodnoty
            for key, val in value.items():

                # Kontrola zda je klíč definovaný na hlavní třídě
                if key in type_hints:

                    # Odpočet zanoření pro další kontrolu
                    inner_depth = reduce_depth_check(inner_depth)

                    # Načtení typu z hlavní třídy
                    expected_type = type_hints[key]

                    # Validace hodnoty a typu
                    validate_typing(
                        val, expected_type, inner_depth, custom_types, bool_only
                    )

                # Přerušení cyklu, pokud se dosáhne maximální hloubky
                if not inner_depth:
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