# Srovnání knihoven traceback a inspect v Pythonu

## Základní rozdíly

**traceback** knihovna:
- Zaměřuje se primárně na informace o výjimkách a jejich zpracování
- Poskytuje informace o cestě vykonávání programu v momentě, kdy došlo k výjimce
- Je hlavně určena pro analýzu call stacku při výjimkách
- Pracuje s objektem traceback, který vzniká při výjimce

**inspect** knihovna:
- Poskytuje obecnější nástroje pro introspekci kódu
- Umožňuje procházet aktuální call stack bez ohledu na výjimky
- Nabízí širší množství informací o objektech, funkcích, modulech
- Dokáže analyzovat běžící program i bez přítomnosti výjimky

## Kdy použít kterou knihovnu

**traceback** použij, když:
- Potřebuješ zpracovat výjimku a získat informace o tom, kde vznikla
- Chceš formátovat výpis výjimky
- Zajímá tě cesta vykonávání kódu vedoucí k výjimce

**inspect** použij, když:
- Potřebuješ informace o aktuálním call stacku v libovolném místě programu
- Chceš získat metadata o funkcích, třídách nebo modulech
- Potřebuješ introspekci kódu (zdrojový kód, signatury funkcí)
- Chceš analyzovat běžící program i když nevznikla výjimka

## Porovnání hlavních funkcí a metod

| Aspekt | traceback modul | inspect modul |
|--------|-----------------|---------------|
| **Základní účel** | Zpracování výjimek | Obecná introspekce |
| **Hlavní vstup** | Objekt traceback získaný při výjimce | Může pracovat s libovolnými objekty |
| **Hlavní funkce** | `extract_tb()`, `format_exception()`, `print_exception()` | `stack()`, `getmembers()`, `getmodule()`, `signature()` |
| **Získání call stacku** | `extract_tb(sys.exc_info()[2])` | `inspect.stack()` |
| **Formátování chyb** | `format_exception()`, `format_exc()` | Neposkytuje přímé formátování výjimek |
| **Přístup k informacím o řádku** | Pouze v rámci traceback objektu | Kdykoli během běhu programu |
| **Metadata objektů** | Ne | Ano (např. `getmembers()`, `isfunction()`) |
| **Zdrojový kód** | Omezené možnosti | Rozsáhlé možnosti (`getsource()`, `getsourcelines()`) |
| **Signatury funkcí** | Ne | Ano (`signature()`) |

## Příklady použití

### traceback - zachycení výjimky

```python
import sys
import traceback

try:
    1/0
except Exception as e:
    exc_type, exc_value, exc_tb = sys.exc_info()
    # Získání seznamu framů v traceback
    tb_list = traceback.extract_tb(exc_tb)
    # Formátování výjimky do řetězce
    exception_str = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    # Tisk traceback
    traceback.print_exc()
```

### inspect - analýza call stacku

```python
import inspect

def foo():
    # Získání aktuálního call stacku
    stack = inspect.stack()
    # Informace o aktuálním framu
    current_frame = stack[0]
    print(f"Funkce: {current_frame.function}")
    print(f"Soubor: {current_frame.filename}")
    print(f"Řádek: {current_frame.lineno}")
    # Zdrojový kód
    if current_frame.code_context:
        print(f"Kód: {current_frame.code_context[0].strip()}")

foo()
```

# Srovnání knihoven traceback a inspect v Pythonu

## Základní rozdíly

**traceback** knihovna:
- Zaměřuje se primárně na informace o výjimkách a jejich zpracování
- Poskytuje informace o cestě vykonávání programu v momentě, kdy došlo k výjimce
- Je hlavně určena pro analýzu call stacku při výjimkách
- Pracuje s objektem traceback, který vzniká při výjimce

**inspect** knihovna:
- Poskytuje obecnější nástroje pro introspekci kódu
- Umožňuje procházet aktuální call stack bez ohledu na výjimky
- Nabízí širší množství informací o objektech, funkcích, modulech
- Dokáže analyzovat běžící program i bez přítomnosti výjimky

## Kdy použít kterou knihovnu

**traceback** použij, když:
- Potřebuješ zpracovat výjimku a získat informace o tom, kde vznikla
- Chceš formátovat výpis výjimky
- Zajímá tě cesta vykonávání kódu vedoucí k výjimce

**inspect** použij, když:
- Potřebuješ informace o aktuálním call stacku v libovolném místě programu
- Chceš získat metadata o funkcích, třídách nebo modulech
- Potřebuješ introspekci kódu (zdrojový kód, signatury funkcí)
- Chceš analyzovat běžící program i když nevznikla výjimka

## Porovnání hlavních funkcí a metod

| Aspekt | traceback modul | inspect modul |
|--------|-----------------|---------------|
| **Základní účel** | Zpracování výjimek | Obecná introspekce |
| **Hlavní vstup** | Objekt traceback získaný při výjimce | Může pracovat s libovolnými objekty |
| **Hlavní funkce** | `extract_tb()`, `format_exception()`, `print_exception()` | `stack()`, `getmembers()`, `getmodule()`, `signature()` |
| **Získání call stacku** | `extract_tb(sys.exc_info()[2])` | `inspect.stack()` |
| **Formátování chyb** | `format_exception()`, `format_exc()` | Neposkytuje přímé formátování výjimek |
| **Přístup k informacím o řádku** | Pouze v rámci traceback objektu | Kdykoli během běhu programu |
| **Metadata objektů** | Ne | Ano (např. `getmembers()`, `isfunction()`) |
| **Zdrojový kód** | Omezené možnosti | Rozsáhlé možnosti (`getsource()`, `getsourcelines()`) |
| **Signatury funkcí** | Ne | Ano (`signature()`) |

## Příklady použití

### traceback - zachycení výjimky

```python
import sys
import traceback

try:
    1/0
except Exception as e:
    exc_type, exc_value, exc_tb = sys.exc_info()
    # Získání seznamu framů v traceback
    tb_list = traceback.extract_tb(exc_tb)
    # Formátování výjimky do řetězce
    exception_str = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    # Tisk traceback
    traceback.print_exc()
```

### inspect - analýza call stacku

```python
import inspect

def foo():
    # Získání aktuálního call stacku
    stack = inspect.stack()
    # Informace o aktuálním framu
    current_frame = stack[0]
    print(f"Funkce: {current_frame.function}")
    print(f"Soubor: {current_frame.filename}")
    print(f"Řádek: {current_frame.lineno}")
    # Zdrojový kód
    if current_frame.code_context:
        print(f"Kód: {current_frame.code_context[0].strip()}")

foo()
```


Rád ti vysvětlím rozdíly mezi knihovnami `traceback` a `inspect` v Pythonu.

## Knihovna traceback

Knihovna `traceback` je specializovaná na práci s výjimkami. Když v Pythonu nastane výjimka, vytvoří se objekt traceback, který obsahuje informace o "cestě", po které se program dostal k místu výjimky.

Hlavní účel `traceback` knihovny:
- Zobrazit a zpracovat cesty vykonávání programu při výjimce
- Formátovat chybové zprávy podobně jako standardní Python
- Extrahovat informace z traceback objektu získaného pomocí `sys.exc_info()`

Důležité je pochopit, že knihovna `traceback` pracuje primárně s již existujícím objektem traceback, který vznikl při výjimce.

## Knihovna inspect

Knihovna `inspect` je mnohem obecnější nástroj pro introspekci. Umožňuje zkoumat "živé" objekty v Pythonu - ať už jde o moduly, třídy, funkce nebo běžící program.

Hlavní účel `inspect` knihovny:
- Získat detailní informace o běžícím programu kdykoli
- Prozkoumat vlastnosti objektů, funkcí, tříd a modulů
- Přistupovat ke zdrojovému kódu objektů
- Analyzovat signatury funkcí
- Procházet call stack i bez přítomnosti výjimky

V tvém případě pomohla knihovna `inspect`, protože dokáže získat informace o volajícím framu bez ohledu na to, jestli je součástí traceback objektu výjimky.

## Kdy kterou použít?

- Používej `traceback`, když zpracováváš výjimky a chceš z nich vytáhnout informace nebo je formátovat.
- Používej `inspect`, když potřebuješ obecnější introspekci programu, získat informace o call stacku mimo kontext výjimky, nebo když potřebuješ informace o objektech a funkcích.

Vytvořil jsem pro tebe přehlednou tabulku srovnání těchto knihoven, kterou najdeš v přiloženém dokumentu. Obsahuje detailní porovnání funkcí, příklady použití a doporučení, kdy je vhodné kterou knihovnu použít.

Máš nějaké další otázky k těmto knihovnám nebo k jejich praktickému využití?