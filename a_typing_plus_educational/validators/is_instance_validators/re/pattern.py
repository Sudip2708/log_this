from re import Pattern

from ...._bases import BaseIsInstanceValidator


class PatternValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci re.Pattern

    Typ re.Pattern reprezentuje zkompilovaný objekt regulárního výrazu v Pythonu,
    který umožňuje efektivní opakované vyhledávání a porovnávání vzorů v textu.
    Zkompilovaný vzor obsahuje optimalizovanou reprezentaci regulárního výrazu,
    která je připravena pro rychlé operace nad řetězci.

    Syntaxe:
        - Pattern                # Vyžaduje import z modulu re (from re import Pattern)
        - re.Pattern             # Alternativní zápis (import re)

    Příklady použití:
        - def validate_with_regex(pattern: Pattern, text: str) -> bool:
        - def compile_regex(expression: str) -> Pattern:
        - compiled_regex: Pattern = re.compile(r'[a-z]+')

    Implementační detaily:
        Pattern objekt je vytvářen funkcí re.compile() a obsahuje vnitřní optimalizovanou
        reprezentaci regulárního výrazu. Objekty Pattern jsou znovupoužitelné a umožňují
        efektivní provádění operací nad řetězci bez nutnosti opakované kompilace vzoru.

    Validační proces:
        1. Ověří, zda hodnota je instance typu re.Pattern
        2. Validace probíhá pomocí isinstance(value, re.Pattern)

    Použití v kódu:
        - Pro parametry funkcí: def extract_data(regex: Pattern, text: str) -> List[str]:
        - Pro návratové hodnoty: def create_validator() -> Pattern:
        - Pro typování proměnných: email_regex: Pattern = re.compile(r'[^@]+@[^@]+\.[^@]+')

    Důležité metody objektu Pattern:
        - pattern.search(string) - Vyhledává shodu kdekoli v řetězci, vrací Match nebo None
        - pattern.match(string) - Testuje shodu na začátku řetězce, vrací Match nebo None
        - pattern.fullmatch(string) - Testuje shodu celého řetězce, vrací Match nebo None
        - pattern.findall(string) - Vrátí seznam všech nepřekrývajících se shod
        - pattern.finditer(string) - Vrátí iterátor přes všechny nepřekrývající se Match objekty
        - pattern.split(string) - Rozdělí řetězec podle výskytů vzoru
        - pattern.sub(repl, string) - Nahradí výskyty vzoru v řetězci

    Důležité atributy:
        - pattern.pattern - Řetězec reprezentující původní vzor regulárního výrazu
        - pattern.flags - Příznaky použité při kompilaci vzoru
        - pattern.groups - Počet skupin závorek v regulárním výrazu
        - pattern.groupindex - Slovník mapující názvy skupin na jejich indexy

    Srovnání s přímým použitím funkcí re:
        Pattern objekty jsou efektivnější při opakovaném použití, protože se vzor kompiluje
        pouze jednou, zatímco funkce jako re.search() nebo re.match() kompilují vzor při
        každém volání, pokud není již uložen v interní cache.

    Běžné chyby:
        - Zapomenutí importu: from re import Pattern
        - Záměna s re.Match objektem, který představuje výsledek hledání
        - Zbytečná rekompilace stejného regulárního výrazu

    Reference:
        - https://docs.python.org/3/library/re.html#regular-expression-objects
        - https://docs.python.org/3/library/re.html#re.compile
    """

    VALIDATOR_KEY = "Pattern"
    ANNOTATION = Pattern

    IS_INSTANCE = Pattern
    DUCK_TYPING = {
        "has_callable_attr": ("search", "match", "sub"),
    }

    DESCRIPTION = "Zkompilovaný regulární výraz"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí re.Pattern, "
            "tedy zkompilovaným regulárním výrazem vytvořeným funkcí re.compile(). "
            "Poskytuje metody pro vyhledávání a nahrazování."
        )
