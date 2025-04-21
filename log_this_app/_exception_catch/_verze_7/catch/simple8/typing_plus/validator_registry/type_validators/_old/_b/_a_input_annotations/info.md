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

---

Myslím, že by dávalo smysl rozdělit tyto běžné typy na menší logické skupiny podle jejich vlastností a způsobu použití. 
Tady je návrh rozdělení:

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
   - `chain_map` - Řetězová mapa
   - `counter` - Počítadlo
   - `deque` - Oboustranná fronta
   - `default_dict` - Slovník s výchozí hodnotou
   - `ordered_dict` - Uspořádaný slovník

5. **Abstraktní typy kolekcí**
   - `sequence` - Abstraktní typ pro sekvence
   - `mutable_sequence` - Abstraktní typ pro měnitelné sekvence
   - `met` - Abstraktní typ pro množiny
   - `mutable_set` - Abstraktní typ pro měnitelné množiny
   - `mapping` - Abstraktní typ pro mapování
   - `mutable_mapping` - Abstraktní typ pro měnitelná mapování
   - `iterable` - Abstraktní typ pro objekty podporující iteraci
   - `collection` - Abstraktní typ pro kolekce
   - `container` - Abstraktní typ pro kontejnery

6. **Speciální kontejnery a kompozitní typy**
   - `optional` - Hodnota daného typu nebo None
   - `union` - Hodnota jednoho z několika typů
   - `any_str` - Generický typ pro str nebo bytes
   - `typed_dict` - Slovník s klíči specifických typů
   - `named_tuple` - Pojmenovaná n-tice s typovanými položkami

7. **Funkční typy**
   - `callable` - Funkce nebo jiný volatelný objekt

Toto rozdělení by ti mohlo pomoci systematicky zpracovávat podobné typy společně, 
protože typy v každé skupině budou pravděpodobně vyžadovat podobný přístup při validaci.