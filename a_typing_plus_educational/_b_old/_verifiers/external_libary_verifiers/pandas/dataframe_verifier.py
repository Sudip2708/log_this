from typing import Any, Dict, List, Union, Tuple, Annotated
import pandas as pd

from ...end_verifiers import is_instance_verifier
from ..._tools import get_args_safe
from ...._exceptions import VerifyError, VerifyUnexpectedInternalError, PandasValueError


def pandas_dataframe_verifier(
        value: Any,
        expected: Union[type, Tuple[type, ...]],
        annotation: Any = None,
        depth_check: Union[bool, int] = True,
        bool_only: bool = False
) -> bool:
    """
    Validuje, zda je hodnota typu pandas.DataFrame.

    Pokud je povolena hloubková validace (`depth_check`) a jsou k dispozici metadata,
    provádí se kontrola povinných sloupců a jejich datových typů.

    Args:
        value (Any): Hodnota, která má být validována.
        expected (Union[type, Tuple[type, ...]]): Požadovaný typ (DataFrame).
        annotation (Any, optional): Typová anotace, může obsahovat metadata o sloupích a jejich typech.
            Např. Annotated[pd.DataFrame, {'columns': ['A', 'B'], 'dtypes': {'A': 'int64', 'B': 'object'}}]
        depth_check (Union[bool, int], optional): Pokud True, provede se hloubková kontrola.
        bool_only (bool, optional): Pokud je True, vrátí se pouze True/False bez výjimek.

    Returns:
        bool: True, pokud validace proběhne úspěšně, jinak vyhazuje výjimku.

    Raises:
        VerifyError: Pokud validace typu selže.
        PandasValueError: Pokud DataFrame neodpovídá požadovaným vlastnostem.
        VerifyUnexpectedInternalError: Pokud dojde k nečekané interní chybě.
    """
    try:
        # Validace základního typu (pandas.DataFrame)
        is_instance_verifier(value, expected)

        # Pokud není požadována hloubková validace, vrátíme True
        if not depth_check:
            return True

        # Pokusíme se získat metadata z Annotated[...]
        inner_args = get_args_safe(annotation)

        # Pokud je anotace Annotated a má metadata
        if (
                inner_args
                and hasattr(annotation, "__origin__")
                and annotation.__origin__ is Annotated
        ):
            # První argument je samotný typ, druhý jsou metadata
            if len(inner_args) >= 2 and isinstance(inner_args[1], dict):
                metadata = inner_args[1]

                # Kontrola přítomnosti sloupců
                if 'columns' in metadata:
                    expected_columns = set(metadata['columns'])
                    actual_columns = set(value.columns)

                    # Kontrola, zda DataFrame obsahuje všechny požadované sloupce
                    missing_columns = expected_columns - actual_columns

                    if missing_columns:

                        if bool_only:
                            return False

                        raise PandasValueError(
                            value,
                            f"Chybějící sloupce: {missing_columns}"
                        )

                # Kontrola datových typů sloupců
                if 'dtypes' in metadata:
                    expected_dtypes = metadata['dtypes']

                    for col, dtype in expected_dtypes.items():


                        if col in value.columns:
                            # Převod pandas dtype objektu na string pro porovnání
                            actual_dtype = str(value[col].dtype)

                            if actual_dtype != dtype:

                                if bool_only:
                                    return False

                                raise PandasValueError(
                                    value,
                                    f"Sloupec '{col}' má nesprávný dtype. "
                                    f"Očekávaný: {dtype}, Aktuální: {actual_dtype}"
                                )

        return True

    except VerifyError:
        raise

    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e