## Mod 'one_line' 

Stručný výpis na jeden řádek obsahující název funkce a vstupní parametry

- Možnosti zápisu: **1, 'one_line', True**
- Použitím jedné z těchto hodnot výstupný log, pro daný dekorátor, obsahuje pouze jeden řádek.
- Jednořádkový výpis informuje o volání dané funkce a parametrů s kterými je volaná.
- Smysl tohoto výstupu je informace o metodách a funkcích, které se během operace volají.
- Zároveň i může sloužit k rychlému dohledání chyby na základě vizuální kontroli vstupních argumentů.

### Výstup se skládá z těchto částí:

Informace o použitém logeru a modu, název funkce, časové razítko a výpis případných argumentů se kterými je funkce volaná: 

    # INFO LogThis('one_line') | Function: {func.__name__} | {datetime.now()} | Arguments: {safe_serialize(args)}

### Příklad výstupu:

    # INFO LogThis('one_line') | Vstup do funkce: try_out_this | 2024-12-09 13:47:13.258484 | Vstupní argumenty: [[10, 20, 30], 2] 
