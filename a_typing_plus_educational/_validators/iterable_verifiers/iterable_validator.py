from typing import Any, Tuple, Union

from ..end_verifiers import is_instance_validator
from ..typing_validator import validate_typing
from .._tools import reduce_depth_check, get_args_safe
from ..._exceptions import (
    VerifyError,
    InternalUnexpectedError
)


def iterable_validator(
    value: Any,
    expected: Union[type, Tuple[type, ...]],
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: Tuple[Any, ...] = None,
    bool_only: bool = False
) -> bool:
    """
    Validuje, zda je hodnota iterovatelná a případně rekurzivně kontroluje vnitřní typy.

    Používá se pro kontrolu struktur jako `list`, `set`, `tuple`, atd. Nejprve se ověří,
    zda objekt odpovídá požadovanému základnímu typu (např. `list`, `set`). Pokud je povolena
    hloubková validace (`depth_check`), zkoumají se i vnitřní typy dle anotace.

    Args:
        value (Any): Hodnota, která má být validována.
        expected (Union[type, Tuple[type, ...]]): Požadovaný základní typ nebo typy.
        annotation (Any, optional): Typová anotace, podle které se validují vnitřní prvky.
        depth_check (Union[bool, int], optional): Pokud True, provede se rekurzivní kontrola.
            Pokud int, určuje maximální hloubku zanoření. False přeskočí kontrolu vnitřních typů.
        custom_types (Tuple[Any, ...], optional): Rozšířené vlastní typy pro validaci.
        bool_only (bool, optional): Pokud je True, funkce pouze vrací True/False bez výjimek.

    Returns:
        bool: True, pokud validace proběhne úspěšně. Jinak vyhazuje výjimku.

    Raises:
        VerifyError: Pokud validace typu nebo vnitřního typu selže.
        InternalUnexpectedError: Pokud dojde k nečekané interní chybě během validace.

    Example:
        >>> iterable_validator([1, 2, 3], list, list[int])
        True
    """

    try:

        # Validace základního typu (např. list, set)
        is_instance_validator(value, expected)

        # Pokud není požadována vnitřní validace, návrat
        if not depth_check:
            return True

        # Ověření a získání vnitřních typových anotací
        inner_args = get_args_safe(annotation)

        # Pokud nejsou specifikovány vnitřní typy, validace je považována za úspěšnou
        if not inner_args and not isinstance(value, IterableOrigin):
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
