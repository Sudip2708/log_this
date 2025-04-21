from .._base_type_validator import BaseTypeValidator


class ComplexValidator(BaseTypeValidator):
    """
    Validátor pro typovou anotaci complex

    Complex reprezentuje komplexní číslo v Pythonu, které obsahuje reálnou a imaginární část.
    Komplexní čísla jsou používána především ve vědeckých výpočtech, zpracování signálů,
    elektrotechnice a v matematických operacích vyžadujících práci s imaginární jednotkou.

    Syntaxe:
        - complex    # Přímý zápis typu

    Příklady použití:
        - complex    # Komplexní číslo ve formátu a+bj

    Validační proces:
        1. Ověřuje, zda hodnota je instance typu complex
        2. Kontroluje, že hodnota je přímo objekt typu complex, nikoliv hodnoty,
           které lze na complex převést

    Použití v kódu:
        - Pro parametry funkcí: def process_signal(wave: complex) -> None
        - Pro návratové hodnoty: def calculate_impedance() -> complex
        - Pro typování proměnných: c: complex = 3+4j

    Vytváření complex hodnot:
        - Přímý zápis: 1+2j, 3.14-2.5j, 0j
        - Pomocí konstruktoru: complex(1, 2)  # vytvoří 1+2j
        - Převodem z řetězce: complex("1+2j")

    Operace:
        - Aritmetické operace: +, -, *, /, **
        - Atributy: z.real (reálná část), z.imag (imaginární část)
        - Metody: z.conjugate() (komplexně sdružené číslo)

    Omezení:
        - Komplexní čísla nemají přirozené uspořádání (nelze použít <, >, <=, >=)
        - Nelze převést na int nebo float
        - Nelze použít matematické funkce vyžadující uspořádání (min, max)

    Běžné chyby:
        - Záměna zápisu imaginární jednotky (j místo i v matematice)
        - Vynechání "j" při zápisu komplexního čísla
        - Pokus použít komplexní číslo tam, kde se očekává float nebo int
        - Pokus porovnávat komplexní čísla pomocí relačních operátorů

    Reference:
        - https://docs.python.org/3/library/functions.html#complex
        - https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
    """

    VALIDATOR_KEY = "complex"
    ANNOTATION = complex
    INFO = "Definuje, že hodnota může být pouze komplexní číslo"
    ORIGIN = complex