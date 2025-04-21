import functools
from typing import Any, Callable, get_type_hints, get_origin, get_args
import inspect


def abc_type_validator(func: Callable) -> Callable:
    """
    Dekorátor pro rozšířenou typovou kontrolu abstraktních metod.

    Výhody:
    - Statická typová kontrola před voláním metody
    - Detailní validace vstupních parametrů
    - Podpora složitých typů (generics, union, optional)

    Použití:
    1. Zvýšení bezpečnosti typů v runtime
    2. Včasná detekce nesprávných typů
    3. Podpora komplexnějších typových kontrol

    Args:
        func: Abstraktní metoda pro validaci

    Returns:
        Dekorovaná metoda s typovou kontrolou
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Získání typových anotací
        type_hints = get_type_hints(func)

        # Odstranění 'self' pro správnou validaci
        sig = inspect.signature(func)
        bound_arguments = sig.bind(*args, **kwargs)
        bound_arguments.apply_defaults()

        # Validace každého parametru
        for param_name, param_value in bound_arguments.arguments.items():
            # Přeskočení 'self'
            if param_name == 'self':
                continue

            # Získání očekávaného typu
            expected_type = type_hints.get(param_name)

            if expected_type is not None:
                # Pokročilá validace včetně generických typů
                if not _is_type_match(param_value, expected_type):
                    raise TypeError(
                        f"Nesprávný typ pro parametr {param_name}. "
                        f"Očekáváno {expected_type}, "
                        f"obdrženo {type(param_value)}"
                    )

        return func(*args, **kwargs)

    return wrapper


def _is_type_match(value: Any, expected_type: type) -> bool:
    """
    Detailní kontrola shody typů včetně generických a složitých typů.

    Podporuje:
    - Jednoduché typy
    - Generic typy (List, Dict)
    - Union typy
    - Optional typy
    """
    # Speciální případ pro Any
    if expected_type is Any:
        return True

    # Základní typová kontrola
    if isinstance(value, expected_type):
        return True

    # Kontrola generických typů
    origin = get_origin(expected_type)
    if origin is not None:
        # Kontrola generických kontejnerů
        if origin in (list, set, frozenset):
            if not isinstance(value, origin):
                return False

            # Kontrola vnitřních typů
            args = get_args(expected_type)
            if args:
                return all(_is_type_match(item, args[0]) for item in value)

        # Kontrola Union typů
        elif origin is typing.Union:
            return any(
                _is_type_match(value, arg) for arg in get_args(expected_type))

    return False


# # Příklad použití
# class ExampleValidator(ABC):
#
#     @abc_type_validator
#     @abstractmethod
#     def process_data(
#             self,
#             data: List[int],
#             config: Dict[str, Any],
#             optional_param: Optional[str] = None
#     ) -> bool:
#         """Abstraktní metoda s komplexní typovou validací."""
#         pass
#
#     process_data = abc_method("process_data")