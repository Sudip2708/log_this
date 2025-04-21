### Další skupiny "alike" validátorů

Zde jsou návrhy pro další skupiny "alike" validátorů, které by mohly být v knihovně:

0. **dict_alike** - validátory pro kontejnery podobné slovníkům:
   - `Dict[K, V]` - Nejběžnější a nejpoužívanější slovníkový typ.
   - `DefaultDict[K, V]` - Užitečný pro eliminaci kontrol existence klíče a pro skupinování dat.
   - `OrderedDict[K, V]` - Užitečný, když záleží na pořadí vkládání prvků.
   - `Mapping[K, V]` - Akceptuje jakýkoliv objekt, který implementuje rozhraní slovníku.
   - `MutableMapping[K, V]` - Vhodné pro parametry funkcí, kde potřebujeme číst i zapisovat.
   - `Counter[T]` - Speciální slovník pro počítání výskytů prvků.
   - `ChainMap[K, V]` - Poskytuje pohled na několik slovníků jako na jeden.
   - `TypedDict` - Na rozdíl od Dict[K, V] umožňuje mít různé typy pro různé klíče.
   - `UserDict` - Základní třída pro vytváření vlastních implementací slovníků.

1. **list_alike** - validátory pro kontejnery podobné seznamům:
   - `List[T]` - základní list
   - `Sequence[T]` - čtecí sekvence
   - `MutableSequence[T]` - zapisovací sekvence
   - `Deque[T]` - oboustranná fronta
   - `UserList` - základ pro vlastní implementace seznamů

2. **set_alike** - validátory pro množinové typy:
   - `Set[T]` - základní set
   - `FrozenSet[T]` - neměnný set
   - `AbstractSet[T]` - rozhraní pro množiny
   - `MutableSet[T]` - měnitelné množiny

3. **tuple_alike** - validátory pro n-tice:
   - `Tuple[T, ...]` - homogenní n-tice libovolné délky
   - `Tuple[T1, T2, ...]` - heterogenní n-tice (s rozdílnými typy)
   - `NamedTuple` - pojmenované n-tice

4. **union_alike** - validátory pro sjednocení typů:
   - `Union[T1, T2, ...]` - sjednocení typů
   - `Optional[T]` - volitelný typ (Union[T, None])
   - `Literal[values...]` - jeden z konkrétních literálů

5. **callable_alike** - validátory pro volatelné objekty:
   - `Callable[[Args...], Return]` - funkce/metody
   - `Protocol` - strukturální typování

6. **container_alike** - obecné kontejnery:
   - `Container[T]` - kontejner s operací `in`
   - `Collection[T]` - kombinace Container, Iterable, Sized
   - `Iterable[T]` - objekt, který lze iterovat
   - `Iterator[T]` - iterátor
   - `Sized` - objekt s metodou `__len__`
   - `Reversible[T]` - objekt, který lze procházet opačně

7. **async_alike** - validátory pro asynchronní typy:
   - `Coroutine[T_co, T_contra, V_co]` - korutina
   - `AsyncIterable[T]` - async iterovatelný objekt
   - `AsyncIterator[T]` - async iterátor
   - `Awaitable[T]` - cokoliv, co lze použít s await

8. **io_alike** - validátory pro IO operace:
   - `IO[AnyStr]` - obecný vstup/výstup
   - `TextIO` - textový vstup/výstup
   - `BinaryIO` - binární vstup/výstup

9. **type_alike** - validátory pro generická a meta-typování:
   - `Type[T]` - typ třídy
   - `ClassVar[T]` - třídní proměnná
   - `Final[T]` - konečný, neměnitelný typ
   - `Generic[T]` - základ pro generické typy
   - `TypeVar` - typová proměnná
   - `NewType` - vytvoření nového typu

10. **contextmanager_alike** - validátory pro kontextové manažery:
    - `ContextManager[T]` - kontextový manažer (`with` statement)
    - `AsyncContextManager[T]` - asynchronní kontextový manažer

Tato organizace podle "alike" skupin by měla přehledně pokrýt většinu typových anotací z modulu `typing` a umožní tak systematický vývoj validátorů.