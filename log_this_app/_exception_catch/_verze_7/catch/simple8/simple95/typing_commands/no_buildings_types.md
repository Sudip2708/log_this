# Tabulka typových anotací z modulu typing

|Kategorie|Typ|Popis|Příklad použití|
|---------|---|-----|---------------|
|Obecné obálky|Any|Libovolný typ|`Any`|
|Obecné obálky|NoReturn|Funkce nikdy nevrátí hodnotu (vyvolá výjimku nebo nekonečná smyčka)|`def exit() -> NoReturn:`|
|Obecné obálky|Never|Označení kódu, který nikdy nebude dosažen|`def never_called() -> Never:`|
|Obecné obálky|TypeAlias|Explicitní označení typových aliasů|`Vector: TypeAlias = list[float]`|
|Obecné obálky|TypeGuard|Pro funkce, které provádějí typovou kontrolu|`def is_str(val: Any) -> TypeGuard[str]:`|
|Složení typů|Union|Více typů současně|`Union[int, str]` nebo `int | str` (Python 3.10+)|
|Složení typů|Optional|Zkrácený zápis Union[X, None]|`Optional[str]` nebo `str | None` (Python 3.10+)|
|Složení typů|Annotated|Typ s dodatečnou informací|`Annotated[int, "Popis"]`|
|Složení typů|Literal|Předdefinovaná množina hodnot|`Literal["a", "b", "c"]`|
|Složení typů|Final|Neměnitelná hodnota|`Final[int]`|
|Složení typů|ClassVar|Proměnná třídy, ne instance|`ClassVar[int]`|
|Složení typů|Required|Pro požadované klíče v TypedDict|`class User(TypedDict): name: Required[str]`|
|Složení typů|NotRequired|Pro volitelné klíče v TypedDict|`class User(TypedDict): age: NotRequired[int]`|
|Složení typů|Unpack|Pro rozbalení TypedDict nebo tuple|`def f(**kwargs: Unpack[Options]): ...`|
|Generika / parametry|TypeVar|Parametrizovaný typ|`T = TypeVar("T")`|
|Generika / parametry|ParamSpec|Parametrizovaný typ pro parametry funkce|`P = ParamSpec("P")`|
|Generika / parametry|TypeVarTuple|Variabilní počet typových parametrů|`Ts = TypeVarTuple("Ts")`|
|Generika / parametry|Generic|Základ pro tvorbu obecných tříd|`class MyBox(Generic[T]):`|
|Generika / parametry|Protocol|Strukturální typování|`class Serializable(Protocol):`|
|Generika / parametry|NewType|Alias na jiný typ|`UserId = NewType("UserId", int)`|
|Generika / parametry|Concatenate|Pro částečnou aplikaci parametrů funkce|`def partial(f: Callable[Concatenate[int, P], T])`|
|Sekvence / Kolekce|Iterable, Iterator|Sekvence / iterátory|`Iterable[int]`|
|Sekvence / Kolekce|Sequence|Nepřepisovatelná sekvence|`Sequence[str]`|
|Sekvence / Kolekce|MutableSequence|Přepisovatelná sekvence|`MutableSequence[str]`|
|Sekvence / Kolekce|Mapping|Obecný slovník|`Mapping[str, int]`|
|Sekvence / Kolekce|MutableMapping|Přepisovatelný slovník|`MutableMapping[str, int]`|
|Sekvence / Kolekce|Container|Obecný kontejner (testovatelný operátorem `in`)|`Container[int]`|
|Sekvence / Kolekce|Collection|Velikost + iterace + obsahuje|`Collection[str]`|
|Sekvence / Kolekce|Hashable|Hashovatelná hodnota|`Hashable`|
|Sekvence / Kolekce|Sized|Má délku (velikost)|`Sized`|
|Sekvence / Kolekce|Counter|Počítadlo výskytů|`Counter[str]`|
|Sekvence / Kolekce|Deque|Oboustranná fronta|`Deque[int]`|
|Sekvence / Kolekce|ChainMap|Řetězení více mapování|`ChainMap[str, int]`|
|Volání/funkce|Callable|Funkce|`Callable[[int], str]`|
|Volání/funkce|Awaitable|Hodnota čekatelná pomocí await|`Awaitable[int]`|
|Volání/funkce|Coroutine|Korutina|`Coroutine[Any, Any, int]`|
|Volání/funkce|AsyncIterable, AsyncIterator|Asynchronní iterátory|`AsyncIterable[str]`|
|Volání/funkce|AsyncContextManager|Asynchronní kontextový manažer|`AsyncContextManager[int]`|
|Volání/funkce|ContextManager|Kontextový manažer|`ContextManager[int]`|
|Speciální kontejnery|TypedDict|Slovník s typovanými klíči|`class User(TypedDict): name: str`|
|Speciální kontejnery|NamedTuple|Pojmenovaná n-tice|`class Point(NamedTuple): x: int; y: int`|
|Speciální kontejnery|LiteralString|Řetězec známý v době překladu|`def query(sql: LiteralString): ...`|
|Odkazy a introspekce|ForwardRef|Odkaz na typ definovaný později|`List["MyClass"]`|
|Odkazy a introspekce|Self|Odkaz na vlastní třídu|`def copy(self) -> Self:`|
|Odkazy a introspekce|Type|Typ třídy|`Type[User]`|
|Odkazy a introspekce|Deprecated|Označení zastaralé funkce/třídy|`@deprecated(message="...")`|
|Odkazy a introspekce|reveal_type|Zobrazení typu v IDE/typové kontrole|`reveal_type(x)  # Není skutečná funkce`|