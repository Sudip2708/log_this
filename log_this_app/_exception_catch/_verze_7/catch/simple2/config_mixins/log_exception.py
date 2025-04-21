from abc import ABC
from typing import Dict, List, Optional, Type, Union, Callable, Any

from ......abc_helper import abc_property, abc_method


class LogExceptionMixin(ABC):

    # Slovník {exception_type: handler_config} pro specifické zpracování výjimek
    exception_handlers = abc_property("exception_handlers")

    # Vlastní logger pro použití (pokud není zadán, použije se root logger)
    loger = abc_property("exception_handlers")


    def log_exception(
            self,
            func_name: str,
            exception: Exception,
            specific_exceptions: List[Type[Exception]] = None
    ) -> None:
        """
        Loguje výjimku podle konfigurace.

        Args:
            func_name: Jméno funkce, kde došlo k výjimce
            exception: Zachycená výjimka
            specific_exceptions: Seznam typů výjimek, které byly zadány v dekorátoru
        """

        # Načtení typu výjimky
        exc_type = type(exception)  # Např: <class 'ZeroDivisionError'>
        exc_name = type(exception).__name__  # Např: ZeroDivisionError>

        # Kontrola, zda existuje specifická konfigurace pro daný typ výjimky
        handler_config = None
        # Procházení slovníku se specifikací pro jedotlivé výjimky
        for exc_class in self.exception_handlers:
            # Porovnání, zda se výjimka schoduje
            if isinstance(exception, exc_class):
                handler_config = self.exception_handlers[exc_class]
                break

        # Kontrola zda se našli pro výjimku nějaké specidfické požadavky
        if handler_config:
            # Použijeme specifickou konfiguraci
            log_level = handler_config.get('log_level', self.log_level)
            prefix = handler_config.get('message_prefix', '')
            custom_handle_func = handler_config.get('handle_func')

            error_message = f"{prefix}Chyba při vykonávání {func_name}: {exc_name} - {exception}}"

            # Pokud je k dispozici vlastní handle funkce, použijeme ji
            if custom_handle_func:
                custom_handle_func(exception, {'error_message': error_message,
                                               'function': func_name})
            else:
                self.logger.log(log_level, error_message, exc_info=True)
        else:
            # Použijeme výchozí konfiguraci
            error_message = f"Chyba při vykonávání {func_name}: {exc_name} - {exception}"
            # f"Výjimka v metodě {func.__name__}: {type(e).__name__} - {str(e)}"
            error_message2 = f"Chyba při vykonávání {func_name}: {exc_name} - {exception}"


            self.logger.error(error_message, exc_info=True)

# def hlavni_program():
#     try:
#         funkce_a()
#     except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        last_frame = tb[-1]  # Poslední krok v tracebacku
        filename = last_frame.filename
        line_number = last_frame.lineno
        line_code = last_frame.line

        first_frame = tb[0]  # Poslední krok v tracebacku
#         first_filename = first_frame.filename
#         first_line_number = first_frame.lineno
#         first_line_code = first_frame.line
#
#         print(f"Chyba v souboru: {filename}, řádek: {line_number}, kód: {line_code}")
#         print(f"První výskyt v souboru: {first_filename}, řádek: {first_line_number}, kód: {first_line_code}")
#         # Nebo pro výpis jen řádku a kodu, kde se nacházíme.
#         print(f"Chyba na řádku: {line_number}, kód: {line_code}")

"""
Jasně, zde je kompletní tabulka s informacemi, které můžete získat z tracebacku pomocí `traceback.extract_tb()`:

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



* Většinou budou `func.__name__` a `last_frame.name` totožné.
* Existují situace, kdy se mohou lišit, zejména při použití vnořených funkcí nebo volání kódu z jiných souborů.

**Možné rozdíly:**

1.  **Vnořené funkce:**
    * Pokud máte vnořené funkce, může se stát, že výjimka vznikne ve vnitřní funkci, ale je zachycena ve vnější funkci.
    * V takovém případě `last_frame.name` bude název vnitřní funkce, kde došlo k chybě, zatímco `func.__name__` bude název vnější funkce, kde byla výjimka zachycena.
2.  **Volání z jiného souboru:**
    * Pokud funkce volá kód z jiného souboru, tak `last_frame.name` bude jméno funkce v onom souboru, a `func.__name__` bude jméno funkce v souboru aktuálním.
3.  **Použití `eval()` nebo `exec()`:**
    * Pokud se kód, který vyvolá výjimku, provádí pomocí `eval()` nebo `exec()`, může být `last_frame.name` `<module>`, protože se jedná o dynamicky generovaný kód.


**1. Informace z `Exception as e`:**

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

**2. Další příkazy v bloku `try-except`:**

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

Ano, v kontextu, ve kterém jsme se bavili (tedy v rámci bloku `try-except`), je `func.__name__` nejčastěji používaný a relevantní atribut. Nicméně, objekty funkcí v Pythonu mají i další atributy.

**Další atributy objektu funkce (`func`)**

Zde je několik dalších atributů, které objekt funkce (`func`) může mít:

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

**Příklad:**

```python
def moje_funkce(a, b=0):
    """Vrátí součet dvou čísel."""
    return a + b

print(moje_funkce.__name__)
print(moje_funkce.__doc__)
print(moje_funkce.__defaults__)
print(moje_funkce.__module__)

```

Tento kód vypíše název funkce, dokumentační řetězec a výchozí hodnoty argumentů.

Doufám, že vám toto upřesnění pomůže.

"""