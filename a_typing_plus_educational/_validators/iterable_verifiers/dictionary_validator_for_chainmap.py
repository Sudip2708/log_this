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


def dictionary_validator_for_chainmap(
    value: Any,
    expected: Union[type, Tuple[type, ...]],
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: Tuple[Any, ...] = None,
    bool_only: bool = False
) -> bool:
    """
    Validuje hodnotu typu `collections.ChainMap` s možností rekurzivní kontroly vnitřních slovníků.

    Funkce ověřuje, zda hodnota je instance `ChainMap` (nebo kompatibilního typu), a pokud je aktivní hloubková validace (`depth_check`), zkontroluje typy všech klíčů a hodnot napříč všemi mapami ve stacku. Podporuje i validaci pomocí generické anotace `ChainMap[K, V]`.

    Args:
        value (Any): Hodnota, která má být validována.
        expected (Union[type, Tuple[type, ...]]): Očekávaný typ, např. `ChainMap`.
        annotation (Any, optional): Typová anotace (např. `ChainMap[str, int]`).
        depth_check (Union[bool, int], optional): Hloubková validace. Pokud je `int`, určuje počet úrovní rekurze.
        custom_types (Tuple[Any, ...], optional): Vlastní typy považované za validní.
        bool_only (bool, optional): Pokud `True`, funkce vrací pouze True/False bez vyhazování výjimek.

    Returns:
        bool: `True`, pokud hodnota odpovídá očekávání. V opačném případě vyhazuje výjimku.

    Raises:
        VerifyError: Pokud hodnota nebo její vnitřní prvky neodpovídají očekávaným typům.
        AnnotationDictArgsError: Pokud anotace nemá přesně dva generické argumenty (klíč a hodnota).
        InternalUnexpectedError: Pokud dojde k neočekávané interní chybě.

    Example:
        >>> from collections import ChainMap
        >>> dictionary_validator_for_chainmap(
        ...     ChainMap({'a': 1}, {'b': 2}),
        ...     ChainMap,
        ...     ChainMap[str, int]
        ... )
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

        # Validujeme každý jednotlivý mapping ve stacku
        for mapping in value.maps:

            # Každý mapping by měl být dict-typu (nebo kompatibilní)
            is_instance_validator(mapping, dict)

            # Odpočet zanoření pro další kontrolu
            depth_check = reduce_depth_check(depth_check)
            inner_deep_check = depth_check

            # Validace každého klíče a hodnoty
            for key, val in mapping.items():

                # Rekurzivní validace klíče
                validate_typing(
                    key, key_type, depth_check, custom_types, bool_only
                )

                # Rekurzivní validace hodnoty
                validate_typing(
                    val, value_type, depth_check, custom_types, bool_only
                )

                # Odpočet zanoření pro další kontrolu
                inner_deep_check = reduce_depth_check(inner_deep_check)

                # Přerušení cyklu, pokud se dosáhne maximální hloubky
                if not inner_deep_check:
                    break

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