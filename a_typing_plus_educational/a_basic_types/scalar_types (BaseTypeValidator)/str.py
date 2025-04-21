from .._base_type_validator import BaseTypeValidator


class StrValidator(BaseTypeValidator):
    """
    Validátor pro typovou anotaci str
 
    Str reprezentuje textový řetězec v Pythonu. Je to sekvence Unicode znaků (code points),
    která podporuje širokou škálu operací pro manipulaci s textem. Řetězce v Pythonu jsou
    immutable (neměnné), což znamená, že po vytvoření nelze jejich obsah měnit.
 
    Syntaxe:
        - str    # Přímý zápis typu
 
    Příklady použití:
        - str    # Libovolný textový řetězec
 
    Validační proces:
        1. Ověřuje, zda hodnota je instance typu str
        2. Kontroluje, že hodnota je skutečně objekt typu str, nikoliv jiné objekty,
           které lze na řetězec převést pomocí str()
 
    Použití v kódu:
        - Pro parametry funkcí: def greet(name: str) -> str
        - Pro návratové hodnoty: def get_username() -> str
        - Pro typování proměnných: message: str = "Hello, world"
 
    Vytváření řetězců:
        - Pomocí uvozovek: "text", 'text', '''víceřádkový text'''
       - Pomocí konstruktoru: str(42), str(True)
       - Formátované řetězce: f"Hodnota je {value}"
       - Spojování řetězců: "Hello" + " " + "world"

   Operace:
       - Indexování a krájení: text[0], text[1:5]
       - Spojování: "a" + "b", "".join(["a", "b", "c"])
       - Hledání: "abc".find("b"), "abc".index("b")
       - Nahrazování: "abc".replace("a", "x")
       - Rozdělování: "a,b,c".split(",")
       - Testování: text.startswith("A"), text.endswith(".txt"), "x" in text

   Kompatibilita:
       - str není kompatibilní s bytes (pro kódované binární data)
       - str není kompatibilní s numeric typy, ačkoli může obsahovat číselné znaky

   Běžné chyby:
       - Zaměňování str a bytes pro binární data
       - Použití číselných hodnot nebo jiných typů místo řetězců tam, kde je očekáván str
       - Ignorování rozdílu mezi str a char (v Pythonu neexistuje samostatný typ pro znak)
       - Modifikace řetězců "na místě" (str je immutable, vše vytváří nový řetězec)

   Reference:
       - https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
       - https://docs.python.org/3/library/functions.html#func-str
       - https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
   """

    VALIDATOR_KEY = "str"
    ANNOTATION = str
    INFO = "Definuje, že hodnota může být pouze řetězec"
    ORIGIN = str