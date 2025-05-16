from typing import Any, Tuple, Union

from ..end_verifiers import is_instance_verifier
from ..typing_validator import validate_typing
from .._tools import (
    reduce_depth_check,
    get_args_safe,
)
from ..._exceptions import (
    VerifyError,
    VerifyUnexpectedInternalError
)


def iterable_key_value_verifier_for_counter(
    value: Any,
    expected: Union[type, Tuple[type, ...]],
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: dict = None,
    bool_only: bool = False
) -> bool:
    """
    Validuje, zda hodnota odpovídá typu `Counter[K]` a rekurzivně kontroluje klíče.

    Tato funkce je specializovaná varianta validační logiky pro `dict`, která je upravena pro potřeby `collections.Counter`.
    Ověřuje, zda hodnota odpovídá typu `Counter`, a následně (pokud je zapnuta hloubková kontrola) validuje
    typ klíčů podle typové anotace `Counter[K]`, přičemž hodnota je vždy `int`.

    Logika odpovídá standardní validační funkci pro `dict[K, V]`, s tím rozdílem, že:
    - Hodnoty nejsou odvozovány z anotace, ale jsou vždy pevně typovány jako `int`.
    - Ověřují se tedy pouze typy klíčů, zatímco hodnoty jsou kontrolovány pouze na `int`.

    Args:
        value (Any): Hodnota, která má být validována (např. `Counter[str]`).
        expected (Union[type, Tuple[type, ...]]): Očekávaný základní typ (`Counter`).
        annotation (Any, optional): Typová anotace, např. `Counter[str]`.
        depth_check (Union[bool, int], optional): Hloubková kontrola. Pokud je int, určuje počet úrovní.
        custom_types (Tuple[Any, ...], optional): Vlastní typy, které se mají považovat za validní.
        bool_only (bool, optional): Pokud True, vrací pouze True/False bez vyhazování výjimek.

    Returns:
        bool: True, pokud hodnota projde validací. Jinak vyhazuje výjimku.

    Raises:
        VerifyError: Pokud hodnota nebo její vnitřní prvky neodpovídají očekávaným typům.
        AnnotationDictArgsError: Pokud anotace neobsahuje přesně jeden argument (typ klíče).
        VerifyUnexpectedInternalError: Pokud dojde k nečekané interní chybě.

    Example:
        >>> from collections import Counter
        >>> iterable_key_value_verifier_for_counter(Counter({"a": 2, "b": 1}), Counter, Counter[str])
        True
    """


    try:

        # Validace základního typu (např. dict)
        is_instance_verifier(value, expected)

        # Pokud není požadována vnitřní validace, návrat
        if not depth_check:
            return True

        # Ověření a získání vnitřních typových anotací pro klíč a hodnotu
        inner_args = get_args_safe(annotation)

        # Pokud nemáme specifikované typy pro klíče a hodnoty, vrátíme True
        if not inner_args:
            return True

        # Načtení klíče a hodnoty
        key_type = inner_args[0]
        value_type = int

        # Validace každého klíče a hodnoty
        for key, val in value.items():

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
        raise VerifyUnexpectedInternalError(e) from e