from typing import Annotated, Any, Tuple, Union
from array import array

from ..end_verifiers import is_instance_verifier
from .._tools import get_args_safe
from ..._exceptions import (
    VerifyError,
    InternalUnexpectedError,
    ArrayValueError
)


def array_verifier(
        value: Any,
        expected: Union[type, Tuple[type, ...]],
        annotation: Any = None,
        depth_check: Union[bool, int] = True,
        bool_only: bool = False
) -> bool:
    """
    Validuje, zda je hodnota typu array.array a případně kontroluje typový kód a hodnoty.

    Nejprve ověří, zda objekt je instancí array.array. Pokud je povolena
    hloubková validace (`depth_check`) a jsou k dispozici metadata o očekávaném
    typovém kódu (např. přes Annotated), zkontroluje i typový kód pole.

    Args:
        value (Any): Hodnota, která má být validována.
        expected (Union[type, Tuple[type, ...]]): Požadovaný typ array.array.
        annotation (Any, optional): Typová anotace, která může obsahovat metadata o typovém kódu.
        depth_check (Union[bool, int], optional): Pokud True, provede se kontrola typového kódu.
            Pokud int, určuje hloubku validace. False přeskočí kontrolu typového kódu.
        bool_only (bool, optional): Pokud je True, funkce pouze vrací True/False bez výjimek.

    Returns:
        bool: True, pokud validace proběhne úspěšně. Jinak vyhazuje výjimku.

    Raises:
        VerifyError: Pokud validace typu selže.
        TypeValidationError: Pokud typový kód pole neodpovídá očekávanému.
        InternalUnexpectedError: Pokud dojde k nečekané interní chybě během validace.

    Example:
        >>> # Základní validace typu
        >>> array_verifier(array('i', [1, 2, 3]), array)
        True
        >>> # Validace s kontrolou typového kódu (s využitím Annotated)
        >>> from typing import Annotated
        >>> IntArray = Annotated[array, 'i']
        >>> array_verifier(array('i', [1, 2, 3]), array, IntArray, True)
        True
    """

    try:
        # Validace základního typu (array.array)
        is_instance_verifier(value, expected)

        # Pokud není požadována hloubková validace, vrátíme True
        if not depth_check:
            return True

        # Pokusíme se získat metadata o typovém kódu
        inner_args = get_args_safe(annotation)

        # Pokud je anotace Annotated a má metadata s typovým kódem
        if (
                inner_args
                and hasattr(annotation, "__origin__")
                and annotation.__origin__ is Annotated
        ):

            # První argument je samotný typ, druhý jsou metadata
            if (
                    len(inner_args) >= 2
                    and isinstance(inner_args[1], str)
                    and len(inner_args[1]) == 1
            ):

                # Získání očekávaného kodu
                expected_typecode = inner_args[1]

                # Validace typového kódu
                if value.typecode != expected_typecode:

                    # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
                    if bool_only:
                        return False

                    # Jinak vyhoď výjimku pro nevalidní hodnotu
                    raise ArrayValueError(value)

        # Pokud vše projde, vrátíme True
        return True

    except VerifyError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise InternalUnexpectedError(e) from e
