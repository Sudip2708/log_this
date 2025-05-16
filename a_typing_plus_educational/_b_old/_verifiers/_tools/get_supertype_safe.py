from typing import Any
from ..._exceptions import AnnotationGetSuperTypeError


def get_supertype_safe(annotation: Any):
    """
    Pomocná interní funkce pro bezpečné získání nadřazeného typu z NewType anotace.

    NewType vytváří podtypy existujících typů, kde skutečný typ je uložen v atributu
    __supertype__. Tato funkce bezpečně extrahuje tento nadřazený typ pro účely validace.

    Args:
        annotation (Any): NewType anotace, z níž se má získat nadřazený typ.

    Returns:
        Any: Nadřazený typ získaný z anotace.

    Raises:
        AnnotationGetSuperTypeError: Pokud se nepodaří z anotace získat nadřazený typ.
    """

    # Pokus o získání __supertype__ atributu
    try:
        return annotation.__supertype__

    # Pokud atribut neexistuje nebo je nepřístupný, převede se na interní výjimku
    except (AttributeError, TypeError) as e:
        raise AnnotationGetSuperTypeError(annotation) from e