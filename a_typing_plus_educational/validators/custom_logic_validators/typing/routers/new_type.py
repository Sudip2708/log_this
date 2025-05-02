from typing import NewType

from ...._bases import BaseCustomLogicValidator
from ...._verifiers import inner_args_transmitter_for_newtype


class NewTypeValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci NewType

    NewType je funkce, která vytváří odlišné typy odvozené od existujících typů. 
    Slouží k vytváření nominálních typů, které jsou na úrovni typové kontroly 
    odlišné od svého základu, ale na úrovni runtime jsou identické s původním typem.

    Syntaxe:
        - UserId = NewType('UserId', int)       # Vytvoření nového typu
        - def func(user_id: UserId): ...        # Použití typu v anotaci

    Příklady použití:
        - UserId = NewType('UserId', int)       # ID uživatele jako speciální typ celého čísla
        - Email = NewType('Email', str)         # E-mail jako speciální typ řetězce
        - Vector = NewType('Vector', List[float]) # Vektor jako speciální typ seznamu

    Validační proces:
        1. Získání nadřazeného typu z NewType anotace pomocí __supertype__ atributu
        2. Rekurzivní validace hodnoty vůči tomuto nadřazenému typu
        3. NewType samotný nepřidává další validační podmínky na hodnotu

    Použití v kódu:
        ```python
        # Definice typů
        UserId = NewType('UserId', int)
        AdminId = NewType('AdminId', UserId)  # Lze řetězit
        
        # Použití
        def get_user(user_id: UserId) -> User:
            ...
            
        # Vytvoření hodnoty daného typu
        user_id = UserId(42)  # Vytvoří UserId
        ```

    Specifické informace:
        - Nominální vs. strukturální typování: NewType umožňuje nominální typování,
          kde dva typy se stejnou strukturou jsou považovány za různé
        - Řetězení: Lze vytvářet hierarchii typů (AdminId odvozený od UserId)
        - Runtime chování: Na runtime úrovni je NewType transparentní - hodnota je 
          stejného typu jako původní typ
        - Kompatibilita s mypy: Statické analyzátory jako mypy kontrolují, aby se
          nepoužily zaměnitelně typy, které jsou sice strukturálně stejné, ale 
          sémanticky odlišné

    Běžné chyby:
        - Záměna s podtřídou: NewType nevytváří skutečnou podtřídu, pouze typ pro statickou kontrolu
        - Předpoklad nové funkcionality: NewType nepřidává žádné metody ani neprovádí validaci
        - Zmatek s isinstance: isinstance(UserId(5), int) vrátí True, ale isinstance(5, UserId) není validní
        - Použití bez volání konstruktoru: user_id: UserId = 5 mine typovou kontrolu, musí být UserId(5)

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.NewType
        - https://peps.python.org/pep-0484/#newtype-helper-function
        - https://mypy.readthedocs.io/en/stable/more_types.html#newtype
    """

    VALIDATOR_KEY = "newtype"
    ANNOTATION = NewType

    IS_INSTANCE = NewType
    HAS_ATTRS = None  # Nepodporuje validaci přes Duck Typing.
    CALLABLE_ATTRS = None  # Nepodporuje validaci přes Duck Typing.

    DESCRIPTION = "Alias pro nový typ založený na existujícím"
    LONG_DESCRIPTION = (
            "Validuje, že typ byl vytvořen pomocí NewType, "
            "tedy jako nový typ odvozený z jiného, "
            "aby bylo možné odlišit jejich použití při statické kontrole typů."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Definice metody __call__ pro přeformulování dotazu."""
        
        return inner_args_transmitter_for_newtype(
            value, annotation, depth_check, custom_types, bool_only
        )