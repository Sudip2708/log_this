import functools
from typing import Any, Optional, Callable, get_origin

from ..._exceptions import VerifyUnexpectedInternalError
from ...validators import validators_orig_dict, validators_dict


class GetValidateClass:
    """Třída zapouzdřující logiku pro získání validační třídy"""

    def __call__(self, annotation: Any) -> Optional[Callable]:
        """Hlavní funkce pro navrácení validační třídy"""

        try:

            # Načtení anotace
            self.annotation = annotation

            # Navrácení validační třídy nebo None
            return self._from_origin() or self._from_key()

        # Zachycení všech neočekávaných výjimek
        except Exception as e:
            raise VerifyUnexpectedInternalError(e) from e

    def _from_origin(self) -> Optional[Callable]:
        """Vrací validační třídu na základě generického typu (např. list, dict)."""
        origin = get_origin(self.annotation)
        return validators_orig_dict.get(origin) if origin else None

    def _from_key(self) -> Optional[Callable]:
        """Vrací validační třídu podle řetězcového klíče."""
        key = self._get_key()
        return validators_dict.get_item(key, None)

    @functools.lru_cache(maxsize=1024)
    def _get_key(self) -> str:
        """Vrací zjednodušený klíč typu z anotace pomocí split metod."""
        s = str(self.annotation)
        s = s.split('[', 1)[0]
        s = s.rsplit('.', 1)[-1]
        return s.strip().lower()


get_validate_class = GetValidateClass()