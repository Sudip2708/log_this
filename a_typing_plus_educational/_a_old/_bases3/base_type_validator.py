from typing import Any, Tuple, Union

from ._base_validator import BaseValidator
from ...validators import validate_native_type


class BaseTypeValidator(BaseValidator):
    """
    Základní třída pro validační třídy, které provádějí jednoduchou validaci základního typu.

    Tato třída slouží jako společný základ pro validátory, jejichž cílem je ověření
    základního typu hodnoty pomocí isinstance nebo podobného mechanismu.

    Příkladové použití ve třídách:
        - AnyValidator (any.py) – přepisuje validační logiku
        - CallableValidator (callable.py) – přepisuje validační logiku
        - LiteralValidator (literal.py) – přepisuje validační logiku
        - LiteralStringValidator (literal_string.py)
        - TypeValidator (type.py) – přepisuje validační logiku
    """

    def __call__(
        self,
        value: Any,
        annotation: Any,
        inner_check: Union[bool, int],
        custom_types: dict = None,
        bool_only: bool
    ) -> Union[bool, Any]:
        """
        Provádí základní typovou validaci hodnoty.

        Typická kontrola probíhá pomocí isinstance(value, self.ORIGIN).

        Args:
            value (Any): Vstupní hodnota k validaci.
            annotation (Any): Typová anotace, např. `int`, `str`, ...
            inner_check (Union[bool, int]): Hloubka kontroly nebo True/False.
            custom_types (Tuple[Any, ...]): N-tice uživatelsky definovaných typů.
            bool_only (bool): Pokud je True, výstup je pouze True/False; jinak se vrací výjimka při chybě.

        Returns:
            bool | Any: True při úspěšné validaci, jinak vyvolá výjimku nebo vrátí False.
        """
        return validate_native_type(value, self.ORIGIN, bool_only)
