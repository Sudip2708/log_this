## Mod 'all' 

Úplný výpis doplněý o popis funkce a diagnostiku doby běhu funkce a využití paměti

### Základní info:

- Možnosti zápisu: **3, 'all'**
- Použitím jedné z těchto hodnot výstupný log, pro daný dekorátor, vypíše nastavené maximum informací.
- Výpis je oproti zjednodušenému výpisu 'simple' rozšířen o popis funkce, diagnostiku využití paměti a času běhu samotné funkce.
- Smyslem tohoto dekorátoru je poskytnout dodatečné informace které se mohou hodit pro hlubší analízu.
- Slouží tak převážně pro chvíle jemného ladění kodu a dohledávání chyb.
- Dekorátor zohledňuje vnořené volání, které je oddělené prázdným řádkem.

### Výstup se skládá z těchto částí:

Informace o použitém logeru a modu, název funkce a časové razítko: 

    # START LogThis('all') | Function: {func.__name__} | {datetime.now()}

Cesta k souboru kde je kod umístněn: 

    # >>> File: {inspect.getfile(func)}

Typová anotace vstupních hodnot (je-li): 

    # >>> Annotations: {func.__annotations__ or 'N/A'}

Výpis argunemtů se kterými je funkce, nebo metoda volaná: 

    # >>> Arguments: {safe_serialize(args)}

Výpis klíčových slov se kterými je funkce, nebo metoda volaná: 

    # >>> Kwards: {safe_serialize(kwargs)}

Popis funce z docstringu (je-li): 

    # >>> Docstring: {func.__doc__ or 'N/A'}

Výpis výsledku pokud vše proběhne v pořádku: 

        # >>> Result for '{func.__name__}': {result} (Type: {type(result).__name__})

Výpis výsledku pokud dojde k vyvolání výjimky: 

        # >>> Result for '{func.__name__}': An exception has been raised.
        # >>> Exception: {type(e).__name__}: {str(e)}")

Doba potřebná pro zpracování funkce: 

    # >>> Processing time: {function_duration:.6f} seconds

Využití paměti (z pohledu loggeru): 

    # >>> Memory usage: {memory_used} bytes

Výpis využití paměti (pro každý záznam: Hodnota využití, číslo řádku kodu, odkaz na soubor): 

    # >>> Memory allocation listing:
    # >>> > Allocated: {stat.size_diff} bytes, Line: {stat.traceback[0].lineno}, File: {stat.traceback[0].filename}

Informace o ukončení logu, název funkce, časové razítko a doba běhu logeru: 

    # END LogThis('all') | Function: '{func.__name__}' | {datetime.now()} | Log duration: {time.perf_counter() - logger_time:.6f} seconds\n

### Příklad výstupu bez vnořené funkce:

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

### Příklad výstupu s vnořenou funkcí nastavenou na mod 'simle' (mod pro vnořené funkce se mohou libovolně lišit):

    # START LogThis('all') pro funkci 'try_out_this' | 2024-12-09 13:52:30.085577 |
    # >>> Adresa souboru: C:\Users\Sudip2708\Desktop\planck_units\libraries\log_this\log_this\tests\_try_out_this.py
    # >>> Anotace parametrů: {'data_points': typing.List[int], 'multiplier': <class 'int'>, 'return': <class 'int'>}
    # >>> Vstupní argumenty: [[10, 20, 30], 2]
    # >>> Klíčová slova: {}
    # >>> Popis funkce: N/A
    
    # START LogThis('simple') pro funkci 'analyze_data' | 2024-12-09 13:52:30.085577 |
    # >>> Adresa souboru: C:\Users\Sudip2708\Desktop\planck_units\libraries\log_this\log_this\tests\_try_out_this.py
    # >>> Vstupní argumenty: [[10, 20, 30], 2]
    # >>> Klíčová slova: {}
    # >>> Výsledek pro funkci 'analyze_data': 120 (Typ: int)
    # END LogThis('simple') pro funkci 'analyze_data' | 2024-12-09 13:52:30.088024 | 
    Log duration: 0.001387 seconds
    
    # >>> Výsledek pro funkci 'try_out_this': 120 (Typ: int)
    # >>> Doba zpracování: 0.001777 seconds 
    # >>> Využití paměti: 640 bytes
    # >>> Výpis paměťových alokací:
    # >>> > Alokováno: 320 bajtů, Řádek: 560, Soubor: C:\Users\Sudip2708\AppData\Local\Programs\Python\Python311\Lib\tracemalloc.py
    # >>> > Alokováno: 320 bajtů, Řádek: 423, Soubor: C:\Users\Sudip2708\AppData\Local\Programs\Python\Python311\Lib\tracemalloc.py
    # END LogThis('all') pro funkci 'try_out_this' | 2024-12-09 13:52:30.088512 | Log duration: 0.002936 seconds
