"""
Metaprogramming types:
→ Typy určené k práci s obecným programovým kódem a typovými anotacemi.
→ Používají se především v obecné (generické) programování a metaprogramování.
→ Typy v této kategorii obvykle:
    - Umožňují definovat vlastní generické typy (`Generic`, `TypeVar`).
    - Slouží k ověření typové hierarchie (`Type[T]`, `ClassVar[T]`).
    - Používají se při definování protokolů, generických tříd a složitějších typových anotací.
→ Příklady: `Type[T]`, `Generic`, `TypeVar`, `Concatenate[...]`, `ClassVar[T]`
"""

from ..type_validator_dataclass import TypeValidator
from ..verify import verify


VALIDATORS = {
    "type": TypeValidator(
        description="Validator for Type[T] types",
        validate_type=lambda value: isinstance(value, type),
        validate_items=lambda value, target_type: issubclass(value,
                                                             target_type),
    ),

    # [Generic] je jen pro definice tříd

    # [TypeVar] závisí na konkrétním typu dosazaném za TypeVar

}