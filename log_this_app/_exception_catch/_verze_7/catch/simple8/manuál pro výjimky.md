Jasně, tady je `.md` soubor, který slouží jako přehledný manuál pro práci s výjimkami v Pythonu, včetně poznámek z tvého testování a shrnutí výstupu `tracebacku`:

---

### `exceptions_guide.md`

```markdown
# Manuál pro práci s výjimkami v Pythonu

Tento dokument shrnuje principy práce s výjimkami (`try`, `except`, `finally`, `raise`) v jazyce Python. Je doplněn o konkrétní příklady a poznatky z testování chování `tracebacku`.

---

## 1. Základy výjimek

Python výjimky slouží k zachycení a zpracování chyb, které nastanou při běhu programu. Základní syntaxe:

```python
try:
    # kód, který může vyvolat výjimku
except Výjimka as e:
    # zpracování výjimky
finally:
    # blok, který se provede vždy, i když došlo k výjimce
```

---

## 2. Automatické chování při výjimce

Bez jakéhokoli `try` bloku Python automaticky vypíše tzv. traceback, který obsahuje:

- cestu k souboru
- číslo řádku
- kód řádku
- typ výjimky
- textový popis chyby

Např.:

```text
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    int("abc")
ValueError: invalid literal for int() with base 10: 'abc'
```

---

## 3. Zachycení výjimky

Zachycením výjimky pomocí `except` do procesu vstupujeme:

```python
try:
    int("abc")
except ValueError as e:
    print("Chyba byla zachycena.")
```

Tím zabráníme automatickému tracebacku a máme kontrolu nad tím, co se děje dál.

---

## 4. Znovuvyvolání výjimky (`raise`)

### 4.1. `raise`

Pouhým `raise` bez argumentu znovu vyvoláme původní výjimku:

```python
try:
    int("abc")
except ValueError:
    print("Chyba zachycena, předávám dál.")
    raise
```

Traceback se v tomto případě chová stejně, jako kdyby výjimka nebyla zachycena.

---

### 4.2. `raise ValueError("text")`

Můžeme také vyvolat novou výjimku:

```python
try:
    int("abc")
except ValueError:
    raise ValueError("Chyba při převodu na int")
```

Výstup ukazuje:
- původní chybu (pokud ji uvedeme pomocí `from e`)
- novou chybu

---

### 4.3. `raise ... from e`

Používá se k explicitnímu propojení výjimky s původní chybou:

```python
try:
    int("abc")
except ValueError as e:
    raise TypeError("Došlo k typové chybě") from e
```

Přínos: **zachová kontext původní výjimky**, což je užitečné při ladění složitějších aplikací.

Výstup:

```text
The above exception was the direct cause of the following exception:
```

---

## 5. `traceback` modul

Pomocí `traceback.format_exc()` lze získat traceback jako text:

```python
import traceback

try:
    int("abc")
except Exception as e:
    tb = traceback.format_exc()
    print("Zachyceno:", tb)
```

To se hodí např. pro logování.

---

## 6. `finally`

Blok `finally` se **vždy vykoná**, i když výjimka nebyla zachycena nebo byl proveden `return`.

```python
try:
    ...
except:
    ...
finally:
    print("Toto se provede vždy.")
```

---

## 7. Možnosti zpracování výjimek

| Přístup | Popis | Vhodné použití |
|--------|-------|----------------|
| `pass` | Zcela potlačí výjimku | Testovací kód, občas nevhodné |
| `raise` | Opět vyvolá aktuální výjimku | Předání výjimky výš |
| `raise NováVýjimka()` | Přepíše výjimku novou | Přesnější popis chyby |
| `raise ... from e` | Spojí novou výjimku s původní | Užitečné pro ladění, logování |
| `traceback.format_exc()` | Získá text výpisu tracebacku | Logging, debugging |

---

## 8. Kdy zasahovat do výjimky?

Pokud je výstup výjimky dostatečný (např. `TypeError`, `ValueError` s popisem), často není potřeba jej přepisovat. Do procesu výjimky má smysl vstupovat, pokud:

- chceme přidat kontext (např. informace o proměnné nebo prostředí)
- potřebujeme transformovat výjimku (např. z `ValueError` na `ConfigError`)
- logujeme výjimku do souboru
- chceme výstup "ztišit" nebo elegantně ošetřit

---

## 9. Shrnutí

- Výjimky v Pythonu jsou mocný nástroj pro řízení toku programu.
- Traceback se generuje automaticky a většinou obsahuje dost informací.
- `raise` a `raise ... from e` umožňují elegantní předávání a transformaci výjimek.
- `try/except/finally` dává programátorovi plnou kontrolu nad tím, jak se chyby zpracují.
- Výjimku je vhodné zachytit pouze pokud s ní chceme něco konkrétního udělat.

---

## 10. Doporučení

- Nepoužívej `except Exception: pass` bez velmi dobrého důvodu.
- Loguj traceback výjimky v aplikacích pro snazší ladění.
- Používej `raise ... from e` pro zachování souvislostí u přepisovaných výjimek.
- Při vlastních výjimkách vytvářej vlastní třídy (např. `class MyError(Exception)`).

```

### 🛑 Ukončení programu bez `raise`: `sys.exit()` vs `exit()`

Pokud nechceme použít `raise`, ale přesto chceme při chybě:

- vypsat vlastní chybovou hlášku,
- **převzít kontrolu nad formátem výstupu** (např. místo tracebacku),
- a **ukončit program okamžitě bez dalšího zpracování**,

pak je vhodné použít:

#### ✅ `sys.exit([exit_code])`
Toto je standardní způsob ukončení běhu programu ve skriptech.  
Volitelně můžeš předat návratový kód (např. `1` pro chybu, `0` pro úspěch).

```python
import sys

try:
    # nějaký kód, který může selhat
    ...
except SomeError:
    print("Vlastní zpráva o chybě.")
    sys.exit(1)  # ukončí program, nezobrazí traceback
```

> `sys.exit()` pod kapotou vyvolá výjimku `SystemExit`, kterou ale běžné `except Exception` bloky nechytí (pokud výslovně nechceš pomocí `except BaseException`).

---

#### ⚠️ `exit()`
Tato funkce funguje podobně, ale je určena hlavně pro **interaktivní režim Pythonu** (např. konzole, Jupyter Notebook).  
Ve skriptech může být nespolehlivá – někdy nefunguje vůbec, nebo funguje jinak podle prostředí.

---

### 🔍 Kdy použít který?

| Funkce       | Použití                          | Stabilita ve skriptech | Výchozí návratový kód |
|--------------|----------------------------------|--------------------------|------------------------|
| `sys.exit()` | V produkčních skriptech a CLI    | ✅ Spolehlivá             | `0` (nebo co zadáš)    |
| `exit()`     | V interaktivní konzoli / REPL    | ❌ Nespolehlivá           | `0` (nebo co zadáš)    |

---

### 📌 Shrnutí:
Pokud **nechceš traceback**, **nechceš dál předávat výjimku** a chceš **plně vlastní výstup**, pak kombinace `print(...)` a `sys.exit(...)` je ideální.  
Díky tomu si můžeš kompletně přizpůsobit zobrazení chyby podle vlastního formátu – třeba i využitím `traceback.format_exc()` do vlastního logu.

