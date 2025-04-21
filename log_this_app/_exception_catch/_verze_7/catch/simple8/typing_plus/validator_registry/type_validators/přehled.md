# **Přehled knihovny `typing`**

## **1. Typové anotace (použitelné přímo v anotacích)**

### 1.1 Primitivní a speciální typy

| Typ                  | Význam                         | Příklad použití              |
|----------------------|--------------------------------|-------------------------------|
| `Any`                | libovolný typ                  | `def f(x: Any): ...`         |
| `None`               | žádná hodnota                  | `def f() -> None: ...`       |
| `NoReturn`           | funkce nikdy nevrací           | `def f() -> NoReturn: ...`   |
| `Literal[...]`       | konkrétní hodnota/y            | `x: Literal["a", "b"]`       |
| `Final`              | neměnný atribut                | `x: Final[int] = 42`         |
| `ClassVar[...]`      | class-level atribut            | `x: ClassVar[int]`           |
| `Type[X]`            | typ třídy, ne instance         | `cls: Type[MyClass]`         |
| `Self` *(3.11+)*     | odkaz na instanci třídy        | `def clone(self) -> Self:`   |

---

### 1.2 Kolekce a kontejnery

| Typ                  | Význam                         | Příklad použití              |
|----------------------|--------------------------------|-------------------------------|
| `List[X]`            | seznam                         | `List[int]`                  |
| `Tuple[X, Y]`        | n-tice                         | `Tuple[int, str]`           |
| `Set[X]`             | množina                        | `Set[str]`                   |
| `Dict[K, V]`         | slovník                        | `Dict[str, int]`            |
| `FrozenSet[X]`       | neměnná množina                | `FrozenSet[int]`            |
| `Deque[X]`           | fronta z `collections`         | `Deque[str]`                |
| `DefaultDict[K, V]`  | slovník s výchozími hodnotami  | `DefaultDict[str, int]`     |
| `OrderedDict[K, V]`  | pořadí zachováno               | `OrderedDict[str, int]`     |

---

### 1.3 Abstraktní kolekce a iterace

| Typ                  | Význam                         | Příklad použití              |
|----------------------|--------------------------------|-------------------------------|
| `Iterable[X]`        | cokoliv iterovatelného         | `Iterable[int]`             |
| `Iterator[X]`        | iterátor                       | `Iterator[int]`             |
| `Sequence[X]`        | posloupnost                    | `Sequence[str]`             |
| `Mapping[K, V]`      | mapování                       | `Mapping[str, int]`         |
| `MutableMapping[K, V]`| měnitelné mapování            | `MutableMapping[str, int]`  |
| `Container[X]`       | `in` operátor podporován       | `Container[str]`            |
| `Reversible[X]`      | má `__reversed__`              | `Reversible[int]`           |

---

### 1.4 Funkce a výrazy

| Typ                  | Význam                         | Příklad použití              |
|----------------------|--------------------------------|-------------------------------|
| `Callable[[A1, A2], R]` | volatelný objekt             | `Callable[[int, str], bool]`|
| `Concatenate[...]`   | při kombinaci s `ParamSpec`    | `Concatenate[int, str]`     |
| `ParamSpec`          | typ pro argumenty funkce       | viz generické použití        |

---

### 1.5 Složené a logické typy

| Typ                  | Význam                         | Příklad použití              |
|----------------------|--------------------------------|-------------------------------|
| `Union[X, Y]`        | buď X nebo Y                   | `Union[int, str]`            |
| `Optional[X]`        | X nebo None                    | `Optional[int]`              |
| `Annotated[X, ...]`  | dodatečné metadata             | `Annotated[int, Range(0,10)]`|
| `Literal[...]`       | výčet hodnot                   | `Literal["GET", "POST"]`     |

---

## **2. Tvorba nových typů a generika**

| Typ                   | Význam                         | Příklad použití              |
|-----------------------|--------------------------------|-------------------------------|
| `NewType(name, type)` | nový typ, alias                | `UserId = NewType("UserId", int)` |
| `TypeVar("T")`        | obecný typ                     | `T = TypeVar("T")`           |
| `Generic[T]`          | generická třída                | `class Box(Generic[T]): ...` |
| `Protocol`            | strukturální typování          | `class Sized(Protocol): ...` |
| `TypedDict`           | typovaný dict                  | `class Point(TypedDict): x: int; y: int` |
| `Required`, `NotRequired` | pro volitelné klíče v `TypedDict` | `name: Required[str]`     |

---

## **3. Introspekce a runtime analýza typů**

| Funkce / nástroj       | Význam                         | Příklad použití              |
|------------------------|--------------------------------|-------------------------------|
| `get_type_hints(obj)`  | získá anotace jako dict        | `get_type_hints(f)`          |
| `get_origin(tp)`       | získá základní typ             | `get_origin(List[int]) == list` |
| `get_args(tp)`         | získá argumenty                | `get_args(Dict[str, int])`   |
| `is_typeddict(cls)`    | je `TypedDict`?                | `is_typeddict(MyTD)`         |
| `is_protocol(cls)`     | je `Protocol`?                 | `is_protocol(MyProto)`       |
| `ForwardRef`           | dopředné typy                  | `ForwardRef("MyClass")`      |

---

## **4. Typy pro statickou kontrolu a validaci**

| Typ                    | Význam                         | Příklad použití              |
|------------------------|--------------------------------|-------------------------------|
| `assert_type(value, type)` | kontrola při vývoji (ne běhu) | `assert_type(x, int)`     |
| `TypeGuard[X]`         | zúžení typu v podmínce         | `def is_str_list(x) -> TypeGuard[list[str]]:` |
| `Never` *(3.11+)*      | nemožný návrat                 | `def f() -> Never: ...`      |
| `Unpack[...]` *(3.11+)*| rozbalení typu                 | `Callable[[Unpack[Ts]], R]`  |

---

## **5. `typing_extensions` – rozšíření a kompatibilita**

| Typ / nástroj           | Důvod použití                 | Poznámka                    |
|-------------------------|-------------------------------|-----------------------------|
| `Literal`, `Final`, `Annotated`, `Self`, `NotRequired`, `Required`, `Unpack`, `TypeAliasType` | zpětná kompatibilita | pokud cílíš na <3.9 |
| `assert_type()`         | statická kontrola při vývoji  | nefunguje za běhu           |

---

## **6. Interní atributy typových objektů (pro hlubší analýzu)**

| Atribut                 | Význam                         | Příklad                     |
|-------------------------|--------------------------------|-----------------------------|
| `__origin__`            | základní typ (alternativa k `get_origin`) | `List[int].__origin__ == list` |
| `__args__`              | parametry                      | `Dict[str, int].__args__`  |
| `__annotations__`       | slovník anotací                | `obj.__annotations__`       |
| `__parameters__`, `__bound__`, `__constraints__` | u `TypeVar` a generik       | pokročilé použití           |

---

