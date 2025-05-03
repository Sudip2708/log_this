from typing import Any, Tuple, Union

from ..end_verifiers import is_instance_verifier
from ..typing_validator import validate_typing
from .._tools import reduce_depth_check, get_args_safe
from ..._exceptions import (
    VerifyError,
    InternalUnexpectedError
)


def iterable_item_verifier_for_tuple(
    value: Any,
    expected: Union[type, Tuple[type, ...]],
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: dict = None,
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
        >>> iterable_item_verifier([1, 2, 3], list, list[int])
        True
    """

    try:

        # Validace sebe sama (origin)
        is_instance_verifier(value, expected)

        # Kontrola zda je požadavek i na vnitřní validaci
        if not depth_check:
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

            # Vytvoření vlastní hloubky
            depth = depth_check

            # Kontrola všech položek proti stejnému typu
            for item in value:

                # Změna hloubky
                depth = reduce_depth_check(depth)

                # Validace hodnoty
                validate_typing(
                    item, item_type, depth, custom_types, bool_only
                )

                # Kontrola vyčerpání zanoření (přerušení cyklu)
                if not depth_check:
                    break

        # Fixní n-tice (Tuple[T1, T2, ...])
        else:

            # Kontrola délky
            if len(value) != len(inner_args):
                raise ValueError(
                    f"Očekávaná délka n-tice {len(inner_args)}, ale obdrženo {len(value)}")

            # Vytvoření vlastní hloubky
            depth = depth_check

            # Kontrola typu každé položky na dané pozici
            for i, (item, item_type) in enumerate(zip(value, inner_args)):

                # Změna hloubky
                depth = reduce_depth_check(depth)

                # Validace hodnoty
                validate_typing(
                    item, item_type, depth, custom_types, bool_only
                )

                # Kontrola vyčerpání zanoření (přerušení cyklu)
                if not depth_check:
                    break

        return True

    # Propagace všech již ošetřených výjimek
    except VerifyError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise InternalUnexpectedError(e) from e
