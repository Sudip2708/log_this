from .._base_type_validator import BaseTypeValidator
import pandas as pd


class SeriesValidator(BaseTypeValidator):
    """
    Validátor pro pandas.Series

    Hint:
        pandas.Series = Jednorozměrná označená struktura dat
    """

    VALIDATOR_KEY = "Series"
    ANNOTATION = "pandas.Series"
    INFO = "Definuje pandas Series objekt"
    ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, pd.Series):
            raise TypeError(f"Hodnota '{value}' není validní pandas.Series.")
        return True