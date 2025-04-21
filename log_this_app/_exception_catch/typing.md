### **📌 Přehled knihovny `typing` v Pythonu**

---

## **1️⃣ Generické typy**
| Typ | Popis |
|------|------------------------------------|
| `List[T]` | Seznam prvků typu `T` |
| `Dict[K, V]` | Slovník s klíči typu `K` a hodnotami typu `V` |
| `Tuple[T, ...]` | N-tice prvků různých typů |
| `Set[T]` | Množina prvků typu `T` |
| `FrozenSet[T]` | Neměnná množina prvků typu `T` |
| `Deque[T]` | Obojesměrný seznam (`collections.deque`) |
| `DefaultDict[K, V]` | Slovník s výchozí hodnotou (`collections.defaultdict`) |
| `OrderedDict[K, V]` | Seřazený slovník (`collections.OrderedDict`) |
| `ChainMap[K, V]` | Kombinace více slovníků (`collections.ChainMap`) |
| `Counter[T]` | Počítadlo výskytů (`collections.Counter`) |
| `NamedTuple` | Strukturovaná pojmenovaná n-tice |
| `TypedDict` | Slovník s pevně danými typy hodnot |
| `Protocol` | Rozhraní pro strukturované typování |
| `Literal[...]` | Omezí hodnotu na konkrétní výčtové hodnoty |
| `Type[T]` | Odkaz na třídu typu `T` |
| `Final` | Označuje neměnné atributy nebo třídy |
| `Concatenate[...]` | Používá se při `Callable` pro spojení argumentů |

---

## **2️⃣ Speciální konstrukce (`Union`, `Optional`, …)**
| Typ | Popis |
|------|-------------------------------------|
| `Any` | Může být jakýkoli typ |
| `Union[T1, T2]` | Může být jakýkoli z uvedených typů |
| `Optional[T]` | Buď `T`, nebo `None` (ekvivalent `Union[T, None]`) |
| `Callable[..., T]` | Odkaz na funkci s návratovým typem `T` |
| `NoReturn` | Označuje, že funkce nikdy nevrátí hodnotu |
| `ClassVar[T]` | Atribut třídy, nikoli instance |
| `Self` | Odkaz na instanci v rámci třídy (od Pythonu 3.11) |
| `Never` | Označuje, že kód by nikdy neměl být dosažen (od Pythonu 3.11) |

---

## **3️⃣ Nativní typy Pythonu**
| Typ | Popis |
|------|---------------------------------|
| `int` | Celé číslo |
| `float` | Desetinné číslo |
| `complex` | Komplexní číslo |
| `bool` | Boolean (True/False) |
| `str` | Řetězec |
| `bytes` | Bajtové pole |
| `bytearray` | Mutovatelné bajtové pole |
| `memoryview` | Pohled na paměť |
| `list` | Seznam prvků |
| `tuple` | N-tice prvků |
| `set` | Množina |
| `frozenset` | Neměnná množina |
| `dict` | Slovník klíč-hodnota |
| `range` | Sekvence čísel |
| `NoneType` | Typ `None` |
| `EllipsisType` | Typ `...` (ellipsis) |

---

## **4️⃣ Metody knihovny `typing`**
| Metoda | Popis |
|----------------|-------------------------------------------------------------|
| `get_origin(T)` | Vrátí základní typ generického typu (např. `list` pro `List[int]`) |
| `get_args(T)` | Vrátí argumenty generického typu (např. `(int,)` pro `List[int]`) |
| `cast(T, obj)` | Přetypování objektu (neovlivňuje runtime, pouze statickou analýzu) |
| `isinstance(obj, T)` | Ověření instance proti typové anotaci (dostupné od Pythonu 3.10) |
| `issubclass(cls, T)` | Ověření dědičnosti proti typové anotaci (dostupné od Pythonu 3.10) |
| `reveal_type(obj)` | Debugovací nástroj, zobrazí detekovaný typ v `mypy` |
| `NewType(name, type)` | Vytvoří nový podtyp existujícího typu |
| `TypeGuard[T]` | Označuje funkci, která slouží jako typový strážce (Python 3.10+) |

---

### **📌 Co s tím můžeš dělat?**
💡 Tohle je kompletní přehled všeho, co knihovna `typing` nabízí. Můžeš se k tomu kdykoli vrátit, když budeš potřebovat zjistit, co použít pro typovou kontrolu.  

🔥 **Chceš k tomu ještě něco přidat nebo rozšířit nějakou sekci?** 😊