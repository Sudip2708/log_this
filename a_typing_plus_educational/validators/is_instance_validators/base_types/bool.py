from ...._bases import BaseIsInstanceValidator


class BoolValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci bool

    Bool reprezentuje logickou hodnotu, která může nabývat pouze dvou stavů: True nebo False.
    Používá se pro reprezentaci pravdivostních hodnot a řízení toku programu v podmínkách.

    Syntaxe:
        - bool    # Přímý zápis typu

    Příklady použití:
        - bool    # Boolean hodnota True nebo False

    Validační proces:
        1. Ověřuje, zda hodnota je instance typu bool
        2. Ujišťuje se, že hodnota je skutečně True nebo False, nikoliv jiný typ
           převeditelný na boolean (jako 1, 0, "", [], atd.)

    Použití v kódu:
        - Pro parametry funkcí: def toggle_feature(enabled: bool) -> None
        - Pro návratové hodnoty: def is_valid() -> bool
        - Pro typování proměnných: active: bool = True

    Převod na bool:
        Python umožňuje implicitní převod mnoha hodnot na bool pomocí bool() funkce,
        ale validátor vyžaduje přímou instanci bool (True/False):
        - False hodnoty: False, None, 0, 0.0, "", [], {}, set()
        - True hodnoty: True, nenulová čísla, neprázdné řetězce a kolekce

    Kompatibilita:
        - bool je subtype int v Pythonu (bool je podtřídou int)
        - True má číselnou hodnotu 1, False má hodnotu 0
        - ale int není kompatibilní s bool pro účely validátoru

    Běžné chyby:
        - Použití hodnot 0/1 místo True/False
        - Očekávání, že hodnoty převeditelné na bool budou platné pro bool anotaci
        - Zaměňování boolean podmínek s bool typem

    Reference:
        - https://docs.python.org/3/library/functions.html#bool
        - https://docs.python.org/3/library/stdtypes.html#boolean-values
    """

    VALIDATOR_KEY = "bool"
    ANNOTATION = bool

    IS_INSTANCE = bool
    DUCK_TYPING = None

    DESCRIPTION = "Logická hodnota"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je typu bool, tedy nabývá hodnoty True nebo False. "
            "Používá se pro reprezentaci pravdivostních hodnot v logických výrazech."
        )

