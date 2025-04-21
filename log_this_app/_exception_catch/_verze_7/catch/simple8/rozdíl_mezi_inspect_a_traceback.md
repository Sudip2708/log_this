## Takže by se dalo říci že pro to co potřebuji je traceback lepší pro svoji jednoduchost a inspect je zase výhodnější v případech kde potřebuji i dodatečné informace jako je třeba název třídy?

Ano, přesně tak. Vaše shrnutí je velmi trefné.

**`traceback` je lepší pro jednoduchost a přímé získání základních informací o místě vzniku výjimky:**

* Poskytuje specializované funkce, které přímo extrahují jméno souboru, číslo řádku a kód z traceback objektu výjimky.
* Jeho použití je intuitivní a kód je stručnější pro tento konkrétní účel.

**`inspect` je výhodnější v případech, kde potřebujete dodatečné informace a máte komplexnější požadavky na introspekci:**

* Umožňuje získat širší škálu informací o rámcích zásobníku volání, včetně názvu funkce, lokálních a globálních proměnných (i když s opatrností, kvůli potenciálním bezpečnostním rizikům a složitosti).
* Pokud byste potřebovali prozkoumat kontext volající funkce nebo získat informace o jejím okolí, `inspect` by byl vhodnější. Například, pokud byste chtěli zjistit název třídy, ve které se metoda volala (i když to vyžaduje trochu více práce s rámci zásobníku volání).

**Příklad pro získání názvu třídy pomocí `inspect` ve větvi `except` (složitější):**

```python
import traceback
import inspect

class MyClass:
    def my_method(self):
        try:
            1 / 0
        except Exception as e:
            tb = traceback.extract_tb(e.__traceback__)[-1]
            filename = tb.filename
            lineno = tb.lineno
            code = tb.line

            frame = inspect.currentframe().f_back.f_back  # Dvě úrovně zpět pro získání rámce my_method
            method_name = frame.f_code.co_name
            class_name = frame.f_locals['self'].__class__.__name__ if 'self' in frame.f_locals else None

            print(f"Chyba v souboru: {filename}, na řádku: {lineno}, kód: {code}")
            print(f"Došlo k chybě v metodě: {method_name} třídy: {class_name}")

obj = MyClass()
obj.my_method()
```

Tento příklad ukazuje, že získání názvu třídy pomocí `inspect` vyžaduje navigaci po rámcích zásobníku volání a přístup k lokálním proměnným, což je složitější než přímé použití `traceback` pro základní informace o chybě.

**Závěr:**

Pro standardní potřebu získání místa vzniku výjimky (soubor, řádek, kód) je `traceback` jednodušší a efektivnější. Pokud máte specifické a pokročilejší požadavky na introspekci kontextu chyby, jako je například název volající třídy nebo přístup k lokálním proměnným, pak může být `inspect` užitečný, i když s vyšší složitostí implementace. V mnoha běžných scénářích zpracování výjimek si vystačíte s modulem `traceback`.

---

## Je nějaký snadný způsob, jak zjistit název funkce a vstupního parametru, a nebo na to bych už musel použít inspect?

Ano, pro získání názvu aktuální funkce (`validate_native_type`) a jejích vstupních parametrů (`value`, `expected_type`) v kontextu bloku `except`, **budete muset použít modul `inspect`**.

Modul `traceback` primárně poskytuje informace o zásobníku volání *v okamžiku vzniku původní výjimky*, nikoli o kontextu, ve kterém je tato výjimka zachycena a znovu vyvolána.

Zde je, jak byste to mohli udělat pomocí `inspect`:

```python
import traceback
import inspect
from typing import Any, Type

class TypingValidateError(TypeError):
    pass

def validate_native_type(value: Any, expected_type: Type):
    """Ověření nativního typu"""
    try:
        if not isinstance(value, expected_type):
            raise TypingValidateError(
                f"Hodnota neodpovídá zadanému typu. "
                f"Požadovaný typ: {expected_type}. "
                f"Typ předané hodnoty: {type(value)}"
            )
        return True

    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)[-1]
        frame = inspect.currentframe()
        func_name = frame.f_code.co_name
        arg_info = inspect.getargvalues(frame)
        arg_names = arg_info.args
        arg_values = arg_info.locals

        input_params_str = ", ".join(f"{name}={repr(arg_values[name])}" for name in arg_names)

        raise TypingValidateError(
            f"Neočekávaná chyba při ověření nativního typu. "
            f"Funkce: {func_name}({input_params_str}). \n"
            f"Popis chyby: {e.__class__.__name__} - {str(e)}. \n"
            f"Soubor: {tb.filename}. "
            f"Řádek: {tb.lineno}. "
            f"Kod: {tb.line}. \n"
        )

if __name__ == '__main__':
    try:
        validate_native_type("svět", int)
    except TypingValidateError as e:
        print(f"Chyba ověření: {e}")

    try:
        class MyClass:
            pass
        validate_native_type("test", MyClass())
    except TypingValidateError as e:
        print(f"Chyba ověření (neočekávaná): {e}")
```

**Vysvětlení změn:**

1.  **`import inspect`**: Importujeme modul `inspect`.
2.  **`frame = inspect.currentframe()`**: Získáváme aktuální rámec zásobníku volání, což je rámec funkce `validate_native_type` v bloku `except`.
3.  **`func_name = frame.f_code.co_name`**: Získáváme název funkce z objektu kódu rámce.
4.  **`arg_info = inspect.getargvalues(frame)`**: Získáváme informace o argumentech aktuálního rámce. `arg_info` obsahuje:
    * `args`: Seznam názvů pozičních argumentů.
    * `varargs`: Název argumentu pro *args (pokud existuje).
    * `keywords`: Název argumentu pro **kwargs (pokud existuje).
    * `locals`: Slovník lokálních proměnných v rámci, včetně argumentů.
5.  **`arg_names = arg_info.args`**: Získáváme seznam názvů argumentů.
6.  **`arg_values = arg_info.locals`**: Získáváme slovník lokálních proměnných.
7.  **`input_params_str = ", ".join(f"{name}={repr(arg_values[name])}" for name in arg_names)`**: Vytváříme řetězec reprezentující vstupní parametry ve formátu `name=value`. Používáme `repr()` pro získání řetězcové reprezentace hodnot.

Nyní chybová zpráva bude obsahovat název funkce `validate_native_type` a její vstupní parametry v okamžiku, kdy došlo k zachycení a opětovnému vyvolání výjimky.

**Důležité poznámky:**

* Použití `inspect.currentframe()` získá informace o aktuálním rámci. Pokud byste chtěli informace o volající funkci, museli byste použít `inspect.currentframe().f_back`. V tomto případě chceme informace o `validate_native_type`, takže aktuální rámec je ten správný.
* `inspect` je mocný nástroj, ale jeho použití může být někdy trochu složitější než přímé použití `traceback`. Pro jednoduché získání informací o místě chyby je `traceback` obvykle dostačující. Pro získání kontextových informací o funkci, ve které se chyba zpracovává, je `inspect` nezbytný.

---

## Zajímalo by mě tedy, zda kdybych chtěl i tyto další informace, zda je lepší použít inspect pro všechno i pro jméno souboru, číslo řádku, a řádek kodu, a nebo i tak zde přináší použití kombinace inspect/traceback nějakou výhodu?

Použití kombinace `inspect` a `traceback` pro získání všech požadovaných informací (název funkce, vstupní parametry, jméno souboru, číslo řádku, řádek kódu) **přináší výhodu v oddělení zodpovědností a může vést k přehlednějšímu kódu.**

**Důvody pro kombinaci:**

* **`traceback` je specializovaný na informace o místě *původní* chyby:** Modul `traceback` je navržen primárně pro extrahování informací o zásobníku volání v okamžiku, kdy výjimka vznikla. Je velmi snadné a přímočaré s ním získat jméno souboru, číslo řádku a řádek kódu, kde došlo k problému.

* **`inspect` je lepší pro informace o *aktuálním kontextu zpracování* chyby:** Modul `inspect` je vhodný pro zjištění informací o funkci, ve které se výjimka *zachytila* (váš blok `except`), včetně jejího názvu a vstupních parametrů.

**Proč nepoužít `inspect` pro všechno?**

Ačkoli byste teoreticky mohli použít `inspect` k procházení rámců zásobníku volání a získání jména souboru, čísla řádku a kódu, je to o něco složitější a méně přímé než použití `traceback` pro tento konkrétní účel. Museli byste se pohybovat po rámcích zpět, dokud byste nenašli ten, kde došlo k původní chybě.

**Výhody kombinace:**

* **Čistší kód:** Oddělujete logiku získávání informací o původní chybě (`traceback`) od logiky získávání informací o aktuálním kontextu zpracování (`inspect`). To může vést k čitelnějšímu a udržitelnějšímu kódu.
* **Jasnější záměr:** Je zřejmé, že pro informace o místě chyby se používá nástroj, který je k tomu určen (`traceback`), a pro informace o aktuální funkci se používá nástroj pro introspekci (`inspect`).
* **Potenciálně robustnější:** `traceback` je navržen tak, aby spolehlivě pracoval s informacemi o výjimkách.

**Jak by vypadal kód s kombinací (pro připomenutí):**

```python
import traceback
import inspect
from typing import Any, Type

class TypingValidateError(TypeError):
    pass

def validate_native_type(value: Any, expected_type: Type):
    """Ověření nativního typu"""
    try:
        if not isinstance(value, expected_type):
            raise TypingValidateError(
                f"Hodnota neodpovídá zadanému typu. "
                f"Požadovaný typ: {expected_type}. "
                f"Typ předané hodnoty: {type(value)}"
            )
        return True

    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)[-1]
        frame = inspect.currentframe()
        func_name = frame.f_code.co_name
        arg_info = inspect.getargvalues(frame)
        arg_names = arg_info.args
        arg_values = arg_info.locals
        input_params_str = ", ".join(f"{name}={repr(arg_values[name])}" for name in arg_names)

        raise TypingValidateError(
            f"Neočekávaná chyba při ověření nativního typu. "
            f"Funkce: {func_name}({input_params_str}). \n"
            f"Popis chyby: {e.__class__.__name__} - {str(e)}. \n"
            f"Soubor: {tb.filename}. "
            f"Řádek: {tb.lineno}. "
            f"Kod: {tb.line}. \n"
        )
```

V tomto kódu `traceback` elegantně řeší získání informací o původu chyby a `inspect` se stará o kontext aktuálního zpracování. Je to rozumný kompromis mezi jednoduchostí a získáním všech potřebných detailů.

Použití pouze `inspect` by vyžadovalo složitější logiku pro nalezení správného rámce v zásobníku volání, který odpovídá místu původní chyby, a mohlo by být méně robustní, pokud by se hloubka zásobníku změnila. Proto je kombinace obou modulů pro tento scénář obecně lepší přístup.


