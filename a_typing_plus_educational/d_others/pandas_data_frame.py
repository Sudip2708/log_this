from ..._bases import IsInstanceValidatorBase
import pandas as pd


class DataFrameValidator(IsInstanceValidatorBase):
    """
    Validátor pro pandas.DataFrame

    Hint:
        pandas.DataFrame = Dvourozměrná tabulková struktura dat s označenými osami
    """

    VALIDATOR_KEY = "DataFrame"
    ANNOTATION = "pandas.DataFrame"
    INFO = "Definuje pandas DataFrame objekt"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, pd.DataFrame):
            raise TypeError(f"Hodnota '{value}' není validní pandas.DataFrame.")

        # Pokud má anotace specifikované typy sloupců
        if hasattr(annotation, "dtypes") and annotation.dtypes is not None:
            for col, expected_type in annotation.dtypes.items():
                if col not in value.columns:
                    raise TypeError(f"Sloupec '{col}' chybí v DataFrame.")
                if value[col].dtype != expected_type:
                    raise TypeError(
                        f"Sloupec '{col}' má nesprávný datový typ. Očekáváno: {expected_type}, získáno: {value[col].dtype}")

        return True