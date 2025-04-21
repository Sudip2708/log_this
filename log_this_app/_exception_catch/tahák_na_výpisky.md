## Kompletní tabulka s informacemi, které můžete získat z tracebacku pomocí `traceback.extract_tb()`:

Pro práci v rámci výjimky:

tb = traceback.extract_tb(e.__traceback__)
last_frame = tb[-1]  # Poslední krok v tracebacku
first_frame = tb[0]  # Poslední krok v tracebacku
filename = last_frame.filename
line_number = last_frame.lineno
line_code = last_frame.line

        
| Název atributu | Popis | Příklad hodnoty |
|---|---|---|
| `filename` | Název souboru, kde došlo k chybě. | `"muj_soubor.py"` |
| `lineno` | Číslo řádku, kde došlo k chybě. | `15` |
| `name` | Název funkce, ve které došlo k chybě. | `"moje_funkce"` |
| `line` | Řádek kódu, kde došlo k chybě. | `"return 10 / 0"` |

**Vysvětlení atributů:**

* **`filename`**:
    * Tento atribut obsahuje název souboru, ve kterém došlo k chybě.
    * Je to užitečné pro identifikaci souboru, kde je třeba hledat problém.
    * Příklad: `"muj_soubor.py"`
* **`lineno`**:
    * Tento atribut obsahuje číslo řádku v souboru, kde došlo k chybě.
    * Umožňuje přesně lokalizovat řádek kódu, který způsobil výjimku.
    * Příklad: `15`
* **`name`**:
    * Tento atribut obsahuje název funkce, ve které došlo k chybě.
    * Pomáhá sledovat, které funkce byly volány před výskytem chyby.
    * Příklad: `"moje_funkce"`
* **`line`**:
    * Tento atribut obsahuje skutečný řádek kódu, který způsobil výjimku.
    * Umožňuje zobrazit konkrétní kód, který vedl k chybě.
    * Příklad: `"return 10 / 0"`

## Několik atributů, které objekt funkce (`func`) může mít:

* `func.__doc__`:
    * Obsahuje dokumentační řetězec funkce (docstring).
    * Příklad: `"Vrátí součet dvou čísel."`
* `func.__module__`:
    * Obsahuje název modulu, ve kterém je funkce definována.
    * Příklad: `"muj_soubor"`
* `func.__defaults__`:
    * Obsahuje tuple výchozích hodnot argumentů funkce.
    * Příklad: `(0, "ahoj")`
* `func.__code__`:
    * Obsahuje objekt kódu funkce, který obsahuje bajtkód funkce.
    * Tento atribut je složitější a obvykle se nepoužívá pro základní logování.
* `func.__globals__`:
    * obsahuje slovník globálních proměnných funkce.

**Důležité body:**

* Většina těchto atributů se nepoužívá pro běžné zpracování výjimek.
* `func.__name__` je nejčastěji používaný atribut pro logování názvu funkce, kde došlo k chybě.
* Atributy jako `func.__doc__` nebo `func.__module__` mohou být užitečné pro dokumentaci nebo ladění.

* Většinou budou `func.__name__` a `traceback.last_frame.name` totožné.
* Existují situace, kdy se mohou lišit, zejména při použití vnořených funkcí nebo volání kódu z jiných souborů.

**Možné rozdíly:**

1.  **Vnořené funkce:**
    * Pokud máte vnořené funkce, může se stát, že výjimka vznikne ve vnitřní funkci, ale je zachycena ve vnější funkci.
    * V takovém případě `last_frame.name` bude název vnitřní funkce, kde došlo k chybě, zatímco `func.__name__` bude název vnější funkce, kde byla výjimka zachycena.
2.  **Volání z jiného souboru:**
    * Pokud funkce volá kód z jiného souboru, tak `last_frame.name` bude jméno funkce v onom souboru, a `func.__name__` bude jméno funkce v souboru aktuálním.
3.  **Použití `eval()` nebo `exec()`:**
    * Pokud se kód, který vyvolá výjimku, provádí pomocí `eval()` nebo `exec()`, může být `last_frame.name` `<module>`, protože se jedná o dynamicky generovaný kód.


## Informace z `Exception as e`:**

| Název atributu | Popis | Příklad hodnoty |
|---|---|---|
| `e.__class__` | Typ výjimky (objekt). | `<class 'ZeroDivisionError'>` |
| `e.__class__.__name__` | Název typu výjimky. | `"ZeroDivisionError"` |
| `str(e)` | Textová reprezentace výjimky. | `"division by zero"` |
| `e.args` | Tuple argumentů výjimky. | `("division by zero",)` |
| `e.__traceback__` | Objekt tracebacku výjimky. | `<traceback object at 0x...>` |

**Vysvětlení atributů:**

* **`e.__class__`**:
    * Vrací objekt typu výjimky.
    * Umožňuje zjistit přesný typ zachycené výjimky.
    * Příklad: `<class 'ZeroDivisionError'>`
* **`e.__class__.__name__`**:
    * Vrací název typu výjimky jako řetězec.
    * Umožňuje snadno zobrazit název typu výjimky.
    * Příklad: `"ZeroDivisionError"`
* **`str(e)`**:
    * Vrací čitelnou textovou reprezentaci výjimky.
    * Obsahuje chybové hlášení popisující, co se stalo.
    * Příklad: `"division by zero"`
* **`e.args`**:
    * Vrací tuple argumentů, které byly předány při vytvoření výjimky.
    * Umožňuje získat další informace o výjimce.
    * Příklad: `("division by zero",)`
* **`e.__traceback__`**:
    * Vrací objekt tracebacku, který obsahuje informace o zásobníku volání funkcí.
    * Umožňuje získat podrobné informace o tom, kde došlo k chybě.
    * Příklad: `<traceback object at 0x...>`

## Další příkazy v bloku `try-except`:**

| Název atributu/funkce | Popis | Příklad hodnoty |
|---|---|---|
| `func.__name__` | Název aktuální funkce. | `"moje_funkce"` |
| `inspect.currentframe()` | Aktuální rámec volání. | `<frame at 0x...>` |
| `inspect.currentframe().f_lineno` | Číslo řádku v aktuálním rámci. | `15` |
| `traceback.extract_tb(e.__traceback__)` | Seznam objektů `FrameSummary` z tracebacku. | `[<FrameSummary file="muj_soubor.py", line 10 in moje_funkce>, ...]` |

**Vysvětlení atributů/funkcí:**

* **`func.__name__`**:
    * Vrací název aktuální funkce, kde je blok `try-except` definován.
    * Umožňuje identifikovat funkci, ve které došlo k zachycení výjimky.
    * Příklad: `"moje_funkce"`
* **`inspect.currentframe()`**:
    * Vrací objekt rámce volání, který reprezentuje aktuální stav zásobníku volání funkcí.
    * Umožňuje získat informace o aktuálním kontextu provádění kódu.
    * Příklad: `<frame at 0x...>`
* **`inspect.currentframe().f_lineno`**:
    * Vrací číslo řádku v aktuálním rámci volání.
    * Umožňuje zjistit, na kterém řádku byl zachycen blok `try-except`.
    * Příklad: `15`
* **`traceback.extract_tb(e.__traceback__)`**:
    * Vrací seznam objektů `FrameSummary`, které obsahují informace o tracebacku.
    * Umožňuje získat podrobné informace o tom, kde došlo k chybě.
    * Příklad: `[<FrameSummary file="muj_soubor.py", line 10 in moje_funkce>, ...]`

