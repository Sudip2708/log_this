from typing import Any, Tuple, Union

from ..end_verifiers import is_instance_verifier
from ..typing_validator import validate_typing
from .._tools import (
    reduce_depth_check,
    compare_dicts_keys,
    get_attr_safe,
    get_type_hints_safe,
    check_required_keys
)
from ..._exceptions import (
    VerifyError,
    VerifyUnexpectedInternalError
)


def iterable_key_value_verifier_for_typeddict(
    value: Any,
    expected: Union[type, Tuple[type, ...]],
    annotation: Any = None,
    depth_check: Union[bool, int] = True,
    custom_types: dict = None,
    bool_only: bool = False
) -> bool:
    """
    Validuje hodnotu vůči anotaci typu `TypedDict` a jejímu vnitřnímu rozložení.

    Tato funkce rozšiřuje základní logiku validace slovníku o specifika `TypedDict`:
    kontroluje typy hodnot podle anotace atributů a případně přítomnost či nepřítomnost klíčů
    v závislosti na totalitě (`__total__`) typu.

    - Pokud je `TypedDict` totalitní (`__total__=True`), ověřuje se:
        - že slovník má přesně všechny požadované klíče,
        - že žádný klíč nechybí ani nepřebývá,
        - a že všechny hodnoty odpovídají definovaným typům.
    - Pokud není totalitní (`__total__=False`), ověřuje se:
        - že slovník obsahuje minimálně všechny povinné klíče,
        - a že definované klíče (pokud existují v hodnotě) odpovídají svému typu.

    Hloubková kontrola (`depth_check`) umožňuje rekurzivní validaci hodnot uvnitř `TypedDict`.
    Stejně jako u běžného slovníku lze kontrolovat typy klíčů a hodnot do zvolené hloubky.

    Args:
        value (Any): Hodnota, která má být validována.
        expected (Union[type, Tuple[type, ...]]): Očekávaný základní typ (např. `dict` nebo `TypedDict`).
        annotation (Any, optional): Třída typu `TypedDict`, která definuje očekávané klíče a jejich typy.
        depth_check (Union[bool, int], optional): Hloubková kontrola. Pokud je `int`, určuje počet úrovní.
        custom_types (Tuple[Any, ...], optional): Vlastní typy, které se mají považovat za validní.
        bool_only (bool, optional): Pokud `True`, vrací pouze `True`/`False` bez vyhazování výjimek.

    Returns:
        bool: `True`, pokud hodnota projde validací. Jinak vyhazuje výjimku nebo vrací `False`, pokud `bool_only=True`.

    Raises:
        VerifyError: Pokud hodnota nebo její vnitřní prvky neodpovídají očekávaným typům nebo chybí povinné klíče.
        VerifyUnexpectedInternalError: Pokud dojde k nečekané interní chybě.

    Example:
        >>> class UserData(TypedDict):
        ...     name: str
        ...     age: int
        >>> iterable_key_value_verifier_for_typeddict({"name": "Alice", "age": 30}, dict, UserData)
        True
    """

    try:

        # Validace základního typu (např. dict)
        is_instance_verifier(value, expected)

        # Pokud není požadována vnitřní validace, návrat
        if not depth_check:
            return True

        # Ověření a získání vnitřních typových anotací pro klíče a hodnoty
        type_hints = get_type_hints_safe(annotation)

        # Pokud nemáme žádné anotace, vrátíme True
        if not type_hints:
            return True

        # Získání informací o totalitě (všechny klíče jsou povinné)
        is_total = get_attr_safe(annotation, "__total__", True)

        # Pokud je hlavní třída total (potomek musí přesně korespondovat)
        if is_total:

            # Kontrola zda oba slovníky obsahují shodné klíče
            compare_dicts_keys(type_hints, value)

            # Kopije hodnoty zanoření
            inner_depth = depth_check

            # Kontrola typů u existujících klíčů
            for key, val in value.items():

                # Odpočet zanoření pro další kontrolu
                inner_depth = reduce_depth_check(inner_depth)

                # Kontrola na očekávaný typ
                expected_type = type_hints[key]

                # Validace hodnoty a typu
                validate_typing(
                    val, expected_type, inner_depth, custom_types, bool_only
                )

                # Kontrola zanoření
                if not inner_depth:
                    break

        # Pokud hlavní třída není total (potomek nemusí mýt všechny klíče a může mít i klíče navíc)
        else:

            # Kontrola zda slovník obsahuje poviné klíče
            check_required_keys(type_hints, value)

            # Kopije hodnoty zanoření
            inner_depth = depth_check

            # Validace každého klíče a hodnoty
            for key, val in value.items():

                # Kontrola zda je klíč definovaný na hlavní třídě
                if key in type_hints:

                    # Odpočet zanoření pro další kontrolu
                    inner_depth = reduce_depth_check(inner_depth)

                    # Načtení typu z hlavní třídy
                    expected_type = type_hints[key]

                    # Validace hodnoty a typu
                    validate_typing(
                        val, expected_type, inner_depth, custom_types, bool_only
                    )

                # Přerušení cyklu, pokud se dosáhne maximální hloubky
                if not inner_depth:
                    break

        # Pokud vše proběhne v pořádku a bez chyb
        return True

    # Propagace všech již ošetřených výjimek
    except VerifyError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e