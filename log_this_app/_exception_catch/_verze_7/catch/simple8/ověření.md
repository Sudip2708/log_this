Doplním tabulku s pravidly pro ověřování podle vzoru a přidám další relevantní typy z knihovny `typing`. Zde je kompletní tabulka:

| Typ | Ověření typu | Ověření vnitřních položek |
|-----|--------------|----------------------------|
| List[T] | isinstance(value, list) | isinstance(item, T) for item in value |
| Dict[K, V] | isinstance(value, dict) | isinstance(key, K) and isinstance(value[key], V) for key in value |
| Tuple[T1, T2, ...] | isinstance(value, tuple) and len(value) == len(args) | isinstance(value[i], args[i]) for i in range(len(args)) |
| Tuple[T, ...] | isinstance(value, tuple) | isinstance(item, T) for item in value |
| Set[T] | isinstance(value, set) | isinstance(item, T) for item in value |
| FrozenSet[T] | isinstance(value, frozenset) | isinstance(item, T) for item in value |
| Deque[T] | isinstance(value, collections.deque) | isinstance(item, T) for item in value |
| DefaultDict[K, V] | isinstance(value, collections.defaultdict) | isinstance(key, K) and isinstance(value[key], V) for key in value |
| OrderedDict[K, V] | isinstance(value, collections.OrderedDict) | isinstance(key, K) and isinstance(value[key], V) for key in value |
| ChainMap[K, V] | isinstance(value, collections.ChainMap) | all(isinstance(key, K) and isinstance(map_item[key], V) for map_item in value.maps for key in map_item) |
| Counter[T] | isinstance(value, collections.Counter) | isinstance(key, T) for key in value |
| NamedTuple | isinstance(value, tuple) and hasattr(value, '_fields') | ověřit typy jednotlivých položek podle anotací |
| TypedDict | isinstance(value, dict) | ověřit typy klíčů a hodnot podle definice TypedDict |
| Protocol | hasattr(value, všechny potřebné metody/atributy) | N/A (protokoly jsou strukturální typy) |
| Literal[...] | value in (literální hodnoty) | N/A |
| Type[T] | isinstance(value, type) a issubclass(value, T) | N/A |
| Final | ověřit základní typ T v Final[T] | stejné jako pro T |
| Concatenate[...] | N/A (pouze pro typy funkcí) | N/A |
| Any | True (vždy platné) | N/A |
| Union[T1, T2, ...] | any(verify(value, T) for T in args) | závisí na konkrétním typu, který byl vyhodnocen jako platný |
| Optional[T] | value is None or verify(value, T) | stejné jako pro T, pokud hodnota není None |
| Callable[..., R] | callable(value) | případně ověřit signaturu a návratový typ R |
| NoReturn | False (nikdy neplatné) | N/A |
| ClassVar[T] | ověřit základní typ T | stejné jako pro T |
| Self | isinstance(value, aktuální třída) | N/A |
| NewType | ověřit základní typ | stejné jako pro základní typ |
| Annotated[T, ...] | ověřit základní typ T | stejné jako pro T |
| Generic | N/A (jen pro definice tříd) | N/A |
| TypeVar | závisí na konkrétním typu dosazaném za TypeVar | závisí na konkrétním typu |
| AnyStr | isinstance(value, (str, bytes)) | N/A |
| Sequence[T] | isinstance(value, collections.abc.Sequence) | isinstance(item, T) for item in value |
| Mapping[K, V] | isinstance(value, collections.abc.Mapping) | isinstance(key, K) and isinstance(value[key], V) for key in value |
| MutableMapping[K, V] | isinstance(value, collections.abc.MutableMapping) | isinstance(key, K) and isinstance(value[key], V) for key in value |
| Iterable[T] | isinstance(value, collections.abc.Iterable) | isinstance(item, T) for item in value (POZOR: spotřebuje iteraci) |
| Iterator[T] | isinstance(value, collections.abc.Iterator) | isinstance(next(value), T) (POZOR: spotřebuje iteraci) |
| AsyncIterable[T] | isinstance(value, collections.abc.AsyncIterable) | vyžaduje async ověření |
| AsyncIterator[T] | isinstance(value, collections.abc.AsyncIterator) | vyžaduje async ověření |
| Generator[Y, S, R] | isinstance(value, collections.abc.Generator) | složité ověření návratových/yield hodnot |
| Coroutine[Y, S, R] | inspect.iscoroutine(value) | složité ověření návratových hodnot |
| ContextManager[T] | hasattr(value, '__enter__') and hasattr(value, '__exit__') | ověřit návratovou hodnotu __enter__ |
| AsyncContextManager[T] | hasattr(value, '__aenter__') and hasattr(value, '__aexit__') | vyžaduje async ověření |

Pár poznámek k implementaci:

1. Pro složené typy jako `Union`, `Optional` atd. je potřeba rekurzivní ověření.
2. Pro typy jako `Iterator`, `Generator` apod. je problém, že ověření obsahu by spotřebovalo iteraci, což by mohlo být nežádoucí.
3. Pro `Protocol` a strukturální typy je ověření složitější - je potřeba zkontrolovat všechny požadované metody a atributy.
4. Pro asynchronní typy je nutné speciální zacházení.
