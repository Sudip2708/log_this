"""
ABC types (Abstract Base Classes):
→ Obecné rozhraní pro datové typy, které definují jejich chování pomocí abstraktních metod.
→ Nachází se v modulu `collections.abc` a určují "smluvní chování" různých typů.
→ Typy v této kategorii obvykle:
    - Nejsou přímo implementované, ale slouží k validaci nebo dědičnosti.
    - Umožňují ověřit kompatibilitu objektů s určitými vlastnostmi (`isinstance(value, Iterable)`).
    - Definují rozhraní pro iteraci, mapování, sekvence atd.
→ Příklady: `Sequence[T]`, `Mapping[K, V]`, `MutableMapping[K, V]`, `Iterable[T]`, `Iterator[T]`, `Generator[Y, S, R]`
"""

from collections.abc import Sequence as SequenceABC  # sequence
from collections.abc import Mapping as MappingABC  # mapping
from collections.abc import MutableMapping as MutableMappingABC  # mutablemapping
from collections.abc import Iterable as IterableABC  # iterable
from collections.abc import Iterator as IteratorABC  # iterator
from collections.abc import Generator as GeneratorABC  # generator

from ..type_validator_dataclass import TypeValidator
from ..verify import verify


VALIDATORS = {
    "sequence": TypeValidator(
        description="Validator for Sequence[T] types (from collections.abc import Sequence as SequenceABC)",
        validate_type=lambda value: isinstance(value, SequenceABC),
        validate_items=lambda value, item_type, deep_check: (
            all(
                verify(item, item_type, deep_check)
                for item in value
            )
        ),
    ),
    "mapping": TypeValidator(
        description="Validator for Mapping[K, V] types (from collections.abc import Mapping as MappingABC)",
        validate_type=lambda value: isinstance(value, MappingABC),
        validate_items=lambda value, key_type, value_type, deep_check: (
            all(
                verify(k, key_type, deep_check)
                and verify(value[k], value_type, deep_check)
                for k in value
            )
        ),
    ),
    "mutablemapping": TypeValidator(
        description="Validator for MutableMapping[K, V] types (from collections.abc import MutableMapping as MutableMappingABC)",
        validate_type=lambda value: isinstance(value, MutableMappingABC),
        validate_items=lambda value, key_type, value_type, deep_check: (
            all(
                verify(k, key_type, deep_check)
                and verify(value[k], value_type, deep_check)
                for k in value
            )
        ),
    ),
    "iterable": TypeValidator(
        description="Validator for Iterable[T] types (from collections.abc import Iterable as IterableABC)",
        validate_type=lambda value: isinstance(value, IterableABC),
        # Pozor: Spotřebuje iteraci, vhodné jen pro deep_check=False nebo pro kopírovatelné iterovatelné objekty
        validate_items=lambda value, item_type, deep_check: (
            False if deep_check else True
        ),  # Při deep_check raději neověřovat, aby se nespotřebovala iterace
    ),
    "iterator": TypeValidator(
        description="Validator for Iterator[T] types (from collections.abc import Iterator as IteratorABC)",
        validate_type=lambda value: isinstance(value, IteratorABC),
        # Pozor: Spotřebuje iteraci, raději neověřovat vnitřní hodnoty
        validate_items=lambda value, item_type, deep_check: (
            False if deep_check else True
        ),  # Při deep_check raději neověřovat, aby se nespotřebovala iterace
    ),

    # [AsyncIterable] vyžaduje asynchronní zpracování: isinstance(value, collections.abc.AsyncIterable)

    # [AsyncIterator] vyžaduje asynchronní zpracování: isinstance(value, collections.abc.AsyncIterator)

    "generator": TypeValidator(
        description="Validator for Generator[Y, S, R] types (from collections.abc import Generator as GeneratorABC)",
        validate_type=lambda value: isinstance(value, GeneratorABC),
        # Ověření yield/send/return typů je složité, raději neověřovat vnitřní hodnoty
        validate_items=lambda value, yield_type, send_type, return_type,
                              deep_check: (
            False if deep_check else True
        ),
    ),
    "coroutine": TypeValidator(
        description="Validator for Coroutine[Y, S, R] types (import inspect)",
        validate_type=lambda value: inspect.iscoroutine(value),
        # Ověření běhu korutiny je složité, raději neověřovat vnitřní hodnoty
    ),
    "contextmanager": TypeValidator(
        description="Validator for ContextManager[T] types",
        validate_type=lambda value: hasattr(value, "__enter__")
                                    and hasattr(value, "__exit__"),
        # Ověření návratové hodnoty __enter__ by vyžadovalo spuštění kontextového manažeru
    ),
    "asynccontextmanager": TypeValidator(
        description="Validator for AsyncContextManager[T] types",
        validate_type=lambda value: hasattr(value, "__aenter__")
                                    and hasattr(value, "__aexit__"),
        # Vyžaduje asynchronní zpracování
    ),
}