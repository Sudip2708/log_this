from typing import get_args, Any, Tuple, Union

from ._base_validator import BaseValidator
from ...validators import validate_typing


class BaseGenericValidator(BaseValidator):
    """
    Základní třída pro generické anotace z modulu `typing`.

    Slouží pro validátory, které zpracovávají komplexní nebo složené typy jako:
        - Annotated
        - Optional
        - Union

    Zajišťuje vytažení vnitřních typů a předání dál validační metodě.
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
        Provádí validaci generických typů z `typing`, jako je Union, Optional, Annotated.

        Extrahuje interní typy z anotace a předává je dál validačnímu mechanismu.

        Args:
            value (Any): Hodnota, kterou validujeme.
            annotation (Any): Typová anotace (např. `Union[int, str]`).
            inner_check (Union[bool, int]): Hloubka kontroly nebo True/False.
            custom_types (Tuple[Any, ...]): N-tice vlastních nebo specifických typů.
            bool_only (bool): Výstup jako True/False nebo vyhození výjimky při chybě.

        Returns:
            bool | Any: True při úspěšné validaci, jinak výjimka nebo False.
        """

        inner_args = get_args(annotation)

        return validate_typing(
            value, inner_args, inner_check, custom_types, bool_only
        )
