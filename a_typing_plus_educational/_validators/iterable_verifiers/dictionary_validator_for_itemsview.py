from typing import Any, Tuple, Union

from ..end_verifiers import is_instance_validator
from ..typing_validator import validate_typing
from .._tools import (
    reduce_depth_check,
    get_args_safe,
    get_key_value_safe
)
from ..._exceptions import (
    VerifyError,
    InternalUnexpectedError
)


def dictionary_validator_for_itemsview(
    value: Any,
    expected: Union[type, Tuple[type, ...]],
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: Tuple[Any, ...] = None,
    bool_only: bool = False
) -> bool:
    """
    Validuje, zda hodnota odpovídá typu `ItemsView[K, V]` a případně rekurzivně kontroluje její klíče a hodnoty.

    Tato funkce je varianta standardní validační logiky pro `dict`, upravená pro `ItemsView`, což je pohled na
    dvojice `(key, value)` poskytované metodou `.items()` u slovníku. Hodnota musí být iterovatelná,
    přičemž každý prvek musí být dvojice (2-tuple) odpovídající dané anotaci `ItemsView[K, V]`.

    V porovnání s běžnou validací pro `dict[K, V]` se mění pouze způsob iterace: místo přímého přístupu přes `.items()`
    je očekáváno, že `value` je samotný `ItemsView`, tedy již iterovatelné dvojice `(key, value)`.

    Args:
        value (Any): Hodnota, která má být validována (např. `dict.items()`).
        expected (Union[type, Tuple[type, ...]]): Očekávaný typ (`ItemsView`).
        annotation (Any, optional): Typová anotace, např. `ItemsView[str, int]`.
        depth_check (Union[bool, int], optional): Hloubková kontrola. Pokud je int, určuje počet úrovní.
        custom_types (Tuple[Any, ...], optional): Vlastní typy, které se mají považovat za validní.
        bool_only (bool, optional): Pokud True, vrací pouze True/False bez vyhazování výjimek.

    Returns:
        bool: True, pokud hodnota projde validací. Jinak vyhazuje výjimku.

    Raises:
        VerifyError: Pokud hodnota nebo její vnitřní prvky neodpovídají očekávaným typům.
        AnnotationDictArgsError: Pokud anotace neobsahuje přesně dva argumenty (klíč a hodnota).
        InternalUnexpectedError: Pokud dojde k nečekané interní chybě.

    Example:
        >>> d = {"a": 1, "b": 2}
        >>> dictionary_validator_for_items_view(d.items(), ItemsView, ItemsView[str, int])
        True
    """


    try:

        # Validace základního typu (např. dict)
        is_instance_validator(value, expected)

        # Pokud není požadována vnitřní validace, návrat
        if not depth_check:
            return True

        # Ověření a získání vnitřních typových anotací pro klíč a hodnotu
        inner_args = get_args_safe(annotation)

        # Pokud nemáme specifikované typy pro klíče a hodnoty, vrátíme True
        if not inner_args:
            return True

        # Načtení klíče a hodnoty
        key_type, value_type = get_key_value_safe(inner_args)

        # Validace každého klíče a hodnoty
        for key, val in value:  # ItemsView poskytuje páry (key, value)

            # Odpočet zanoření pro další kontrolu
            depth_check = reduce_depth_check(depth_check)

            # Rekurzivní validace klíče
            validate_typing(
                key, key_type, depth_check, custom_types, bool_only
            )

            # Rekurzivní validace hodnoty
            validate_typing(
                val, value_type, depth_check, custom_types, bool_only
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
        raise InternalUnexpectedError(e) from e