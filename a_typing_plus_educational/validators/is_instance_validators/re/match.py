from re import Match

from ...._bases import BaseIsInstanceValidator


class MatchValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci re.Match

    Typ re.Match reprezentuje objekt shody vytvořený úspěšným vyhledáváním nebo porovnáváním
    pomocí regulárních výrazů v Pythonu. Obsahuje informace o tom, kde byla shoda nalezena,
    které skupiny byly zachyceny a další detaily o výsledku operace regulárního výrazu.

    Syntaxe:
        - Match                # Vyžaduje import z modulu re (from re import Match)
        - re.Match             # Alternativní zápis (import re)

    Příklady použití:
        - def process_match(match: Match) -> str:
        - def find_pattern(text: str) -> Match | None:
        - result: Match = re.search(r'pattern', string)

    Implementační detaily:
        Match objekt není určen k přímému vytváření uživatelem, ale je vrácen funkcemi modulu re
        jako re.search(), re.match() nebo re.fullmatch(). Obsahuje metody a atributy pro přístup
        k detailům o nalezené shodě.

    Validační proces:
        1. Ověří, zda hodnota je instance typu re.Match
        2. Validace probíhá pomocí isinstance(value, re.Match)

    Použití v kódu:
        - Pro parametry funkcí: def extract_data(m: Match) -> str:
        - Pro návratové hodnoty: def find_all_matches(text: str) -> List[Match]:
        - Pro typování proměnných: match_result: Match = re.search(pattern, text)

    Důležité atributy a metody objektu Match:
        - match.group([group1, ...]) - Vrátí jednu nebo více podskupin shody
        - match.groups() - Vrátí tuple obsahující všechny podskupiny shody
        - match.groupdict() - Vrátí slovník pojmenovaných podskupin
        - match.start([group]) - Vrátí počáteční pozici shody nebo skupiny
        - match.end([group]) - Vrátí koncovou pozici shody nebo skupiny
        - match.span([group]) - Vrátí dvojici (start, end) pro shodu nebo skupinu
        - match.string - Původní řetězec, ve kterém byla nalezena shoda
        - match.re - Regulární výraz, který byl použit pro nalezení shody

    Běžné chyby:
        - Zapomenutí kontroly, zda funkce vrátila Match nebo None
        - Pokusy o přímé vytvoření Match objektu (nelze vytvořit přímo, pouze získat z re funkcí)
        - Záměna s re.Pattern objektem, který představuje zkompilovaný regex vzor

    Reference:
        - https://docs.python.org/3/library/re.html#match-objects
        - https://docs.python.org/3/library/re.html#regular-expression-objects
    """

    VALIDATOR_KEY = "match"
    ANNOTATION = Match

    IS_INSTANCE = Match
    DUCK_TYPING = {
        "has_callable_attr": ("group", "groups", "groupdict"),
    }

    DESCRIPTION = "Výsledek shody regulárního výrazu"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí re.Match, "
            "tedy výsledkem úspěšného vyhledání vzoru pomocí regulárního výrazu. "
            "Obsahuje informace o nalezené shodě, včetně pozice a skupin."
        )
