## Knihovna Log This

Tato knihovna slouží k snadnému logování metod a funkcí a je vytvořena čistě z lenosti a snaze zjednodušit si život :-)  
Knihovna je primárně určena pro vývoj a není tak vhodná pro produkční prostředí.

Základní myšlenkou bylo vytvořit jednoduchý logovací systém který má přednastavené 3 mody výpisu,
a je možné ho používat ve vývojové fázy pro rychlé dohledávání chyb a pro kontrolu následností.

Logování tak probíhá čistě jen na základě dekorátoru '**@log_this()**' umístěný nad funkcí nebo metodou,
a nabízí jednoduché ovládání skrze parametr dekorátoru, který pro svou funkčnost může být i prázdný:

    from log_this import log_this
    
    @log_this()
    def example_function(x, y):
        return x + y

V takovém případě se dekorátor chová, jako by měl nastavenou hodnotu 'simple' a vrací výpis obsahující základní 
informace, jako je jméno funkce, vstupní a výstupní hodnoty:

    # START LogThis('simple') pro funkci 'try_out_this' | 2024-12-09 13:48:36.398274 |
    # >>> Adresa souboru: C:\Users\Sudip2708\Desktop\planck_units\libraries\log_this\log_this\tests\_try_out_this.py
    # >>> Vstupní argumenty: [[10, 20, 30], 2]
    # >>> Klíčová slova: {}
    # >>> Výsledek pro funkci 'try_out_this': 120 (Typ: int)
    # END LogThis('simple') pro funkci 'try_out_this' | 2024-12-09 13:48:36.398274 | 
    Log duration: 0.000549 seconds

Dekorátor pak dále nabízí více způsobů zadání daného modu, a to buď skrze číselnou hodnotu, 
jejíž ověření je nejrychlejší a je určena těm, kteří rádi stručnost a rychlost.
Další možností je zadávání definice modu skrze textové formulace sloužící pro lepší čitelnosti v kodu.
Je také možné použít boolena hodnoty, nebo None.

---

### Instalace knihovny:

- Naklonujte si repozitář nebo jej stáhněte.
- Ve složce projektu zadejte v terminálu:
       ```bash
       pip install .
       ```

Součástí knihovny jsou i testy pokrívající veškeré její dosavadní funkce.  
Testy je možné zpustit příkazem:
       ```bash
       doplnit prikaz
       ```
---

### Přednastavené mody knihovny:

- **Přeskočení logování** dané metody:  
  - Možnosti zápisu: **0, 'skip_this', None, False**
    - @log_this(0)
    - @log_this("skip_this")
    - @log_this(None)
    - @log_this(False)


- **Stručný výpis** na jeden řádek obsahující název funkce a vstupní parametry:  
  - Možnosti zápisu: **1, 'one_line', True**   
    - @log_this(1)
    - @log_this("one_line")
    - @log_this(True)
  - Příklad výstupu:
  
        # INFO LogThis('one_line') | Vstup do funkce: try_out_this | 2024-12-09 13:47:13.258484 | Vstupní argumenty: [[10, 20, 30], 2] 

  - [Pro další informace: info pro stručný výpis](about_data/mode_descriptions/mode_one_line.md)





- **Obsáhlejší výpis** obsahující rozšířené informace a výstupní hodnotu:  
  - Tato varianta je derfaultní a funguje i bez zadání parametru. 
  - Možnosti zápisu: **2, 'simple', ()**  
    - @log_this(2)
    - @log_this("simple")
    - @log_this()
  - Příklad výstupu:

        # START LogThis('simple') pro funkci 'try_out_this' | 2024-12-09 13:48:36.398274 |
        # >>> Adresa souboru: C:\Users\Sudip2708\Desktop\planck_units\libraries\log_this\log_this\tests\_try_out_this.py
        # >>> Vstupní argumenty: [[10, 20, 30], 2]
        # >>> Klíčová slova: {}
        # >>> Výsledek pro funkci 'try_out_this': 120 (Typ: int)
        # END LogThis('simple') pro funkci 'try_out_this' | 2024-12-09 13:48:36.398274 | 
        Log duration: 0.000549 seconds

  - [Pro další informace: info pro standardní výpis](about_data/mode_descriptions/mode_simple.md)


- **Úplný výpis** doplněý o popis funkce a diagnostiku doby běhu funkce a využití paměti:  
  - Možnosti zápisu: **3, 'all'**  
    - @log_this(3)
    - @log_this("all")
  - Příklad výstupu:

        # START LogThis('all') pro funkci 'try_out_this' | 2024-12-09 13:51:01.566489 |
        # >>> Adresa souboru: C:\Users\Sudip2708\Desktop\planck_units\libraries\log_this\log_this\tests\_try_out_this.py
        # >>> Anotace parametrů: {'data_points': typing.List[int], 'multiplier': <class 'int'>, 'return': <class 'int'>}
        # >>> Vstupní argumenty: [[10, 20, 30], 2]
        # >>> Klíčová slova: {}
        # >>> Popis funkce: N/A
        # >>> Výsledek pro funkci 'try_out_this': 120 (Typ: int)
        # >>> Doba zpracování: 0.000872 seconds 
        # >>> Využití paměti: 640 bytes
        # >>> Výpis paměťových alokací:
        # >>> > Alokováno: 320 bajtů, Řádek: 560, Soubor: C:\Users\Sudip2708\AppData\Local\Programs\Python\Python311\Lib\tracemalloc.py
        # >>> > Alokováno: 320 bajtů, Řádek: 423, Soubor: C:\Users\Sudip2708\AppData\Local\Programs\Python\Python311\Lib\tracemalloc.py
        # END LogThis('all') pro funkci 'try_out_this' | 2024-12-09 13:51:01.568923 | Log duration: 0.002551 seconds

  - [Pro další informace: info pro úplný výpis](about_data/mode_descriptions/mode_all.md)

---


### Doplňující informace:

- **Požadavky:**  
  - Python 3.6+
  - Standardní knihovny (`logging`, `functools`, `inspect`, `time`).


- **Licence:**
  - Knihovna je volně k použití a bez jakéhokoliv omezení pro úpravu nebo redistribuci kodu.
    

- **Kontakt:**
  - Autor: **Dalibor Sova**  
  - Email: [daliborsova@seznam.cz](daliborsova@seznam.cz)  
  - GitHub: [Sudip2708](https://github.com/Sudip2708)
---

### Podrobný rozbor kodu:

- [**log_this.py** (Kořenový soubor knihovny)](about_data/code_descriptions/code_log_this.md)
- [**log_one_line.py** (Nastavení pro jednořádkový výpis)](about_data/code_descriptions/code_log_one_line.md)
- [**log_simple.py** (Nastavení pro hlavní mod)](about_data/code_descriptions/code_log_simple.md)
- [**log_all.py** (Nastavení pro rozšířený mod)](about_data/code_descriptions/code_log_all.md)
- [**logger_settings.py** (Inicializace loggeru)](about_data/code_descriptions/code_logger_settings.md)
- [**mode_error.py** (Definice chybového oznamu)](about_data/code_descriptions/code_mode_error.md)
- [**safe_serialize.py** (Funkce pro serializaci dat)](about_data/code_descriptions/code_safe_serialize.md)

---