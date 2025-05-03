from typing import TypeVar

from ....._bases import BaseCustomLogicValidator
from ....._verifiers import typevar_verifier


class TypeVarValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci TypeVar

    TypeVar je základním stavebním kamenem generického programování v Pythonu, který umožňuje
    definovat generické typy pro funkce a třídy. Pomocí TypeVar lze vytvářet parametrizované
    typy, které mohou být specifikovány při použití, a tím zajistit typovou bezpečnost
    pro obecné algoritmy a datové struktury.

    Syntaxe:
        - T = TypeVar('T')                        # Základní definice bez omezení
        - T = TypeVar('T', bound=BaseClass)       # Omezení na podtřídy BaseClass
        - T = TypeVar('T', int, str)              # Omezení na konkrétní typy
        - T = TypeVar('T', covariant=True)        # Kovariantní typová proměnná
        - T = TypeVar('T', contravariant=True)    # Kontravariantní typová proměnná

    Příklady použití:
        - V definici generických funkcí:
          ```python
          T = TypeVar('T')
          def first(lst: List[T]) -> T: return lst[0]
          ```
        - V definici generických tříd:
          ```python
          T = TypeVar('T')
          class Box(Generic[T]):
              def __init__(self, value: T): self.value = value
              def get(self) -> T: return self.value
          ```
        - S omezením:
          ```python
          T = TypeVar('T', int, str)
          def process(x: T) -> T: return x  # x může být jen int nebo str
          ```

    Parametry TypeVar:
        - name (str): Jméno typové proměnné (musí odpovídat názvu proměnné)
        - *constraints: Volitelný seznam typů, které omezují možné hodnoty TypeVar
        - bound: Volitelný horní limit typu (typová proměnná musí být podtřídou tohoto typu)
        - covariant: Určuje, zda je typová proměnná kovariantní
        - contravariant: Určuje, zda je typová proměnná kontravariantní

    Validační proces:
        Validace TypeVar je specifická, protože TypeVar sám o sobě není hodnotou, kterou lze
        validovat, ale typovým konstruktem používaným během statické typové kontroly.
        1. Pokud je TypeVar použit přímo jako anotace (což je neobvyklé), lze ověřit pouze
           základní kompatibilitu s příslušnými omezeními.
        2. Pokud je TypeVar použit jako součást generického typu, validace závisí na konkrétní
           specifikaci generického typu v daném kontextu.

    Specifické vlastnosti:
        - TypeVar je určen pro definici generických typů, ne pro přímé použití jako anotace
        - V rámci jedné funkce/třídy může stejná instance TypeVar reprezentovat různé typy
        - TypeVar může být omezen na konkrétní typy nebo na hierarchii typů (bound)
        - TypeVar může definovat variantnost (covariant, contravariant)

    Variantnost TypeVar:
        - Kovariantní (covariant=True): Pokud je B podtypem A, pak je Container[B] podtypem Container[A]
        - Kontravariantní (contravariant=True): Pokud je B podtypem A, pak je Container[A] podtypem Container[B]
        - Invariantní (výchozí): Container[A] a Container[B] nejsou vzájemně kompatibilní, pokud A ≠ B

    Běžné vzory použití:
        - Generické datové struktury (stromy, seznamy, grafy)
        - Generické algoritmy pracující s různými typy dat
        - Typově bezpečné tovární funkce a metody
        - Definice protokolů a rozhraní

    Běžné chyby:
        - Použití TypeVar přímo jako anotace místo vytvoření generického typu
        - Definice TypeVar s jiným názvem než je proměnná (T = TypeVar('U'))
        - Použití constrains a bound současně (nelze kombinovat)
        - Nesprávné pochopení variantnosti (covariant vs contravariant)
        - Nekonzistentní použití stejného TypeVar v rámci jedné funkce

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.TypeVar
        - https://peps.python.org/pep-0484/ (Type Hints)
        - https://mypy.readthedocs.io/en/stable/generics.html
    """

    VALIDATOR_KEY = "typevar"
    ANNOTATION = TypeVar  # T = TypeVar('T')

    IS_INSTANCE = TypeVar
    DUCK_TYPING = None

    DESCRIPTION = "Typový parametr"
    LONG_DESCRIPTION = (
            "Validuje, že typ je TypeVar, což umožňuje definici generických tříd "
            "a funkcí s proměnnými typy."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Definice metody __call__ pro ověření volatelnosti objektu."""

        return typevar_verifier(
            value, annotation, depth_check, bool_only
        )
