"""
Container types:
→ Reprezentují datové struktury, které obsahují více prvků a umožňují jejich organizaci a manipulaci.
→ Patří sem běžné datové typy jako seznamy (list), n-tice (tuple), množiny (set, frozenset) a slovníky (dict).
→ Typy v této kategorii obvykle:
    - Umožňují iteraci přes prvky.
    - Mají metody pro vkládání, mazání nebo přístup k hodnotám.
    - Mohou obsahovat homogenní nebo heterogenní prvky.
→ Příklady: `List[T]`, `Dict[K, V]`, `Tuple[...]`, `Set[T]`, `FrozenSet[T]`
"""

from ..type_validator_dataclass import TypeValidator
from ..verify import verify


VALIDATORS = {
    "list": TypeValidator(
        description="Validator for List[T] types",
        validate_type=lambda value: isinstance(value, list),
        validate_items=lambda value, item_type, deep_check: (
            all(
                verify(item, item_type, deep_check)
                for item in value
            )
        )
    ),
    "dict": TypeValidator(
        description="Validator for Dict[K, V] types",
        validate_type=lambda value: isinstance(value, dict),
        validate_items=lambda value, key_type, value_type, deep_check: (
            all(
                verify(k, key_type, deep_check)
                and verify(v, value_type, deep_check)
                for k, v in value.items()
            )
        ),

    ),
    "tuple": TypeValidator(
        description="Validator for Tuple[...] types",
        validate_type=lambda value: isinstance(value, tuple),
        validate_items=lambda value, args, deep_check: (
            # Ověření pro Tuple[T, ...] (homogenní n-tice)
            all(
                verify(item, args, deep_check)
                for item in value
            )
            if not isinstance(args, tuple) and not isinstance(args, list)
            # Ověření pro Tuple[T1, T2, ...] (heterogenní n-tice)
            else len(value) == len(args) and all(
                verify(value[i], args[i], deep_check)
                for i in range(len(args))
            )
        ),
    ),
    "set": TypeValidator(
        description="Validator for Set[T] types",
        validate_type=lambda value: isinstance(value, set),
        validate_items=lambda value, item_type, deep_check: (
            all(
                verify(item, item_type, deep_check)
                for item in value
            )
        ),
    ),
    "frozenset": TypeValidator(
        description="Validator for FrozenSet[T] types",
        validate_type=lambda value: isinstance(value, frozenset),
        validate_items=lambda value, item_type, deep_check: (
            all(
                verify(item, item_type, deep_check)
                for item in value
            )
        ),
    ),
}