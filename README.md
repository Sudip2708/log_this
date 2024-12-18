## Log This

**Log This** je malá, snadno použitelná knihovna pro logování funkcí a metod v Pythonu. Nabízí tři různé dekorátory, které umožňují sledovat průběh volání funkcí, vstupní a výstupní hodnoty a případně další detaily, jako je zdrojový kód či lokální proměnné. Knihovna je navržena tak, aby usnadnila debugování a sledování výkonu funkcí.

---

### Hlavní vlastnosti

- **Jednoduché použití**: Dekorátory můžete snadno přidat k libovolné funkci nebo metodě pomocí `@log_this`, `@log_this_simple` nebo `@log_this_report`.
- **Flexibilita**: Tři úrovně logování umožňují zvolit mezi základním a detailním sledováním.
- **Lepší přehlednost**: Pomáhá identifikovat chyby, měřit dobu běhu funkcí a získat přehled o průběhu kódu.

---

### Dekorátory a jejich funkce

#### 1. `@log_this`
Tento dekorátor poskytuje **komplexní logování**, včetně:
- Vstupních argumentů funkce (positional a keyword).
- Návratových hodnot.
- Zachycení výjimek a jejich logování.

Použití:
```python
from log_this import log_this

@log_this
def example_function(x, y):
    return x + y
```

---

#### 2. `@log_this_simple`
Jednodušší varianta logování, která:
- Loguje pouze vstupní hodnoty a výstupní stav funkce.
- Vhodná pro rychlé ladění nebo přehledné logy.

Použití:
```python
from log_this import log_this_simple

@log_this_simple
def simple_function(a, b):
    return a * b
```

---

#### 3. `@log_this_report`
Nabízí **podrobné logování** s volitelným detailem:
- Základní logování zahrnuje:
  - Vstupní argumenty, návratové hodnoty a dobu běhu.
  - Zachycení výjimek.
- Při `detailed=True`:
  - Zachycuje lokální proměnné.
  - Zobrazuje zdrojový kód funkce.

Použití:
```python
from log_this import log_this_report

@log_this_report(detailed=True)
def complex_function(x, y):
    result = x * y
    return result
```

---

### Instalace

1. Naklonujte si repozitář nebo jej stáhněte.
2. Ve složce projektu spusťte:
   ```bash
   pip install .
   ```

---

### Použití

#### Příklad 1: Základní logování
```python
from log_this import log_this

@log_this
def add(a, b):
    return a + b

result = add(5, 10)
```

Výstup v logu:
```
2024-12-01 12:00:00 - DEBUG: Vstup do funkce 'add' s argumenty: args=(5, 10), kwargs={}
2024-12-01 12:00:01 - DEBUG: Výstup z funkce 'add': 15
```

#### Příklad 2: Podrobné logování
```python
from log_this import log_this_report

@log_this_report(detailed=True)
def multiply(a, b):
    c = a * b
    return c

result = multiply(3, 4)
```

Výstup v logu:
```
2024-12-01 12:00:00 - INFO: Volání funkce: multiply
2024-12-01 12:00:01 - INFO: Vstupní argumenty positional: (3, 4)
2024-12-01 12:00:01 - INFO: Výstup funkce multiply: 12
2024-12-01 12:00:01 - INFO: Doba běhu funkce multiply: 0.0001 sekund
2024-12-01 12:00:01 - INFO: Lokální proměnné: {'a': 3, 'b': 4, 'c': 12}
2024-12-01 12:00:01 - INFO: Zdrojový kód funkce:
    def multiply(a, b):
        c = a * b
        return c
```

---

### Dokumentace

#### `log_this`
Dekorátor pro logování vstupu, výstupu a chyb:
- **Formát logu**: DEBUG.
- **Zachycuje**:
  - Argumenty funkce.
  - Návratovou hodnotu.
  - Výjimky.

#### `log_this_simple`
Dekorátor pro jednoduché logování:
- **Formát logu**: INFO.
- **Zachycuje**:
  - Argumenty funkce.
  - Návratovou hodnotu.

#### `log_this_report`
Dekorátor pro podrobné logování:
- **Formát logu**: INFO.
- **Zachycuje**:
  - Argumenty funkce.
  - Návratovou hodnotu.
  - Doba běhu funkce.
- **Volitelně** (detailed=True):
  - Lokální proměnné.
  - Zdrojový kód funkce.

---

### Požadavky

- Python 3.6+
- Standardní knihovny (`logging`, `functools`, `inspect`, `time`).

---

### Plánované funkce

- Možnost logovat do souboru místo konzole.
- Přizpůsobitelné formáty logů.
- Podpora asynchronních funkcí (`async def`).

---

### Licence

Tento projekt je licencován pod **MIT License**. Detaily naleznete v souboru `LICENSE`.

---

### Kontakt

Autor: **Dalibor Sova**  
Email: [daliborsova@seznam.cz](daliborsova@seznam.cz)  
GitHub: [Sudip2708](https://github.com/Sudip2708)



