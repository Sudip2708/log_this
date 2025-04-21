Tady je upravená tabulka s přidaným třetím sloupcem `get_origin(Typ)`:  

| Typ | Kategorie | `get_origin(Typ)` |
|-------------------------|----------------------|-------------------|
| `List[T]` | Container types | `list` |
| `Dict[K, V]` | Container types | `dict` |
| `Tuple[T1, T2, ...]` | Container types | `tuple` |
| `Tuple[T, ...]` | Container types | `tuple` |
| `Set[T]` | Container types | `set` |
| `FrozenSet[T]` | Container types | `frozenset` |
| `Deque[T]` | Collections | `collections.deque` |
| `DefaultDict[K, V]` | Collections | `collections.defaultdict` |
| `OrderedDict[K, V]` | Collections | `collections.OrderedDict` |
| `ChainMap[K, V]` | Collections | `collections.ChainMap` |
| `Counter[T]` | Collections | `collections.Counter` |
| `NamedTuple` | Special types | `None` |
| `TypedDict` | Special types | `None` |
| `Protocol` | Special types | `None` |
| `Literal[...]` | Special types | `None` |
| `Type[T]` | Metaprogramming types | `type` |
| `Final` | Special types | `None` |
| `Concatenate[...]` | Special types | `None` |
| `Any` | Special types | `None` |
| `Union[T1, T2, ...]` | Special types | `Union` |
| `Optional[T]` | Special types | `Union` (což je `Union[T, None]`) |
| `Callable[..., R]` | Special types | `collections.abc.Callable` |
| `NoReturn` | Special types | `None` |
| `ClassVar[T]` | Special types | `None` |
| `Self` | Special types | `None` |
| `NewType` | Special types | `None` |
| `Annotated[T, ...]` | Special types | `typing.Annotated` |
| `Generic` | Metaprogramming types | `None` |
| `TypeVar` | Metaprogramming types | `None` |
| `AnyStr` | Special types | `None` |
| `Sequence[T]` | ABC types | `collections.abc.Sequence` |
| `Mapping[K, V]` | ABC types | `collections.abc.Mapping` |
| `MutableMapping[K, V]` | ABC types | `collections.abc.MutableMapping` |
| `Iterable[T]` | ABC types | `collections.abc.Iterable` |
| `Iterator[T]` | ABC types | `collections.abc.Iterator` |
| `AsyncIterable[T]` | ABC types | `collections.abc.AsyncIterable` |
| `AsyncIterator[T]` | ABC types | `collections.abc.AsyncIterator` |
| `Generator[Y, S, R]` | ABC types | `collections.abc.Generator` |
| `Coroutine[Y, S, R]` | ABC types | `collections.abc.Coroutine` |
| `ContextManager[T]` | ABC types | `contextlib.AbstractContextManager` |
| `AsyncContextManager[T]` | ABC types | `contextlib.AbstractAsyncContextManager` |

💡 **Vysvětlení `get_origin(Typ)`**:
- Vrací základní třídu (např. `list` pro `List[T]`).
- U některých speciálních typů (`Union`, `Optional`, `Annotated`) vrací odpovídající `typing` typ.
- Pro většinu speciálních typů (`NamedTuple`, `Final`, `Protocol`, `Any`, ...) vrací `None`, protože nejsou generické.

Je to takto v pořádku? 😊