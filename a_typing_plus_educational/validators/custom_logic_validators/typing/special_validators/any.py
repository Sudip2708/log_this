from typing import Any

from ....._bases import BaseCustomLogicValidator


class AnyValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci Any

    Any reprezentuje speciální "únikový" typ, který je kompatibilní s jakýmkoliv jiným typem.
    Použití Any efektivně vypíná typovou kontrolu pro danou hodnotu nebo proměnnou.

    Syntaxe:
        - Any    # Vyžaduje import z typing

    Příklady použití:
        - Any                   # Libovolný typ hodnoty
        - Dict[str, Any]        # Slovník s řetězcovými klíči a libovolnými hodnotami
        - List[Any]             # Seznam prvků libovolného typu
        - Callable[..., Any]    # Funkce s libovolnými parametry a libovolnou návratovou hodnotou

    Chování:
        - Any je kompatibilní s KAŽDÝM typem v obou směrech:
          * Libovolná hodnota může být přiřazena proměnné typu Any
          * Hodnota typu Any může být přiřazena proměnné jakéhokoliv typu
        - Any se "propaguje" - operace s hodnotou typu Any obvykle vytvoří další Any

    Validační proces:
        - Pro Any validace VŽDY uspěje, bez ohledu na skutečnou hodnotu
        - Hloubková kontrola se u Any neprovádí, protože akceptuje vše

    Použití v kódu:
        - Pro parametry, kde nechceme omezit typ: def process(data: Any) -> None
        - Pro heterogenní kolekce: items: List[Any] = [1, "text", True, [1, 2]]
        - Pro parametry, které přijímají nebo vracejí hodnoty neznámého typu

    Kdy používat:
        - Při práci s kódem, který nemá typové anotace
        - Pro hodnoty, jejichž typ nelze předem určit
        - Při postupném zavádění typových anotací do projektu
        - V generickém kódu, který musí pracovat s libovolnými typy

    Kdy NEpoužívat:
        - Kdykoli je možné použít konkrétnější typ
        - Pro obcházení problémů s typovou kontrolou (lepší je Union/Optional)
        - Pro náhradu za Union[T1, T2, ...] když známe možné typy

    Dobré praktiky:
        - Omezit použití Any na minimum
        - Preferovat Union nebo TypeVar pro případy, kdy potřebujeme flexibilitu
        - Používat cast() pro bezpečné konverze z Any na konkrétní typy

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Any
        - https://mypy.readthedocs.io/en/stable/dynamic_typing.html
    """

    VALIDATOR_KEY = "any"
    ANNOTATION = Any

    IS_INSTANCE = Any
    DUCK_TYPING = None

    DESCRIPTION = "Libovolný typ"
    LONG_DESCRIPTION = (
            "Validuje, že typ je Any, tedy že hodnota může být libovolného typu. "
            "Používá se tam, kde není žádné omezení."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        # Any podporuje všechny hodnoty, takže je vždy True
        return True
