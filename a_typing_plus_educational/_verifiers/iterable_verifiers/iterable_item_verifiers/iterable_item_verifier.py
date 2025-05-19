from typing import Any, Dict, Optional, Tuple, Union

from ..._exceptions_base import (
    VerifyError,
    VerifyUnexpectedInternalError
)
from .._exceptions import VerifyInnerCheckError
from .._tools import (
    get_args_safe,
    verify_base_type,
    verify_iterable_items
)


def iterable_item_verifier(
    value: Any,
    expected_type: Union[type, Tuple[type, ...]],
    duck_typing_instructions: Dict[str, Any],
    annotation: Any = None,
    custom_types: Optional[dict] = None,
    inner_check: Union[bool, int] = True,
    duck_typing: bool = False,
    bool_only: bool = False
) -> bool:
    """
    Validuje, zda je zadaná hodnota iterovatelná určitého typu a případně ověřuje i typy jejích prvků.

    Tato funkce slouží k validaci struktur jako `list`, `tuple`, `set` apod. Nejprve ověřuje,
    zda hodnota odpovídá očekávanému základnímu typu pomocí `is_instance_verifier` nebo
    alternativně přes duck typing. Následně může rekurzivně ověřovat i jednotlivé prvky v iterovatelné
    struktuře dle typové anotace (`annotation`) a předaných parametrů.

    Vnitřní kontrola se řídí parametrem `inner_check`:
        - `False`: Vnitřní typová kontrola se zcela přeskočí.
        - `True`: Vnitřní kontrola se provádí bez omezení hloubky (každý prvek bude validován).
        - `int > 0`: Definuje maximální hloubku rekurze; s každou úrovní se snižuje o 1.

    Pokud validace základního typu selže, výstup závisí na příznaku `bool_only`. Pokud je `True`,
    funkce vrací `False`, jinak vyvolá výjimku. Totéž platí pro vnitřní kontrolu. Pokud vnitřní
    kontrola selže a základní typ je platný, vyvolá se specifická výjimka `VerifyInnerCheckError`.

    Args:
        value (Any): Hodnota, která má být ověřena.
        expected_type (Union[type, Tuple[type, ...]]): Požadovaný základní typ (např. `list`, `tuple`, ...).
        duck_typing_instructions (Dict[str, Any]): Instrukce pro duck typing (např. metody, atributy).
        annotation (Any, optional): Typová anotace prvků uvnitř struktury (např. `List[int]` → `int`).
        custom_types (Optional[dict]): Uživatelsky definované typy a jejich validátory.
        inner_check (Union[bool, int]): Řídí vnitřní kontrolu:
            - `False`: žádná vnitřní kontrola.
            - `True`: rekurze bez omezení hloubky.
            - `int`: maximální hloubka rekurze.
        duck_typing (bool): Pokud `True`, preferuje duck typing validaci před klasickým `isinstance`.
        bool_only (bool): Pokud `True`, namísto výjimek funkce vrací pouze `True/False`.

    Returns:
        bool: `True`, pokud validace proběhne úspěšně.
              `False`, pokud validace selže a `bool_only=True`.

    Raises:
        VerifyError: Obecná výjimka validace.
        VerifyInnerCheckError: Pokud validace typu hodnoty proběhne, ale vnitřní typy selžou.
        VerifyUnexpectedInternalError: Pokud dojde k jiné neočekávané výjimce.

    Example:
        '>>> iterable_item_verifier([1, 2, 3], list, {}, annotation=List[int])
        True
    """

    # Definice parametru pro ověření typu
    base_type_result = None

    try:

        # Kontrola základního typu
        base_type_result = verify_base_type(
            value,
            expected_type,
            duck_typing_instructions,
            duck_typing,
            bool_only
        )

        # Kontrola zda je výsledek negativní
        # V tomto bodě, base_type_result musí být buď True nebo False (nebo je vyvolaná výjimka)
        if not base_type_result:
            return False

        # Pokud není požadována vnitřní validace, návrat
        if not inner_check:
            return True

        # Ověření a získání vnitřních typových anotací
        inner_args = get_args_safe(annotation)

        # Pokud nejsou specifikovány vnitřní typy, návrat
        if not inner_args:
            return True

        # Kontrola vnitřních položek
        return verify_iterable_items(
            value,
            inner_args[0],
            custom_types,
            inner_check,
            duck_typing,
            bool_only
        )

    # Ošetření vnitřních výjimek
    except VerifyError as e:

        # Definovat výjimku popisující danou metodu a výjimku která byla zachycena


        raise VerifyInnerCheckError(value, annotation, base_type_result, e)

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e
