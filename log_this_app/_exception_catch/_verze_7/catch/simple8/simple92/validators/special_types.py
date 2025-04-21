"""
Special types:
→ Typy sloužící k lepší typové anotaci, strukturování dat nebo speciálním účelům.
→ Jsou součástí modulů `typing` a `types` a umožňují lepší práci s typy v Pythonu.
→ Typy v této kategorii obvykle:
    - Reprezentují specifické datové struktury (`NamedTuple`, `TypedDict`).
    - Umožňují flexibilní typové anotace (`Union[T1, T2, ...]`, `Optional[T]`, `Literal[...]`).
    - Slouží pro specifické scénáře (`Final`, `NoReturn`, `Self`).
→ Příklady: `NamedTuple`, `TypedDict`, `Union[T1, T2, ...]`, `Optional[T]`, `Callable[..., R]`, `Literal[...]`, `Final`, `NoReturn`
"""

from ..type_validator_dataclass import TypeValidator
from ..verify import verify


VALIDATORS = {
    # [NamedTuple] je složitější, protože potřebujeme přístup k anotacím
    # Je nutné implementovat speciální validaci

    # [TypedDict] je také složitější kvůli potřebě přístupu k definici

    # [Protocol] vyžaduje strukturální ověření

    "literal": TypeValidator(
        description="Validator for Literal[...] types",
        validate_type=lambda value: True,  # Bude ověřeno v SPECIAL_VALIDATORS
    ),
    "final": TypeValidator(
        description="Validator for Final[T] types",
        validate_type=lambda value: True,  # Bude delegováno na vnitřní typ
        validate_items=lambda value, inner_type, deep_check: (
            verify(value, inner_type, deep_check)
        ),
    ),

    # Concatenate[...]

    "any": TypeValidator(
        description="Validator for Any[...] type (always valid)",
        validate_type=lambda value: True,
        validate_items=lambda value: True,
    ),

    # Union[T1, T2, ...]  potřebují speciální zpracování

    # Optional[T] potřebují speciální zpracování

    "callable": TypeValidator(
        description="Validator for Callable[..., R] types",
        validate_type=lambda value: callable(value),
        # Ověření signatury a návratového typu by vyžadovalo introspekci funkcí
        validate_items=lambda value, return_type, deep_check: True,
        # Signatura se neověřuje
    ),
    "noreturn": TypeValidator(
        description="Validator for NoReturn type (never valid)",
        validate_type=lambda value: False,  # NoReturn nikdy neplatí
        validate_items=lambda value: False,  # NoReturn nikdy neplatí
    ),
    "classvar": TypeValidator(
        description="Validator for ClassVar[T] types",
        validate_type=lambda value: True,  # Bude delegováno na vnitřní typ
        validate_items=lambda value, inner_type, deep_check: (
            verify(value, inner_type, deep_check)
        ),
    ),

    # [Self] vyžaduje znalost aktuální třídy: isinstance(value, aktuální třída)

    # [NewType] vyžaduje přístup k základnímu typu: ověřit základní typ | stejné jako pro základní typ

    annotated: TypeValidator(
        description="Validator for Annotated[T, ...] types",
        validate_type=lambda value: True,  # Bude delegováno na vnitřní typ
        validate_items=lambda value, inner_type, deep_check: (
            verify(value, inner_type[0], deep_check)
        ),
    ),
    "anystr": TypeValidator(
        description="Validator for AnyStr type",
        validate_type=lambda value: isinstance(value, (str, bytes)),
    ),

}