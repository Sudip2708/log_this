def verify_container_items(value, types, container_type):
    """
    Metoda pro ověření:

    list: `List[T]` | Seznam prvků typu `T`
    tuple: `Tuple[T, ...]` | N-tice prvků různých typů
    set: `Set[T]` | Množina prvků typu `T`
    frozenset: `FrozenSet[T]` | Neměnná množina prvků typu `T`
    deque: `Deque[T]` | Obojesměrný seznam (`collections.deque`)
    """
    if container_type in {list, tuple, set, frozenset, deque}:
        for item in value:
            verify(item, inner_types[0])


def verify_list_container_items(value: list, inner_types: tuple) -> bool:
    """Ověří, zda všechny prvky v seznamu odpovídají očekávaným typům."""

    # Kontrola zda seznam obsahuje pouze jednu položku
    if len(inner_types) != 1:
        raise TypeError("List nemůže obsahovat více různých typů v definici")

    expected_type = inner_types[0]

    # Varianta 1: List[str] nebo List[int] (obyčejný typ)
    if isinstance(expected_type, type):
        return all(isinstance(item, expected_type) for item in value)

    # Varianta 2: List[Union[str, int, ...]] (Union s více typy)
    elif get_origin(expected_type) is Union:
        allowed_types = get_args(expected_type)
        return all(isinstance(item, allowed_types) for item in value)

    return False


"""
| Typ | Popis |
|------|------------------------------------|
#| `List[T]` | Seznam prvků typu `T` |
| `Dict[K, V]` | Slovník s klíči typu `K` a hodnotami typu `V` |
#| `Tuple[T, ...]` | N-tice prvků různých typů |
#| `Set[T]` | Množina prvků typu `T` |
#| `FrozenSet[T]` | Neměnná množina prvků typu `T` |
#| `Deque[T]` | Obojesměrný seznam (`collections.deque`) |
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
"""

"""
| Typ | Ověření typu | Ověření vnitřních položek |
List[T] | isinstance(value, list) | isinstance(item, T) for item in value
Dict[K, V]
Tuple[T, ...]
Set[T]
FrozenSet[T]
Deque[T]
DefaultDict[K, V]
OrderedDict[K, V]
ChainMap[K, V]
Counter[T]
NamedTuple
TypedDict
Protocol
Literal[...]
Type[T]
Final
Concatenate[...]


Any
Union[T1, T2] = any(validate(value, t) for t in args)
Optional[T]
Callable[..., T]
NoReturn
ClassVar[T]
Self
Never

"""