from typing import Any, get_args

from .._exceptions import VerifyGetArgumentsError
from ..._exceptions_base import VerifyUnexpectedInternalError


def get_args_safe(annotation: Any):
    """
    Pomocná interní funkce pro bezpečné získání vnitřních typových anotací pomocí `get_args()`.

    Používá se ve validačních funkcích `iterable_validator` a `dictionary_validator`, kde slouží
    k získání typů obsažených v generických anotacích jako `List[int]`, `Dict[str, float]`, `tuple[str, int]` atd.

    Funkce bezpečně zachytává výjimku `TypeError`, která může vzniknout při volání `get_args()`
    na nekompatibilní typy, a převádí ji na specializovanou výjimku `AnnotationGetArgsError`.

    Args:
        annotation (Any): Typová anotace, z níž se mají získat vnitřní typy.

    Returns:
        Tuple[Any, ...]: N-tice typů extrahovaných z anotace.

    Raises:
        AnnotationGetArgsError: Pokud se nepodaří z anotace získat vnitřní typy pomocí `get_args()`.
    """

    # Pokus zda get_atrs nevyvolá výjimku
    try:
        return get_args(annotation)

    # Pokud ano, převede se na interní výjimku
    except TypeError as e:
        raise VerifyGetArgumentsError(annotation) from e

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e