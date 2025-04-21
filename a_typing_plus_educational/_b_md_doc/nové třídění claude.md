# Kompletní přehled anotací v knihovně typing

## 1. Běžné typy pro vstup i výstup

| Anotace | Popis |
|---------|-------|
| `bool` | Booleovská hodnota True/False |
| `int` | Celé číslo |
| `float` | Číslo s plovoucí desetinnou čárkou |
| `complex` | Komplexní číslo |
| `str` | Řetězec |
| `bytes` | Sekvence bajtů |
| `bytearray` | Měnitelná sekvence bajtů |
| `memoryview` | Pohled na paměť objektu typu bytes nebo bytearray |
| `list` | Seznam prvků, např. `list[int]` |
| `tuple` | N-tice prvků, např. `tuple[str, int]` nebo `tuple[int, ...]` |
| `set` | Množina prvků, např. `set[str]` |
| `frozenset` | Neměnitelná množina prvků, např. `frozenset[int]` |
| `dict` | Slovník, např. `dict[str, int]` |
| `Callable` | Funkce nebo jiný volatelný objekt, např. `Callable[[int, str], bool]` |
| `Sequence` | Abstraktní typ pro sekvence (list, tuple, str...) |
| `MutableSequence` | Abstraktní typ pro měnitelné sekvence (list, bytearray...) |
| `Set` | Abstraktní typ pro množiny (set, frozenset) |
| `MutableSet` | Abstraktní typ pro měnitelné množiny (set) |
| `Mapping` | Abstraktní typ pro mapování (dict, collections.defaultdict...) |
| `MutableMapping` | Abstraktní typ pro měnitelná mapování (dict) |
| `Iterable` | Abstraktní typ pro objekty podporující iteraci |
| `Collection` | Abstraktní typ pro kolekce (Sized + Iterable + Container) |
| `Container` | Abstraktní typ pro kontejnery (objekty podporující operátor `in`) |
| `Optional` | Hodnota daného typu nebo None, např. `Optional[int]` (ekvivalent k `int | None`) |
| `Union` | Hodnota jednoho z několika typů, např. `Union[int, str]` (ekvivalent k `int | str`) |
| `AnyStr` | Generický typ pro str nebo bytes |
| `TypedDict` | Slovník s klíči specifických typů |
| `NamedTuple` | Pojmenovaná n-tice s typovanými položkami |
| `ChainMap` | Řetězová mapa (collections.ChainMap) |
| `Counter` | Počítadlo (collections.Counter) |
| `Deque` | Oboustranná fronta (collections.deque) |
| `DefaultDict` | Slovník s výchozí hodnotou (collections.defaultdict) |
| `OrderedDict` | Uspořádaný slovník (collections.OrderedDict) |

## 2. Typy pro návratové hodnoty

| Anotace | Popis |
|---------|-------|
| `ContextManager` | Správce kontextu (objekt podporující `__enter__` a `__exit__`) |
| `AsyncContextManager` | Asynchronní správce kontextu |
| `Generator` | Generátor, např. `Generator[YieldType, SendType, ReturnType]` |
| `Iterator` | Iterátor, např. `Iterator[int]` |
| `AsyncIterator` | Asynchronní iterátor |
| `Awaitable` | Objekt podporující `await` |
| `Coroutine` | Korutina, např. `Coroutine[YieldType, SendType, ReturnType]` |
| `AsyncGenerator` | Asynchronní generátor |
| `AsyncIterable` | Objekt podporující asynchronní iteraci |

## 3. Typy pro dědění / tvorbu vlastních anotací

| Anotace | Popis |
|---------|-------|
| `Generic` | Základní třída pro definici generických tříd |
| `Protocol` | Definice protokolu (strukturální typování) |
| `runtime_checkable` | Dekorátor pro protokoly umožňující runtime kontroly pomocí `isinstance()` |
| `TypeVar` | Proměnná typu pro generické funkce a třídy |
| `ParamSpec` | Proměnná pro parametry funkce v generických anotacích |
| `Concatenate` | Spojení parametrů funkce s `ParamSpec` |
| `TypeVarTuple` | Variabilní počet typových proměnných |
| `Unpack` | Rozbalení `TypeVarTuple` nebo `tuple` typů |
| `dataclass_transform` | Dekorátor pro třídy, které se chovají jako dataclasses |
| `final` | Označení, že třída nebo metoda nemůže být dále podtřídou nebo přepsána |
| `override` | Označení, že metoda přepisuje metodu nadtřídy |
| `Self` | Typ vrácení odkazující na aktuální třídu |
| `ClassVar` | Třídní proměnná, ne instanční |
| `InitVar` | Parametr pouze pro `__init__` v dataclasses |
| `Supports*` | Protokoly pro specifické operace (např. `SupportsInt`, `SupportsFloat`) |
| `SupportsAbs` | Protokol pro objekty podporující `abs()` |
| `SupportsBytes` | Protokol pro objekty podporující `bytes()` |
| `SupportsComplex` | Protokol pro objekty podporující `complex()` |
| `SupportsFloat` | Protokol pro objekty podporující `float()` |
| `SupportsIndex` | Protokol pro objekty podporující `operator.index()` |
| `SupportsInt` | Protokol pro objekty podporující `int()` |
| `SupportsRound` | Protokol pro objekty podporující `round()` |

## 4. Pomocné konstrukce

| Anotace | Popis |
|---------|-------|
| `get_origin` | Získá původní typ z typové anotace (např. `list` z `list[int]`) |
| `get_args` | Získá argumenty typové anotace (např. `(int,)` z `list[int]`) |
| `get_type_hints` | Získá typové anotace ze zadané funkce nebo třídy |
| `cast` | Slouží pouze pro typovou kontrolu, nekonvertuje hodnoty |
| `NewType` | Vytvoří nový typ, který je podtypem existujícího typu |
| `TypeAlias` | Označení proměnné jako typového aliasu |
| `reveal_type` | Debugovací funkce pro odhalení odvozených typů |
| `assert_type` | Statická kontrola, že výraz má očekávaný typ |
| `ForwardRef` | Reference na typ, který ještě nebyl definován |
| `is_typeddict` | Kontrola, zda je typ `TypedDict` |
| `get_overloads` | Získání přetížených variant funkce |
| `clear_overloads` | Vyčištění zaregistrovaných přetížení |
| `dataclass_transform` | Dekorátor pro funkce, které vytvářejí třídy podobné dataclasses |
| `Alias` (Python 3.12+) | Vytvoření typového aliasu |

## 5. Speciální systémové typy

| Anotace | Popis |
|---------|-------|
| `Any` | Speciální typ kompatibilní s libovolným jiným typem |
| `NoReturn` | Typ pro funkce, které nikdy nevracejí hodnotu (vždy vyvolají výjimku) |
| `Never` | Typ, který nelze instancovat a nemá žádné hodnoty |
| `Type` | Typ třídy, např. `Type[int]` reprezentuje typ `int` samotný |
| `Literal` | Přesně specifikované hodnoty, např. `Literal[1, 2, 3]` |
| `Annotated` | Přidává metadata k typovým anotacím, např. `Annotated[int, "pozitivní"]` |
| `Final` | Označení, že proměnná nemůže být přiřazena jinde v kódu |
| `Required` | Označení povinného klíče v TypedDict |
| `NotRequired` | Označení nepovinného klíče v TypedDict |
| `LiteralString` | Řetězec známý v době překladu |
| `Unpack` | Rozbalení typových argumentů |
| `TypeGuard` | Označení funkce pro typové zúžení |
| `Doc` (PEP 727) | Dokumentace typů |
| `@deprecated` | Označení zastaralého API |
| `@override` | Označení metody přepisující metodu nadtřídy |

---

Myslím, že by dávalo smysl rozdělit tyto běžné typy na menší logické skupiny podle jejich vlastností a způsobu použití. Tady je návrh rozdělení:

1. **Základní skalární typy**
   - `bool` - Booleovská hodnota
   - `int` - Celé číslo
   - `float` - Číslo s plovoucí desetinnou čárkou
   - `complex` - Komplexní číslo
   - `str` - Řetězec

2. **Binární typy**
   - `bytes` - Sekvence bajtů
   - `bytearray` - Měnitelná sekvence bajtů
   - `memoryview` - Pohled na paměť objektu typu bytes nebo bytearray

3. **Standardní kolekce**
   - `list` - Seznam prvků
   - `tuple` - N-tice prvků
   - `set` - Množina prvků
   - `frozenset` - Neměnitelná množina prvků
   - `dict` - Slovník

4. **Kolekce z modulu collections**
   - `ChainMap` - Řetězová mapa
   - `Counter` - Počítadlo
   - `Deque` - Oboustranná fronta
   - `DefaultDict` - Slovník s výchozí hodnotou
   - `OrderedDict` - Uspořádaný slovník

5. **Abstraktní typy kolekcí**
   - `Sequence` - Abstraktní typ pro sekvence
   - `MutableSequence` - Abstraktní typ pro měnitelné sekvence
   - `Set` - Abstraktní typ pro množiny
   - `MutableSet` - Abstraktní typ pro měnitelné množiny
   - `Mapping` - Abstraktní typ pro mapování
   - `MutableMapping` - Abstraktní typ pro měnitelná mapování
   - `Iterable` - Abstraktní typ pro objekty podporující iteraci
   - `Collection` - Abstraktní typ pro kolekce
   - `Container` - Abstraktní typ pro kontejnery

6. **Speciální kontejnery a kompozitní typy**
   - `Optional` - Hodnota daného typu nebo None
   - `Union` - Hodnota jednoho z několika typů
   - `AnyStr` - Generický typ pro str nebo bytes
   - `TypedDict` - Slovník s klíči specifických typů
   - `NamedTuple` - Pojmenovaná n-tice s typovanými položkami

7. **Funkční typy**
   - `Callable` - Funkce nebo jiný volatelný objekt

Toto rozdělení by ti mohlo pomoci systematicky zpracovávat podobné typy společně, protože typy v každé skupině budou pravděpodobně vyžadovat podobný přístup při validaci.