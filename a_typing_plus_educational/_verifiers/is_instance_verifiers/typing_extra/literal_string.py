from typing import LiteralString

from ..._bases import IsInstanceValidatorBase


class LiteralStringValidator(IsInstanceValidatorBase):
    """
    Validátor pro typovou anotaci LiteralString

    LiteralString je speciální anotace zavedená v PEP 675, která označuje řetězce, jež
    jsou literály nebo pocházejí z literálů. Slouží především k prevenci SQL injection
    a podobných bezpečnostních zranitelností.

    Syntaxe:
        - LiteralString  # Označuje řetězec, který je staticky známý v době kompilace

    Důležité omezení:
        V runtime NELZE zjistit, zda byl string zadán jako literál, nebo je výsledkem
        dynamického výpočtu. Proto tento validátor pouze ověřuje, že hodnota je typu `str`.
        Skutečná kontrola "statičnosti" řetězce je možná pouze pomocí statických analyzátorů
        jako mypy nebo pyright.

    Příklady použití:
        - LiteralString                     # Řetězec, který je literálem
        - def query(sql: LiteralString)     # Funkce přijímající pouze bezpečné SQL dotazy
        - data: Dict[str, LiteralString]    # Slovník s bezpečnými řetězcovými hodnotami

    Co je a co není LiteralString:
        - JE: "text"                        # Statický literál
        - JE: "prefix" + "suffix"           # Konkatenace literálů
        - JE: f"hodnota {123}"              # f-string s literály
        - NENÍ: user_input                  # Hodnota získaná za běhu
        - NENÍ: f"hodnota {user_input}"     # f-string s dynamickými hodnotami
        - NENÍ: "text".replace("e", "a")    # Výsledek operace na řetězci

    Validační proces:
        1. Kontroluje pouze, zda je hodnota instance typu str
        2. V tomto validátoru nelze runtime ověřit "statičnost" řetězce
        3. Pro úplnou validaci musí být použity statické analyzátory kódu

    Použití v kódu:
        - Pro parametry funkcí pracujících s databází:
          def execute_query(sql: LiteralString) -> None
        - Pro zabezpečené API:
          def process_command(cmd: LiteralString) -> None
        - Pro bezpečné generování kódu:
          def generate_code(template: LiteralString) -> str

    Bezpečnostní aspekty:
        - Pomáhá předcházet zranitelnostem typu SQL injection, XSS, command injection
        - Vynucuje, aby dynamický obsah procházel samostatnou validací/escapováním
        - Umožňuje statickým analyzátorům identifikovat potenciálně nebezpečné užití

    Kdy používat:
        - Pro parametry funkcí pracujících s interprety (SQL, shell, HTML)
        - Pro zabezpečení kritických částí aplikace
        - Pro prevenci zranitelností způsobených neošetřeným vstupem

    Běžné chyby:
        - Spoléhání se jen na tuto runtime kontrolu bez statické analýzy
        - Mylné přesvědčení, že typ zaručuje bezpečnost za běhu
        - Používání pro nekritické nebo neinterpretované řetězce

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.LiteralString
        - https://peps.python.org/pep-0675/ (Arbitrary Literal String Type)
        - https://mypy.readthedocs.io/en/stable/literal_strings.html
    """

    VALIDATOR_KEY = "literalstring"
    ANNOTATION = LiteralString
    INFO = "Ověří, že hodnota je typu string (LiteralString)"
    ORIGIN = str