from collections import deque  # deque
from collections import defaultdict  # defaultdict
from collections import OrderedDict  # ordereddict
from collections import ChainMap  # chainmap
from collections import Counter  # counter
from collections.abc import Sequence as SequenceABC  # sequence
from collections.abc import Mapping as MappingABC  # mapping
from collections.abc import MutableMapping as MutableMappingABC  # mutablemapping
from collections.abc import Iterable as IterableABC  # iterable
from collections.abc import Iterator as IteratorABC  # iterator
from collections.abc import Generator as GeneratorABC  # generator
import inspect  # coroutine

def verify(*args):
    pass

VALIDATORS = {
    list: TypeValidator(
        description="Validator for List[T] types",
        validate_type=lambda value: isinstance(value, list),
        validate_items=lambda value, item_type, deep_check: (
            all(
                verify(item, item_type, deep_check)
                for item in value
            )
        )
    ),
    dict: TypeValidator(
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
    tuple: TypeValidator(
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
    set: TypeValidator(
        description="Validator for Set[T] types",
        validate_type=lambda value: isinstance(value, set),
        validate_items=lambda value, item_type, deep_check: (
            all(
                verify(item, item_type, deep_check)
                for item in value
            )
        ),
    ),
    frozenset: TypeValidator(
        description="Validator for FrozenSet[T] types",
        validate_type=lambda value: isinstance(value, frozenset),
        validate_items=lambda value, item_type, deep_check: (
            all(
                verify(item, item_type, deep_check)
                for item in value
            )
        ),
    ),
    deque: TypeValidator(
        description="Validator for Deque[T] types (from collections import deque)",
        validate_type=lambda value: isinstance(value, deque),
        validate_items=lambda value, item_type, deep_check: (
            all(
                verify(item, item_type, deep_check)
                for item in value
            )
        ),

    ),
    defaultdict: TypeValidator(
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
    ordereddict: TypeValidator(
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
    chainmap: TypeValidator(
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
    counter: TypeValidator(
        description="Validator for Counter[T] types (from collections import Counter)",
        validate_type=lambda value: isinstance(value, Counter),
        validate_items=lambda value, key_type, deep_check: (
            all(
                verify(k, key_type, deep_check)
                for k in value
            )
        ),
    ),

    # Zde ChatGPT končí a přidává už jen Any a Callable

    # [NamedTuple] je složitější, protože potřebujeme přístup k anotacím
    # Je nutné implementovat speciální validaci

    # [TypedDict] je také složitější kvůli potřebě přístupu k definici

    # [Protocol] vyžaduje strukturální ověření

    literal: TypeValidator(
        description="Validator for Literal[...] types",
        validate_type=lambda value: True,  # Bude ověřeno v SPECIAL_VALIDATORS
    ),
    type: TypeValidator(
        description="Validator for Type[T] types",
        validate_type=lambda value: isinstance(value, type),
        validate_items=lambda value, target_type: issubclass(value, target_type),
    ),
    final: TypeValidator(
        description="Validator for Final[T] types",
        validate_type=lambda value: True,  # Bude delegováno na vnitřní typ
        validate_items=lambda value, inner_type, deep_check: (
            verify(value, inner_type, deep_check)
        ),
    ),

    # Concatenate[...]

    any: TypeValidator(
        description="Validator for Any[...] type (always valid)",
        validate_type=lambda value: True,
        validate_items=lambda value: True,
    ),

    # Union[T1, T2, ...]  potřebují speciální zpracování

    # Optional[T] potřebují speciální zpracování

    callable: TypeValidator(
        description="Validator for Callable[..., R] types",
        validate_type=lambda value: callable(value),
        # Ověření signatury a návratového typu by vyžadovalo introspekci funkcí
        validate_items=lambda value, return_type, deep_check: True,  # Signatura se neověřuje
    ),
    noreturn: TypeValidator(
        description="Validator for NoReturn type (never valid)",
        validate_type=lambda value: False,  # NoReturn nikdy neplatí
        validate_items=lambda value: False,  # NoReturn nikdy neplatí
    ),
    classvar: TypeValidator(
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

    # [Generic] je jen pro definice tříd

    # [TypeVar] závisí na konkrétním typu dosazaném za TypeVar

    anystr: TypeValidator(
        description="Validator for AnyStr type",
        validate_type=lambda value: isinstance(value, (str, bytes)),
    ),
    sequence: TypeValidator(
        description="Validator for Sequence[T] types (from collections.abc import Sequence as SequenceABC)",
        validate_type=lambda value: isinstance(value, SequenceABC),
        validate_items=lambda value, item_type, deep_check: (
            all(
                verify(item, item_type, deep_check)
                for item in value
            )
        ),
    ),
    mapping: TypeValidator(
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
    mutablemapping: TypeValidator(
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
    iterable: TypeValidator(
        description="Validator for Iterable[T] types (from collections.abc import Iterable as IterableABC)",
        validate_type=lambda value: isinstance(value, IterableABC),
        # Pozor: Spotřebuje iteraci, vhodné jen pro deep_check=False nebo pro kopírovatelné iterovatelné objekty
        validate_items=lambda value, item_type, deep_check: (
            False if deep_check else True
        ),  # Při deep_check raději neověřovat, aby se nespotřebovala iterace
    ),
    iterator: TypeValidator(
        description="Validator for Iterator[T] types (from collections.abc import Iterator as IteratorABC)",
        validate_type=lambda value: isinstance(value, IteratorABC),
        # Pozor: Spotřebuje iteraci, raději neověřovat vnitřní hodnoty
        validate_items=lambda value, item_type, deep_check: (
            False if deep_check else True
        ),  # Při deep_check raději neověřovat, aby se nespotřebovala iterace
    ),

    # [AsyncIterable] vyžaduje asynchronní zpracování: isinstance(value, collections.abc.AsyncIterable)

    # [AsyncIterator] vyžaduje asynchronní zpracování: isinstance(value, collections.abc.AsyncIterator)

    generator: TypeValidator(
        description="Validator for Generator[Y, S, R] types (from collections.abc import Generator as GeneratorABC)",
        validate_type=lambda value: isinstance(value, GeneratorABC),
        # Ověření yield/send/return typů je složité, raději neověřovat vnitřní hodnoty
        validate_items=lambda value, yield_type, send_type, return_type, deep_check: (
            False if deep_check else True
        ),
    ),
    coroutine: TypeValidator(
        description="Validator for Coroutine[Y, S, R] types (import inspect)",
        validate_type=lambda value: inspect.iscoroutine(value),
        # Ověření běhu korutiny je složité, raději neověřovat vnitřní hodnoty
    ),
    contextmanager: TypeValidator(
        description="Validator for ContextManager[T] types",
        validate_type=lambda value: hasattr(value, "__enter__")
                                    and hasattr(value, "__exit__"),
        # Ověření návratové hodnoty __enter__ by vyžadovalo spuštění kontextového manažeru
    ),
    asyncContextmanager: TypeValidator(
        description="Validator for AsyncContextManager[T] types",
        validate_type=lambda value: hasattr(value, "__aenter__")
                                    and hasattr(value, "__aexit__"),
        # Vyžaduje asynchronní zpracování
    ),

}

