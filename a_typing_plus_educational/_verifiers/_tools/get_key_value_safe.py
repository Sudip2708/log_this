from typing import Any
from ..._exceptions import AnnotationDictArgsError


def get_key_value_safe(inner_args: Any):
    """
    Pomocná funkce pro ověření, že `get_args` vrátil právě dva vnořené typy (pro klíč a hodnotu slovníku).

    Používá se interně ve funkci `dictionary_validator`, kde slouží ke kontrole, že typová anotace
    odpovídá očekávanému formátu pro slovníky, tj. např. `dict[str, int]`, `Dict[CustomKey, CustomVal]` atd.

    Pokud `inner_args` neobsahuje právě dva typy, vyvolá specifickou výjimku `AnnotationDictArgsError`.

    Args:
        inner_args (Any): Výstup z `get_args()`, typicky dvojice typů pro klíč a hodnotu.

    Returns:
        Tuple[Any, Any]: Dvojice typů pro klíč a hodnotu.

    Raises:
        AnnotationDictArgsError: Pokud `inner_args` neobsahuje přesně dvě položky.
    """

    # Kontrola zda inner_args obsahuje pouze dvě položky
    if len(inner_args) == 2:
        return inner_args

    # Pokud ne, vyvolá se výjimka
    raise AnnotationDictArgsError(inner_args)