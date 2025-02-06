"""
Demonstrační modul pro základní použití dekorátoru @log_this() s jednou úrovní vnoření.

Tento soubor poskytuje příklad použití dekorátoru s nastavením dvou úrovní logování
pro vnořené funkce. Umožňuje testování různých módů logování definovaných v choice_info.

Příklad ukazuje jednoduchou strukturu s vnořením jedné funkce do druhé,
kde lze nezávisle nastavit úroveň logování pro každou funkci.

Podporované módy logování jsou definovány v seznamu choice_info a zahrnují:
- Žádné logování
- Jednořádkový výpis
- Stručný výpis
- Rozšířený výpis
- Kompletní výpis
"""
from examples._simple_function import try_out_simple


# Možnosti které jde použít jako vstup pro dekorátor
choice_info = [

    # Bez logování
    0, 'skip_this', False, None,

    # Na jeden řádek (pouze název a vstupní parametry)
    1, 'one_line', True,

    # Stručný výpis na 4 řádky (přidává výstupní hodnotu)
    2, 'simple',

    # Rozšířený výpis na 6 řádek (přidává dobu běhu a využití paměti)
    3, 'detailed',

    # Kompletní výpis na 10+ řádek (přidává analýzu prostředků a docstring)
    4, 'report',

]

# Spuštění ukázky
if __name__ == "__main__":

    # Nastavení úrovně logování
    outer_function = 1
    inner_function = 1

    # Zpuštění ukázky
    result = try_out_simple(outer_function, inner_function)