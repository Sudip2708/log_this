import pandas as pd
from typing import Annotated, Any, Union, Tuple
from ...end_verifiers import is_instance_verifier
from ..._tools import get_args_safe
from ...._exceptions import VerifyError, InternalUnexpectedError, PandasValueError


def pandas_series_verifier(
        value: Any,
        expected: Union[type, Tuple[type, ...]],
        annotation: Any = None,
        depth_check: Union[bool, int] = True,
        bool_only: bool = False
) -> bool:
    """
    Validuje, zda je hodnota typu pandas.Series.

    Pokud je povolena hloubková validace (`depth_check`) a jsou k dispozici metadata,
    provádí se kontrola datového typu (dtype) a dalších vlastností Series.

    Args:
        value (Any): Hodnota, která má být validována.
        expected (Union[type, Tuple[type, ...]]): Požadovaný typ (Series).
        annotation (Any, optional): Typová anotace, může obsahovat metadata o datovém typu.
            Např. Annotated[pd.Series, {'dtype': 'int64', 'name': 'hodnoty'}]
        depth_check (Union[bool, int], optional): Pokud True, provede se hloubková kontrola.
        bool_only (bool, optional): Pokud je True, vrátí se pouze True/False bez výjimek.

    Returns:
        bool: True, pokud validace proběhne úspěšně, jinak vyhazuje výjimku.

    Raises:
        VerifyError: Pokud validace typu selže.
        PandasValueError: Pokud Series neodpovídá požadovaným vlastnostem.
        InternalUnexpectedError: Pokud dojde k nečekané interní chybě.
    """
    try:
        # Validace základního typu (pandas.Series)
        is_instance_verifier(value, expected)

        # Pokud není požadována hloubková validace, vrátíme True
        if not depth_check:
            return True

        # Pokusíme se získat metadata z Annotated[...]
        inner_args = get_args_safe(annotation)

        # Pokud je anotace Annotated a má metadata
        if (
                inner_args and
                hasattr(annotation, "__origin__")
                and annotation.__origin__ is Annotated
        ):
            # První argument je samotný typ, druhý jsou metadata
            if len(inner_args) >= 2 and isinstance(inner_args[1], dict):
                metadata = inner_args[1]

                # Kontrola datového typu
                if 'dtype' in metadata:
                    expected_dtype = metadata['dtype']
                    actual_dtype = str(value.dtype)

                    if actual_dtype != expected_dtype:

                        if bool_only:
                            return False

                        raise PandasValueError(
                            value,
                            f"Nesprávný dtype. Očekávaný: {expected_dtype}, "
                            f"Aktuální: {actual_dtype}"
                        )

                # Kontrola názvu Series
                if 'name' in metadata and metadata['name'] is not None:
                    expected_name = metadata['name']

                    if value.name != expected_name:

                        if bool_only:
                            return False

                        raise PandasValueError(
                            value,
                            f"Nesprávný název Series. Očekávaný: {expected_name}, "
                            f"Aktuální: {value.name}"
                        )

        return True

    except VerifyError:
        raise

    except Exception as e:
        raise InternalUnexpectedError(e) from e