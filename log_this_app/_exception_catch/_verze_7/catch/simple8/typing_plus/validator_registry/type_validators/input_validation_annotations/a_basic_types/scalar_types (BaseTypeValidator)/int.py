from .._base_type_validator import BaseTypeValidator


class IntValidator(BaseTypeValidator):
    """
    Validátor pro typovou anotaci int

    Int reprezentuje celé číslo v Pythonu. Na rozdíl od mnoha programovacích jazyků
    nemá Python omezení na velikost celých čísel - int může reprezentovat libovolně
    velké celé číslo, omezené pouze dostupnou pamětí.

    Syntaxe:
        - int    # Přímý zápis typu

    Příklady použití:
        - int    # Celé číslo (kladné, záporné nebo nula)

    Validační proces:
        1. Ověřuje, zda hodnota je instance typu int
        2. Ujišťuje se, že hodnota je přímo objekt typu int, nikoliv hodnoty,
           které lze na int převést (float, bool, str s číslem)
        3. Poznámka: bool je v Pythonu podtřídou int, ale validátor vyžaduje přesně int

    Použití v kódu:
        - Pro parametry funkcí: def calculate_factorial(n: int) -> int
        - Pro návratové hodnoty: def count_items() -> int
        - Pro typování proměnných: count: int = 42

    Zápis hodnot:
        - Decimální: 42, -7, 0
        - Binární: 0b101010 (42)
        - Oktální: 0o52 (42)
        - Hexadecimální: 0x2A (42)

    Operace:
        - Aritmetické: +, -, *, /, //, %, **
        - Bitové: &, |, ^, ~, <<, >>
        - Porovnávací: ==, !=, <, >, <=, >=

    Kompatibilita:
        - bool je podtřídou int (True je 1, False je 0)
        - float lze zaokrouhlit na int, ale validátor vyžaduje přímo int hodnoty

    Běžné chyby:
        - Použití float místo int, např. 42.0 místo 42
        - Použití hodnot převeditelných na int (str hodnota "42")
        - Očekávání přenosu z jiných typů (např. že float 3.14 bude přijat jako int)
        - Zapomenutí, že dělení (/) vždy vrací float, i když výsledek je celé číslo

    Reference:
        - https://docs.python.org/3/library/functions.html#int
        - https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
    """

    VALIDATOR_KEY = "int"
    ANNOTATION = int
    INFO = "Definuje, že hodnota může být pouze celé číslo"
    ORIGIN = int