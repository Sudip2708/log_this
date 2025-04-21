# Hlavní slovník validátorů
VALIDATORS = {
    list: TypeValidator(
        validate_type=lambda value: isinstance(value, list),
        validate_items=lambda value, item_type, deep_check: all(verify(item, item_type, deep_check) for item in value),
        description="Validator for list types"
    ),
    List: TypeValidator(
        validate_type=lambda value: isinstance(value, list),
        validate_items=lambda value, item_type, deep_check: all(verify(item, item_type, deep_check) for item in value),
        description="Validator for List[T] types"
    ),
    dict: TypeValidator(
        validate_type=lambda value: isinstance(value, dict),
        validate_items=lambda value, key_type, value_type, deep_check: all(
            verify(k, key_type, deep_check) and verify(v, value_type,
                                                       deep_check)
            for k, v in value.items()
        ),
        description="Validator for dictionary types"
    ),
    Dict: TypeValidator(
        validate_type=lambda value: isinstance(value, dict),
        validate_items=lambda value, key_type, value_type, deep_check: all(
            verify(k, key_type, deep_check) and verify(v, value_type,
                                                       deep_check)
            for k, v in value.items()
        ),
        description="Validator for Dict[K, V] types"
    ),
    tuple: TypeValidator(
        validate_type=lambda value: isinstance(value, tuple),
        validate_items=lambda value, args, deep_check:
        # Pro Tuple[T, ...] (homogenní n-tice)
        all(verify(item, args, deep_check) for item in value)
        if not isinstance(args, tuple) and not isinstance(args, list) else
        # Pro Tuple[T1, T2, ...] (heterogenní n-tice)
        len(value) == len(args) and all(
            verify(value[i], args[i], deep_check) for i in range(len(args))),
        description="Validator for tuple types"
    ),
    Tuple: TypeValidator(
        validate_type=lambda value: isinstance(value, tuple),
        validate_items=lambda value, args, deep_check:
        # Pro Tuple[T, ...] (homogenní n-tice)
        all(verify(item, args, deep_check) for item in value)
        if not isinstance(args, tuple) and not isinstance(args, list) else
        # Pro Tuple[T1, T2, ...] (heterogenní n-tice)
        len(value) == len(args) and all(
            verify(value[i], args[i], deep_check) for i in range(len(args))),
        description="Validator for Tuple[...] types"
    ),
    set: TypeValidator(
        validate_type=lambda value: isinstance(value, set),
        validate_items=lambda value, item_type, deep_check: all(
            verify(item, item_type, deep_check) for item in value),
        description="Validator for set types"
    ),
    Set: TypeValidator(
        validate_type=lambda value: isinstance(value, set),
        validate_items=lambda value, item_type, deep_check: all(
            verify(item, item_type, deep_check) for item in value),
        description="Validator for Set[T] types"
    ),
    frozenset: TypeValidator(
        validate_type=lambda value: isinstance(value, frozenset),
        validate_items=lambda value, item_type, deep_check: all(
            verify(item, item_type, deep_check) for item in value),
        description="Validator for frozenset types"
    ),
    FrozenSet: TypeValidator(
        validate_type=lambda value: isinstance(value, frozenset),
        validate_items=lambda value, item_type, deep_check: all(
            verify(item, item_type, deep_check) for item in value),
        description="Validator for FrozenSet[T] types"
    ),
    deque: TypeValidator(
        validate_type=lambda value: isinstance(value, deque),
        validate_items=lambda value, item_type, deep_check: all(
            verify(item, item_type, deep_check) for item in value),
        description="Validator for deque types"
    ),
    defaultdict: TypeValidator(
        validate_type=lambda value: isinstance(value, defaultdict),
        validate_items=lambda value, key_type, value_type, deep_check: all(
            verify(k, key_type, deep_check) and verify(v, value_type,
                                                       deep_check)
            for k, v in value.items()
        ),
        description="Validator for defaultdict types"
    ),
    OrderedDict: TypeValidator(
        validate_type=lambda value: isinstance(value, OrderedDict),
        validate_items=lambda value, key_type, value_type, deep_check: all(
            verify(k, key_type, deep_check) and verify(v, value_type,
                                                       deep_check)
            for k, v in value.items()
        ),
        description="Validator for OrderedDict types"
    ),
    ChainMap: TypeValidator(
        validate_type=lambda value: isinstance(value, ChainMap),
        validate_items=lambda value, key_type, value_type, deep_check: all(
            verify(k, key_type, deep_check) and verify(map_item[k], value_type,
                                                       deep_check)
            for map_item in value.maps for k in map_item
        ),
        description="Validator for ChainMap types"
    ),
    Counter: TypeValidator(
        validate_type=lambda value: isinstance(value, Counter),
        validate_items=lambda value, key_type, deep_check: all(
            verify(k, key_type, deep_check) for k in value),
        description="Validator for Counter types"
    ),
    # NamedTuple je složitější, protože potřebujeme přístup k anotacím
    # Je nutné implementovat speciální validaci

    # TypedDict je také složitější kvůli potřebě přístupu k definici

    # Protocol vyžaduje strukturální ověření

    Literal: TypeValidator(
        validate_type=lambda value: True,  # Bude ověřeno v SPECIAL_VALIDATORS
        description="Validator for Literal types"
    ),
    Type: TypeValidator(
        validate_type=lambda value: isinstance(value, type),
        validate_items=lambda value, target_type, deep_check: issubclass(value,
                                                                         target_type),
        description="Validator for Type[T] types"
    ),
    Final: TypeValidator(
        validate_type=lambda value: True,  # Bude delegováno na vnitřní typ
        validate_items=lambda value, inner_type, deep_check: verify(value,
                                                                    inner_type,
                                                                    deep_check),
        description="Validator for Final types"
    ),
    Any: TypeValidator(
        validate_type=lambda value: True,
        description="Validator for Any type (always valid)"
    ),
    # Union a Optional potřebují speciální zpracování

    Callable: TypeValidator(
        validate_type=lambda value: callable(value),
        # Ověření signatury a návratového typu by vyžadovalo introspekci funkcí
        description="Validator for Callable types"
    ),
    NoReturn: TypeValidator(
        validate_type=lambda value: False,  # NoReturn nikdy neplatí
        description="Validator for NoReturn type (never valid)"
    ),
    ClassVar: TypeValidator(
        validate_type=lambda value: True,  # Bude delegováno na vnitřní typ
        validate_items=lambda value, inner_type, deep_check: verify(value,
                                                                    inner_type,
                                                                    deep_check),
        description="Validator for ClassVar types"
    ),
    # Self vyžaduje znalost aktuální třídy

    # NewType vyžaduje přístup k základnímu typu

    Annotated: TypeValidator(
        validate_type=lambda value: True,  # Bude delegováno na vnitřní typ
        validate_items=lambda value, inner_type, deep_check: verify(value,
                                                                    inner_type[
                                                                        0],
                                                                    deep_check),
        description="Validator for Annotated types"
    ),
    # Generic je jen pro definice tříd

    # TypeVar závisí na konkrétním typu

    AnyStr: TypeValidator(
        validate_type=lambda value: isinstance(value, (str, bytes)),
        description="Validator for AnyStr type"
    ),
    Sequence: TypeValidator(
        validate_type=lambda value: isinstance(value, SequenceABC),
        validate_items=lambda value, item_type, deep_check: all(
            verify(item, item_type, deep_check) for item in value),
        description="Validator for Sequence types"
    ),
    Mapping: TypeValidator(
        validate_type=lambda value: isinstance(value, MappingABC),
        validate_items=lambda value, key_type, value_type, deep_check: all(
            verify(k, key_type, deep_check) and verify(value[k], value_type,
                                                       deep_check)
            for k in value
        ),
        description="Validator for Mapping types"
    ),
    MutableMapping: TypeValidator(
        validate_type=lambda value: isinstance(value, MutableMappingABC),
        validate_items=lambda value, key_type, value_type, deep_check: all(
            verify(k, key_type, deep_check) and verify(value[k], value_type,
                                                       deep_check)
            for k in value
        ),
        description="Validator for MutableMapping types"
    ),
    Iterable: TypeValidator(
        validate_type=lambda value: isinstance(value, IterableABC),
        # Pozor: Spotřebuje iteraci, vhodné jen pro deep_check=False nebo pro kopírovatelné iterovatelné objekty
        validate_items=lambda value, item_type, deep_check: (
            False if deep_check else True
        ),  # Při deep_check raději neověřovat, aby se nespotřebovala iterace
        description="Validator for Iterable types"
    ),
    Iterator: TypeValidator(
        validate_type=lambda value: isinstance(value, IteratorABC),
        # Pozor: Spotřebuje iteraci, raději neověřovat vnitřní hodnoty
        validate_items=lambda value, item_type,
                              deep_check: False if deep_check else True,
        description="Validator for Iterator types"
    ),
    # AsyncIterable a AsyncIterator vyžadují asynchronní zpracování

    Generator: TypeValidator(
        validate_type=lambda value: isinstance(value, GeneratorABC),
        # Ověření yield/send/return typů je složité, raději neověřovat vnitřní hodnoty
        validate_items=lambda value, yield_type, send_type, return_type,
                              deep_check: False if deep_check else True,
        description="Validator for Generator types"
    ),
    Coroutine: TypeValidator(
        validate_type=lambda value: inspect.iscoroutine(value),
        # Ověření běhu korutiny je složité, raději neověřovat vnitřní hodnoty
        description="Validator for Coroutine types"
    ),
    ContextManager: TypeValidator(
        validate_type=lambda value: hasattr(value, "__enter__") and hasattr(
            value, "__exit__"),
        # Ověření návratové hodnoty __enter__ by vyžadovalo spuštění kontextového manažeru
        description="Validator for ContextManager types"
    ),
    AsyncContextManager: TypeValidator(
        validate_type=lambda value: hasattr(value, "__aenter__") and hasattr(
            value, "__aexit__"),
        # Vyžaduje asynchronní zpracování
        description="Validator for AsyncContextManager types"
    ),
}