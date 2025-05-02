from typing import Any, Tuple, Union, Optional, List
import numpy as np

from ..end_verifiers import is_instance_verifier
from .._tools import get_args_safe
from ..._exceptions import (
    VerifyError,
    InternalUnexpectedError,
    NumpyArrayValueError
)


def numpy_array_verifier(
        value: Any,
        expected: Union[type, Tuple[type, ...]],
        annotation: Any = None,
        depth_check: Union[bool, int] = True,
        bool_only: bool = False
) -> bool:
    """
    Validuje, zda je hodnota typu numpy.ndarray a případně kontroluje dtype a tvar.

    Nejprve ověří, zda objekt je instancí numpy.ndarray. Pokud je povolena
    hloubková validace (`depth_check`) a jsou k dispozici metadata o očekávaném
    dtype nebo tvaru pole (např. přes Annotated), kontroluje i tyto vlastnosti.

    Args:
        value (Any): Hodnota, která má být validována.
        expected (Union[type, Tuple[type, ...]]): Požadovaný typ numpy.ndarray.
        annotation (Any, optional): Typová anotace, která může obsahovat metadata o dtype/tvaru.
        depth_check (Union[bool, int], optional): Pokud True, provede se kontrola dtype/tvaru.
            Pokud int, určuje hloubku validace. False přeskočí rozšířenou kontrolu.
        bool_only (bool, optional): Pokud je True, funkce pouze vrací True/False bez výjimek.

    Returns:
        bool: True, pokud validace proběhne úspěšně. Jinak vyhazuje výjimku.

    Raises:
        VerifyError: Pokud validace typu selže.
        NumpyArrayValueError: Pokud dtype nebo tvar pole neodpovídá očekávanému.
        InternalUnexpectedError: Pokud dojde k nečekané interní chybě během validace.

    Example:
        >>> # Základní validace typu
        >>> import numpy as np
        >>> numpy_array_verifier(np.array([1, 2, 3]), np.ndarray)
        True
        >>> # Validace s kontrolou dtype a tvaru (s využitím Annotated)
        >>> from typing import Annotated
        >>> IntArray = Annotated[np.ndarray, {'dtype': np.int64, 'shape': (3,)}]
        >>> numpy_array_verifier(np.array([1, 2, 3], dtype=np.int64), np.ndarray, IntArray, True)
        True
    """

    try:
        # Validace základního typu (numpy.ndarray)
        is_instance_verifier(value, expected)

        # Pokud není požadována hloubková validace, vrátíme True
        if not depth_check:
            return True

        # Pokusíme se získat metadata o dtype a tvaru
        inner_args = get_args_safe(annotation)

        # Pokud je anotace Annotated a má metadata s dtype nebo tvarem
        if (
                inner_args
                and hasattr(annotation, "__origin__")
                and annotation.__origin__ is Annotated
        ):
            # První argument je samotný typ, druhý jsou metadata
            if len(inner_args) >= 2 and isinstance(inner_args[1], dict):
                metadata = inner_args[1]

                # Kontrola dtype
                if 'dtype' in metadata:
                    expected_dtype = metadata['dtype']
                    # Porovnání dtype (podporuje jak string reprezentaci, tak numpy datové typy)
                    if not np.issubdtype(value.dtype, expected_dtype):
                        # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
                        if bool_only:
                            return False

                        # Jinak vyhoď výjimku pro nevalidní dtype
                        raise NumpyArrayValueError(
                            value,
                            f"Očekávaný dtype: {expected_dtype}, "
                            f"Aktuální dtype: {value.dtype}"
                        )

                # Kontrola tvaru (shape)
                if 'shape' in metadata:
                    expected_shape = metadata['shape']

                    # Pokud je expected_shape None, akceptujeme jakýkoli tvar
                    if expected_shape is not None:
                        # Kontrola tvaru s podporou pro None ve specifikaci dimenze
                        if not _check_shape_compatibility(value.shape,
                                                          expected_shape):
                            # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
                            if bool_only:
                                return False

                            # Jinak vyhoď výjimku pro nevalidní tvar
                            raise NumpyArrayValueError(
                                value,
                                f"Očekávaný tvar: {expected_shape}, "
                                f"Aktuální tvar: {value.shape}"
                            )

        # Pokud vše projde, vrátíme True
        return True

    except VerifyError:
        raise

    # Zachycení všech ostatních neočekávaných výjimek
    except Exception as e:
        raise InternalUnexpectedError(e) from e


def _check_shape_compatibility(actual_shape: Tuple[int, ...],
                               expected_shape: Union[Tuple, List]) -> bool:
    """
    Kontroluje kompatibilitu tvaru pole s očekávaným tvarem.

    Podporuje:
    - Přesné porovnání (3,4) == (3,4)
    - Porovnání s None, kde None znamená libovolný rozměr: (3, None) == (3, 5)
    - Porovnání s Ellipsis (...), kde ... znamená libovolný počet dimenzí: (3, ...) == (3, 4, 5)

    Args:
        actual_shape: Skutečný tvar numpy pole
        expected_shape: Očekávaný tvar se specifikací

    Returns:
        bool: True, pokud jsou tvary kompatibilní
    """
    # Převedení expected_shape na list pro jednodušší manipulaci
    expected = list(expected_shape)
    actual = list(actual_shape)

    # Pokud je v expected_shape Ellipsis (...)
    if Ellipsis in expected:
        ellipsis_idx = expected.index(Ellipsis)

        # Rozdělit očekávaný tvar na části před a po ...
        prefix = expected[:ellipsis_idx]
        suffix = expected[ellipsis_idx + 1:]

        # Kontrola prefixu
        if len(actual) < len(prefix) + len(suffix):
            return False

        for i, dim in enumerate(prefix):
            if dim is not None and actual[i] != dim:
                return False

        # Kontrola suffixu (od konce)
        for i, dim in enumerate(reversed(suffix)):
            if dim is not None and actual[-(i + 1)] != dim:
                return False

        return True

    # Standardní porovnání bez Ellipsis
    if len(actual) != len(expected):
        return False

    for a, e in zip(actual, expected):
        # None v expected_shape znamená jakýkoli rozměr
        if e is not None and a != e:
            return False

    return True