"""
Collections:
→ Rozšiřují běžné kontejnery o pokročilejší funkcionalitu nebo specifické chování.
→ Jsou součástí modulu `collections` a poskytují efektivnější správu dat.
→ Typy v této kategorii obvykle:
    - Jsou optimalizované pro specifické operace (např. `Deque[T]` pro rychlé vkládání/mazání z obou stran).
    - Rozšiřují funkcionalitu běžných kontejnerů (`DefaultDict[K, V]`, `OrderedDict[K, V]`).
    - Mají speciální chování, např. počítání výskytů (`Counter[T]`) nebo kombinaci více slovníků (`ChainMap[K, V]`).
→ Příklady: `Deque[T]`, `DefaultDict[K, V]`, `OrderedDict[K, V]`, `ChainMap[K, V]`, `Counter[T]`
"""

from collections import deque  # deque
from collections import defaultdict  # defaultdict
from collections import OrderedDict  # ordereddict
from collections import ChainMap  # chainmap
from collections import Counter  # counter

from ..type_validator_dataclass import TypeValidator
from ..verify import verify


VALIDATORS = {
    "deque": TypeValidator(
        description="Validator for Deque[T] types (from collections import deque)",
        validate_type=lambda value: isinstance(value, deque),
        validate_items=lambda value, item_type, deep_check: (
            all(
                verify(item, item_type, deep_check)
                for item in value
            )
        ),

    ),
    "defaultdict": TypeValidator(
        description="Validator for DefaultDict[K, V] types (from collections import defaultdict)",
        validate_type=lambda value: isinstance(value, defaultdict),
        validate_items=lambda value, key_type, value_type, deep_check: (
            all(
                verify(k, key_type, deep_check)
                and verify(v, value_type, deep_check)
                for k, v in value.items()
            )
        ),
    ),
    "ordereddict": TypeValidator(
        description="Validator for OrderedDict[K, V] types (from collections import OrderedDict)",
        validate_type=lambda value: isinstance(value, OrderedDict),
        validate_items=lambda value, key_type, value_type, deep_check: (
            all(
                verify(k, key_type, deep_check)
                and verify(v, value_type, deep_check)
                for k, v in value.items()
            )
        ),
    ),
    "chainmap": TypeValidator(
        description="Validator for ChainMap[K, V] types (from collections import ChainMap)",
        validate_type=lambda value: isinstance(value, ChainMap),
        validate_items=lambda value, key_type, value_type, deep_check: (
            all(
                verify(k, key_type, deep_check)
                and verify(map_item[k], value_type, deep_check)
                for map_item in value.maps for k in map_item
            )
        ),
    ),
    "counter": TypeValidator(
        description="Validator for Counter[T] types (from collections import Counter)",
        validate_type=lambda value: isinstance(value, Counter),
        validate_items=lambda value, key_type, deep_check: (
            all(
                verify(k, key_type, deep_check)
                for k in value
            )
        ),
    ),
}