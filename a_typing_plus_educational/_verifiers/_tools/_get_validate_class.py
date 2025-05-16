"""
!!! Potřeba doplnit definice obsahu obou slovníků !!!
"""

from typing import Any, get_origin, Optional, Callable
import functools


class GetValidateClass:
    """
    Třída definující metodu pro navrácení třídy s validačními instrukcemi.

    Třídu používá funkce typing_verifier pro načtení validační třídy.
    """

    # Definice základních slovníků
    VALIDATORS_DICT = {}
    VALIDATORS_GET_ORIG_DICT = {}

    def __call__(
            self,
            annotation: Any
    ) -> Optional[Callable]:
        """Vrací validační třídu podle anotace (nejprve přes `origin`, pak podle klíče)."""
        return (
            self.get_origin_validate_class(annotation)
            or self.get_key_validate_class(annotation)
        )

    @staticmethod
    @functools.lru_cache(maxsize=1024)
    def get_annotation_key(
            annotation: Any
    ) -> str:
        """Vrací zjednodušený klíč typu z anotace pomocí split metod."""
        s = str(annotation)
        s = s.split('[', 1)[0]
        s = s.rsplit('.', 1)[-1]
        return s.strip().lower()

    def get_origin_validate_class(
            self,
            annotation: Any
    ) -> 'Optional[Callable]':
        """Vrací validační třídu na základě generického typu (např. list, dict)."""
        origin = get_origin(annotation)
        return (
            self.VALIDATORS_GET_ORIG_DICT.get(origin)
            if origin else None
        )

    def get_key_validate_class(
            self,
            annotation: Any
    ) -> 'Optional[Callable]':
        """Vrací validační třídu podle řetězcového klíče."""
        key = self.get_annotation_key(annotation)
        return self.VALIDATORS_DICT.get(key, None)


# Singleton vzor funkce
get_validate_class = GetValidateClass()