from ...._exceptions import VerifyNotImplementedAttributeError
from ._required_attributes import REQUIRED_ATTRIBUTES


def attributes_check(cls):
    """
    Kontroluje přítomnost všech povinných atributů BaseValidator v potomcích.

    Tato funkce ověřuje, zda validační třída definuje všechny požadované atributy,
    které jsou nezbytné pro správné fungování validačního systému. Pokud nějaký
    atribut chybí, vyvolá výjimku s podrobným popisem problému.

    Funkce je definována mimo třídu BaseValidator, aby zbytečně nezatěžovala
    potomky a umožnila izolaci této kontrolní logiky.

    Args:
        cls (class): Třída k ověření

    Raises:
        VerifyNotImplementedAttributeError: Pokud některý z povinných atributů chybí
    """
    missing = [attr for attr in REQUIRED_ATTRIBUTES if not hasattr(cls, attr)]
    if missing:
        raise VerifyNotImplementedAttributeError(
            cls.__name__,
            missing,
            REQUIRED_ATTRIBUTES
        )