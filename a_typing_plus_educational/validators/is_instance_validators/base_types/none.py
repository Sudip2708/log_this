from ...._bases import BaseIsInstanceValidator


class NoneValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci None

    None reprezentuje v Pythonu prázdnou hodnotu nebo absenci hodnoty. Je to
    speciální konstantní hodnota, která má svůj vlastní typ (NoneType). V Pythonu
    existuje pouze jediná instance None.

    Syntaxe:
        - None    # Přímý zápis hodnoty/typu
        - type(None)  # Technicky přesnější zápis typu

    Příklady použití:
        - None    # Explicitní hodnota None

    Validační proces:
        1. Ověřuje, zda hodnota je přesně instance None
        2. Kontroluje identitu hodnoty (value is None), nikoliv jen ekvivalenci

    Použití v kódu:
        - Pro parametry funkcí: def process(default: None) -> str
        - Pro návratové hodnoty: def initialize() -> None
        - Pro typování proměnných: result: None

    Specifické použití:
        - Pro označení absence návratové hodnoty funkce
        - Pro výchozí hodnoty parametrů funkcí
        - Pro reprezentaci stavu "nic" nebo "nedefinováno"
        - Pro explicitní vyjádření, že funkce pouze vykonává vedlejší efekt

    Kompatibilita:
        - None není kompatibilní s žádným jiným typem
        - None se v podmínkách chová jako False
        - None není prázdný řetězec, nula ani prázdný seznam

    Běžné chyby:
        - Zaměňování None s False, 0, "", [], {} nebo podobnými "prázdnými" hodnotami
        - Kontrola None pomocí == místo is (is je správný způsob kontroly identity)
        - Použití hodnoty None tam, kde se očekává jiný specifický typ
        - Zaměňování None s NaN (Not a Number) pro numerické výpočty

    Reference:
        - https://docs.python.org/3/library/constants.html#None
        - https://docs.python.org/3/library/typing.html#none
        - https://peps.python.org/pep-0484/#using-none
    """

    VALIDATOR_KEY = "none"
    ANNOTATION = None  # Typ None v Pythonu (typ(None))

    IS_INSTANCE = None
    DUCK_TYPING = None

    DESCRIPTION = "Prázdná hodnota"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je None, tedy hodnota reprezentující absenci hodnoty. "
            "V Pythonu existuje pouze jedna instance None, která je singleton."
        )

