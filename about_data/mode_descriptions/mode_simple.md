## Mod 'simple' 

Obsáhlejší výpis obsahující rozšířené informace a výstupní hodnotu 

### Základní info:

- Možnosti zápisu: **2, 'simple', ()**
- Tato varianta je použita i v případě, pokud není zadána žádná hodnota: **@log_this()**
- Použitím jedné z těchto hodnot výstupný log, pro daný dekorátor, obsahuje základní informace rozložené do více řádků.
- Výpis je oproti jednořádkovému výstupu rozšířen o odkaz na soubor, výstupní hodnotu a čas běhu dekorátoru.
- Smyslem tohoto dekorátoru je poskytnout detalnější informace.
- Může tak sloužit při vývoji pro rychlou kontrolu nejen vstupních dat, ale i výstupních a i s odkazen na soubor ve kterém je kod uveden..
- Dekorátor zohledňuje vnořené volání, které je oddělené prázdným řádkem.


### Výstup se skládá z těchto částí:

Informace o použitém logeru a modu, název funkce a časové razítko:

    # START LogThis('simple') | Function: {func.__name__} | {datetime.now()}
  
Cesta k souboru kde je kod umístněn: 

    # >>> File: {inspect.getfile(func)}
  
Výpis argunemtů se kterými je funkce, nebo metoda volaná:

    # >>> Arguments: {safe_serialize(args)}
  
Výpis klíčových slov se kterými je funkce, nebo metoda volaná: 

    # >>> Kwards: {safe_serialize(kwargs)}
  
Výpis výsledku pokud vše proběhne v pořádku: 

        # >>> Result for '{func.__name__}': {result} (Type: {type(result).__name__})
  
Výpis výsledku pokud dojde k vyvolání výjimky: 

        # >>> Result for '{func.__name__}': An exception has been raised.
        # >>> Exception: {type(e).__name__}: {str(e)}")
  
Informace o ukončení logu, název funkce, časové razítko a doba běhu logeru: 

    # END LogThis('simple') | Function: '{func.__name__}' | {datetime.now()} | 
    Log duration: {time.perf_counter() - logger_time:.6f} seconds\n

  
### Příklad výstupu bez vnořené funkce:

    # START LogThis('simple') pro funkci 'try_out_this' | 2024-12-09 13:48:36.398274 |
    # >>> Adresa souboru: C:\Users\Sudip2708\Desktop\planck_units\libraries\log_this\log_this\tests\_try_out_this.py
    # >>> Vstupní argumenty: [[10, 20, 30], 2]
    # >>> Klíčová slova: {}
    # >>> Výsledek pro funkci 'try_out_this': 120 (Typ: int)
    # END LogThis('simple') pro funkci 'try_out_this' | 2024-12-09 13:48:36.398274 | 
    Log duration: 0.000549 seconds

### Příklad výstupu s vnořenou funkcí:

    # START LogThis('simple') pro funkci 'try_out_this' | 2024-12-09 13:49:45.291435 |
    # >>> Adresa souboru: C:\Users\Sudip2708\Desktop\planck_units\libraries\log_this\log_this\tests\_try_out_this.py
    # >>> Vstupní argumenty: [[10, 20, 30], 2]
    # >>> Klíčová slova: {}
    
    # START LogThis('simple') pro funkci 'analyze_data' | 2024-12-09 13:49:45.291435 |
    # >>> Adresa souboru: C:\Users\Sudip2708\Desktop\planck_units\libraries\log_this\log_this\tests\_try_out_this.py
    # >>> Vstupní argumenty: [[10, 20, 30], 2]
    # >>> Klíčová slova: {}
    # >>> Výsledek pro funkci 'analyze_data': 120 (Typ: int)
    # END LogThis('simple') pro funkci 'analyze_data' | 2024-12-09 13:49:45.292412 | 
    Log duration: 0.000518 seconds
    
    # >>> Výsledek pro funkci 'try_out_this': 120 (Typ: int)
    # END LogThis('simple') pro funkci 'try_out_this' | 2024-12-09 13:49:45.292412 | 
    Log duration: 0.001190 seconds