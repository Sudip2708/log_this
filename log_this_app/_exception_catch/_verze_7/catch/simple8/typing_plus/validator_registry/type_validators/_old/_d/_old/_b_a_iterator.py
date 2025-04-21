from typing import Iterator
from collections.abc import Iterator as ABCIterator

from .._base_type_validator import TypeValidator


class IteratorValidator(TypeValidator):
    """
    Validátor pro zápis Iterator[T]

    Iterator reprezentuje jakýkoli objekt, který implementuje metody __iter__ a __next__
    (získaný funkcí iter(), generátory, atd.).

    Hint:
        Iterator[T] = Libovolný iterátor s prvky typu T
    """

    # Definice klíče pro registr
    VALIDATOR_TYPE = Iterator

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama (origin)
        if not isinstance(value, ABCIterator):
            if bool_only:
                return False
            raise TypeError(
                f"Očekáván iterátor (Iterator), ale obdrženo {type(value).__name__}")

        # U iterátorů nemůžeme provádět hloubkovou kontrolu typů prvků,
        # protože bychom je tím spotřebovali. Proto vždy vracíme True.
        # Poznámka: Mohli bychom zkusit první prvek, ale to by také změnilo stav iterátoru.

        return True