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
    VerifyUnexpectedInternalError
)


def dictionary_validator(
    value: Any,
    expected: Union[type, Tuple[type, ...]],
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: dict = None,
    bool_only: bool = False
) -> bool:
    """
    Validuje, zda hodnota odpovídá slovníku daného typu a případně rekurzivně kontroluje klíče a hodnoty.

    Nejprve ověří, zda hodnota odpovídá typu `dict` (nebo jeho variantám jako `OrderedDict`, pokud jsou uvedeny).
    Pokud je zapnuta hloubková kontrola (`depth_check`), provede se validace každého klíče a hodnoty
    podle zadané anotace (např. `dict[str, int]`).

    Args:
        value (Any): Hodnota, která má být validována.
        expected (Union[type, Tuple[type, ...]]): Očekávaný základní typ (např. `dict`).
        annotation (Any, optional): Typová anotace, např. `dict[str, int]`.
        depth_check (Union[bool, int], optional): Hloubková kontrola. Pokud je int, určuje počet úrovní.
        custom_types (Tuple[Any, ...], optional): Vlastní typy, které se mají považovat za validní.
        bool_only (bool, optional): Pokud True, vrací pouze True/False bez vyhazování výjimek.

    Returns:
        bool: True, pokud hodnota projde validací. Jinak vyhazuje výjimku.

    Raises:
        VerifyError: Pokud hodnota nebo její vnitřní prvky neodpovídají očekávaným typům.
        AnnotationDictArgsError: Pokud anotace neobsahuje přesně dva argumenty (klíč a hodnota).
        VerifyUnexpectedInternalError: Pokud dojde k nečekané interní chybě.

    Example:
        >>> dictionary_validator({"a": 1, "b": 2}, dict, dict[str, int])
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