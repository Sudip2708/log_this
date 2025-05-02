from typing import ClassVar

from ....._bases import BaseCustomLogicValidator, T
from ....._verifiers import inner_args_transmitter

class ClassVarValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci ClassVar[T]

    ClassVar je typová anotace, která označuje třídní proměnné v třídách. Používá se
    pro odlišení třídních atributů od instančních v kontextu typové kontroly, zejména
    v dataclasses a podobných konstrukcích. ClassVar neprovádí žádnou validaci samotnou,
    ale pouze označuje, že daná proměnná je zamýšlena jako atribut třídy, ne instance.

    Syntaxe:
        - ClassVar[T]           # T je vnitřní typ proměnné
        - ClassVar              # Bez specifikace typu (ekvivalent ClassVar[Any])

    Příklady použití:
        - ClassVar[int]         # Třídní proměnná typu int
        - ClassVar[List[str]]   # Třídní proměnná typu seznam řetězců
        - ClassVar              # Třídní proměnná bez specifikace typu

    Validační proces:
        1. Získání vnitřního typu T z anotace ClassVar[T]
        2. Rekurzivní validace hodnoty vůči vnitřnímu typu T
        3. ClassVar samotný nepřidává žádné další validační podmínky

    Použití v kódu:
        ```python
        class Config:
            DEBUG: ClassVar[bool] = True  # Třídní konstanta
            counter: ClassVar[int] = 0    # Třídní proměnná sdílená všemi instancemi

            name: str                     # Instanční proměnná (není ClassVar)
        ```

    Specifické informace:
        - Vztah k dataclasses: ClassVar je zvláště užitečný v dataclasses pro označení,
          které proměnné se nemají stát součástí __init__
        - Rozdíl od Final: ClassVar definuje úroveň sdílení (třída vs. instance),
          zatímco Final definuje mutabilitu
        - Kontrola validátory: Nástroje jako mypy budou varovat, pokud je ClassVar použit
          pro instanční proměnnou nebo pokud je instanční proměnná použita tam, kde se
          očekává ClassVar
        - Runtime význam: ClassVar má význam pouze při typové kontrole, při běhu
          programu nemá žádný speciální efekt

    Běžné chyby:
        - Nesprávné pochopení: ClassVar nezabraňuje vytvoření instanční proměnné
          stejného jména, pouze označuje záměr
        - Záměna s Final: ClassVar a Final mají odlišné účely a mohou být kombinovány
        - Použití v nevhodném kontextu: ClassVar nedává smysl mimo definici třídy
        - Kombinace s property: ClassVar se nepoužívá s @property dekorátorem

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.ClassVar
        - https://peps.python.org/pep-0526/#class-and-instance-variable-annotations
        - https://docs.python.org/3/library/dataclasses.html#dataclasses.field
    """

    VALIDATOR_KEY = "classvar"
    ANNOTATION = ClassVar[T]

    IS_INSTANCE = ClassVar
    HAS_ATTRS = None  # Nepodporuje validaci přes Duck Typing
    CALLABLE_ATTRS = None  # Nepodporuje validaci přes Duck Typing

    DESCRIPTION = "Proměnná třídy (ne instance)"
    LONG_DESCRIPTION = (
            "Validuje, že typ označuje ClassVar, tedy proměnnou sdílenou "
            "mezi všemi instancemi třídy, nikoliv instanční atribut."
        )

    def __call__(self, value, annotation, depth_check, custom_types,
                 bool_only):
        """Definice metody __call__ pro přeformulování dotazu.

        Předává validaci vnitřnímu typu anotace ClassVar.
        """
        return inner_args_transmitter(
            value, annotation, depth_check, custom_types, bool_only
        )