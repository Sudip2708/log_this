from typing import Any, Tuple, Union

from ..typing_validator import validate_typing
from .._tools import (
    reduce_depth_check,
    get_attr_safe,
    is_named_tuple
)
from ..._exceptions import (
    VerifyError,
    InternalUnexpectedError
)


def iterable_key_value_verifier_for_nametuple(
    value: Any,
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: dict = None,
    bool_only: bool = False
) -> bool:
    """
    Validátor pro NamedTuple.

    Tento validátor ověřuje, zda hodnota odpovídá typu `NamedTuple` a pokud ano,
    provádí rekurzivní validaci jednotlivých položek podle jejich anotovaných typů.

    V případě, že není požadována rekurzivní validace (parametr `depth_check`),
    validace se provádí pouze na základní úroveň.

    Args:
        value: Hodnota, která bude validována, měla by být instance `NamedTuple`.
        annotation: Anotace, která obsahuje definice polí pro `NamedTuple`. Typicky třída `NamedTuple` s atributem `__annotations__`.
        depth_check: Pokud je nastaveno na True (nebo jinou hodnotu větší než 0), provádí se rekurzivní validace vnořených položek.
        custom_types: Definice vlastních typů pro přizpůsobenou validaci.
        bool_only: Pokud je True, validace bude ignorovat hodnoty, které nejsou booleovského typu.

    Returns:
        bool: Pokud je validace úspěšná, vrátí True. Pokud je hodnota neplatná, vyvolá výjimku.

    Raises:
        VerifyError: Pokud validace selže a vyvolá vlastní výjimku.
        InternalUnexpectedError: Pokud dojde k nečekané chybě při validaci.
    """

    try:

        # Validace základního typu
        is_named_tuple(value)

        # Pokud není požadována vnitřní validace, návrat
        if not depth_check:
            return True

        # Získání anotací
        field_types = get_attr_safe(annotation, "__annotations__", None)

        # Kontola zda jsou uvedené nějaké anotace
        if not field_types:
            return True

        # Cyklus kontrolující vnitřní typy
        for field_name, expected_type in field_types.items():

            # Získání hodnoty (dle jména)
            field_value = get_attr_safe(value, field_name)

            # Snížení hloubky
            depth_check = reduce_depth_check(depth_check)

            # Validace hodnoty v poli
            validate_typing(
                field_value, expected_type, depth_check, custom_types, bool_only
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