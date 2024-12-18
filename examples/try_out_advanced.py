"""
Demonstrační modul pro pokročilé použití dekorátoru @log_this() s vícenásobným vnoořením.

Tento soubor poskytuje komplexní příklad použití dekorátoru s nastavením čtyř úrovní logování
pro různě vnořené funkce. Umožňuje testování a kombinování různých módů logování.

Příklad demonstruje složitější strukturu s několika vnořenými funkcemi,
kde lze nezávisle nastavit úroveň logování pro každou funkci:
- Hlavní obalující funkce
- Funkce pro vnořené volání dalších funkcí
- Funkce pro sčítání
- Funkce pro porovnání

Podporované módy logování jsou definovány v seznamu choice_info a zahrnují:
- Žádné logování
- Jednořádkový výpis
- Stručný výpis
- Rozšířený výpis
- Kompletní výpis

Mody pro logování lze libovolně kombinovat.
"""
from examples._advanced_function import try_out_advanced


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
    first_function = 1
    second_function = 1
    third_function = 1
    fourth_function = 1

    # Zpuštění ukázky
    result = try_out_advanced(
        first_function,  # Hodnota pro dekorátor funkce obalující ostatní 'log_this_test_function'
        second_function,  # Hodnota pro dekorátor funkci volající funkce pro sčítání a porovnání 'first_function_nesting'
        third_function,  # Hodnota pro dekorátor funkce pro sčítání 'second_function_addition'
        fourth_function,  # Hodnota pro dekorátor funkce pro porovnání 'third_function_comparison'
    )