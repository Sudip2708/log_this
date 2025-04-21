Ahojky Dalibore 😊

Skvělé zadání – přesně takhle se člověk opravdu ponoří do typovacích možností Pythonu a knihovny `typing`. Jdeme na to postupně.

---

## 🔸 Předdefinované symboly

```python
native_type = (int, str, bool, float, complex, bytes, None, ...)  # nativní typy
generative_container = (List, Set, Tuple, Dict, FrozenSet, Deque, Iterable, Sequence, Mapping, ...)  # generativní kontejnery
```

---

## 🔹 Platné (a smysluplné) kombinace s `List`

```python
# 1. Prázdný List (není validní pro mypy, ale běží v runtime)
List  # nebo List[Any]

# 2. List s jedním nativním typem
List[native_type]

# 3. List s Union více nativních typů
List[Union[native_type, native_type]]

# 4. List s Union více libovolných typů (včetně generativních)
List[Union[native_type, generative_container[native_type]]]

# 5. List s Any (bez specifikace typu)
List[Any]

# 6. List s vnořeným Listem
List[List[native_type]]
List[List[Union[native_type, generative_container[Any]]]]

# 7. List s jiným generativním kontejnerem
List[Set[native_type]]
List[Tuple[native_type, ...]]
List[Dict[native_type, native_type]]
List[Deque[native_type]]
List[Sequence[native_type]]

# 8. Kombinace více generativních kontejnerů uvnitř Listu
List[Tuple[native_type, List[native_type]]]
List[Dict[str, List[Tuple[native_type, Set[native_type]]]]]

# 9. List s Optional
List[Optional[native_type]]
List[Optional[generative_container[native_type]]]

# 10. List s Literal (pro omezené hodnoty)
List[Literal["a", "b", "c"]]

# 11. List s Annotated
List[Annotated[native_type, "description"]]

# 12. List s Callable
List[Callable[[native_type], generative_container[native_type]]]

# 13. List s NewType nebo TypeVar
List[MyCustomType]  # MyCustomType = NewType("MyCustomType", str)
List[TypeVar("T")]

# 14. List se Self nebo ForwardRef (užitečné např. u tříd, které odkazují samy na sebe)
List["MyClass"]
```

---

## 🔸 Nevalidní / problematické

```python
# Nevalidní v `List`: více parametrů
List[native_type, native_type]  # ❌ List může mít jen 1 typ (není jako Tuple)

# List s elipsou bez Tuple
List[native_type, ...]  # ❌ Elipsa se používá pouze v Tuple (Tuple[int, ...])
```

---

## ✅ Shrnutí

### `List` z `typing` podporuje:

- **1 parametr** – `List[T]`, kde `T` může být:
  - `native_type`
  - `Union[...]`
  - `Optional[...]`
  - `Any`
  - `List[...]` (rekurze)
  - `generative_container[...]`
  - `Tuple[...]`, `Dict[...]`, `Set[...]`, atd.
  - `Callable[...]`, `Annotated[...]`, `Literal[...]`, `TypeVar`, `ForwardRef`

### Nepodporuje:

- **Více parametrů**: `List[int, str]` ❌
- **Elipsy mimo Tuple**: `List[int, ...]` ❌

---

Chceš, abych ti to převedl i do tabulky nebo vygeneroval validní příklady automaticky (např. skriptem)? Mohl bych ti i pomoci udělat testovací sadu pro `mypy`.

---

Skvělý postřeh, Dalibore! 😊  
Teď se tedy zaměříme **výhradně na všechny možné (smysluplné a povolené) typy**, které **nejsou ani nativní typy**, ani generativní kontejnery, a které lze použít uvnitř `List[...]`.

---

## 🔸 Pravidla pro výběr

> **Vyřazujeme**:
- `native_type = (int, str, bool, float, None, ...)`
- `generative_container = (List, Set, Dict, Tuple, FrozenSet, Deque, Mapping, Iterable, ...)`

> **Zůstávají**:
- Typové konstrukty, aliasy a metatypy, které jsou **logické, funkcionální, abstraktní nebo obalující**.

---

## 🔹 Platné a logické typy v `List[...]`, které nejsou `native_type` ani `generative_container`

```python
List[Any]                       # univerzální typ, cokoliv
List[Union[int, str]]          # unie více typů
List[Optional[int]]            # Optional je alias pro Union[X, None]
List[Literal["a", "b", 1]]     # omezený výčet hodnot
List[Annotated[int, "meta"]]   # typ s dodatečnou anotací
List[Callable[[int], str]]     # funkce s typy argumentů a návratovou hodnotou
List[TypeVar("T")]             # generický typový parametr
List[Final[int]]               # konstantní hodnota
List[ClassVar[int]]            # proměnná třídy (většinou jen v rámci datových tříd)
List[ForwardRef("MyClass")]    # odkazy na budoucí definici
List["MyClass"]                # běžný stringový forward ref
List[NewType("UserId", int)]   # vlastní typ alias
```

---

## 🔸 Shrnutí v seznamu

Zde je čistý výpis těch “nenativních a negenerativních” prvků, které jsou validní uvnitř `List[...]`:

```python
logical_special_types = (
    Any,
    Union,
    Optional,
    Literal,
    Annotated,
    Callable,
    TypeVar,
    Final,
    ClassVar,
    ForwardRef,
    str,        # při použití forward reference: List["SomeType"]
    NewType     # při použití: MyAlias = NewType("MyAlias", int)
)
```

> ⚠️ **Poznámka**:
> - `str` zde neznamená nativní typ, ale stringový název typu – tzv. **forward reference**.
> - `NewType(...)` vrací funkci, takže v praxi bys měl vytvořit alias:
>   ```python
>   UserId = NewType("UserId", int)
>   List[UserId]
>   ```

---

## 🔹 Chceš výstup i v JSON nebo jako malý Python parser?

Můžu ti snadno vyrobit třeba `List[<typ>]` výpis pro každý z těchto typů v čistém Python kódu – ať s tím můžeš dál pracovat nebo analyzovat.

Mám pokračovat tímto směrem?

---

To je výborná otázka, Dalibore — a odpověď zní:

### ✅ **Ve většině případů ano… ale s pár výjimkami.**

---

## 🎯 Co **platí obecně**?

Ano, **každý objekt, jehož typ získáš přes `type(value)`**, je technicky třída (`type`) a tedy:

- **může být použit jako typová anotace** (např. `str`, `int`, `dict`, …)
- funguje jako běžná anotace bez nutnosti importovat z `typing`
  
Příklad:

```python
def foo(x: str) -> int:
    return int(x)
```

Tohle funguje naprosto v pořádku – a `type("něco") == str`, takže to potvrzuje tvůj předpoklad.

---

## ❗️ Výjimky a detaily

Ale některé typy:

1. **Mají neintuitivní použití**
2. **Nejsou dostatečně expresivní bez `typing` rozšíření**

Např.:

| Typ                   | type(value)     | Anotace použitelná? | Poznámka |
|----------------------|-----------------|----------------------|----------|
| `None`               | `NoneType`      | ✅ `None` nebo `NoneType` (v `types`) | Funguje, ale `Optional[...]` je čitelnější |
| `Ellipsis (...)`     | `ellipsis`      | ⚠️ nepoužívá se běžně | Má speciální význam v `typing.Tuple[...,]` |
| `NotImplemented`     | `NotImplementedType` | ⚠️ není běžná anotace | Interní konstrukce |
| `type`               | `type`          | ✅                  | ale někdy potřebuje `Type[...]` z `typing` |
| `classmethod`        | `classmethod`   | ❌                  | není určený pro anotace |
| `staticmethod`       | `staticmethod`  | ❌                  | dtto |

---

## 🔎 Shrnutí

### ✔️ Platí:
> „Vše, co je `type(value)`, je objekt typu `type`, a tedy technicky použitelný jako typová anotace.“

Ale…

### ⚠️ Ne vše je praktické nebo čitelné jako typová anotace

Proto je v běžné praxi lepší se držet:

- **nativních datových typů** (`int`, `str`, `float`, …)
- **typovacích rozšíření z `typing`** (`List[int]`, `Union[...]`, `Optional[...]`)

---

## ✅ Tip: Jak poznat, co je bezpečné jako anotace

Pokud chceš programově zjistit, jestli nějaký typ je "bezpečný" pro použití v anotacích:

```python
def is_valid_annotation_type(obj: object) -> bool:
    return isinstance(obj, type) and not obj.__name__.endswith("Error") and not obj.__name__.endswith("Warning")
```

Tohle není dokonalé, ale filtruje většinu výjimek.

---

Chceš připravit funkci, která přijme hodnotu a řekne:  
> "Typ této hodnoty je použitelný jako typová anotace: ✅/❌"?

Mohu i zobrazit proč a co případně místo toho použít.

---


|Kategorie|Typ|Popis|Příklad použití|
|Obecné obálky|Any|Libovolný typ|Any|
|Obecné obálky|Annotated|Typ + metainformace|Annotated[int, "věk v letech"]|
|Složení typů|Union|Více typů současně|Union[int, str]|
|Složení typů|Optional|Zkrácený zápis Union[X, None]|Optional[str]|
|Složení typů|Annotated|Typ s dodatečnou informací|Annotated[int, "Popis"]|
|Složení typů|Literal|Předdefinovaná množina hodnot|Literal["a", "b", "c"]|
|Složení typů|Final|Neměnitelná hodnota|Final[int]|
|Složení typů|ClassVar|Proměnná třídy, ne instance|ClassVar[int]|
|Generika / parametry|TypeVar|Parametrizovaný typ|T = TypeVar("T")|
|Generika / parametry|Generic|Základ pro tvorbu obecných tříd|class MyBox(Generic[T])|
|Generika / parametry|Protocol|Strukturální typování|class Serializable(Protocol)|
|Generika / parametry|NewType|Alias na jiný typ|UserId = NewType("UserId", int)|
|Sekvence / Kolekce|Iterable, Iterator|Sekvence / iterátory|Iterable[int]|
|Sekvence / Kolekce|Sequence|Nepřepisovatelná sekvence|Sequence[str]|
|Sekvence / Kolekce|Mapping|Obecný slovník|Mapping[str, int]|
|Sekvence / Kolekce|MutableMapping|Přepisovatelný slovník|MutableMapping[...]|
|Volání/funkce|Callable|Funkce|Callable[[int], str]|
|Odkazy a introspekce|ForwardRef|Odkaz na typ definovaný později|List["MyClass"]|
|Odkazy a introspekce|Self|Odkaz na vlastní třídu|def copy(self) -> Self:|
