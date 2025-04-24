from ..._bases import IsInstanceValidatorBase
import numpy as np


class NdarrayValidator(IsInstanceValidatorBase):
    """
    Validátor pro numpy.ndarray

    Hint:
        numpy.ndarray = NumPy n-rozměrné pole
    """

    VALIDATOR_KEY = "ndarray"
    ANNOTATION = "numpy.ndarray"
    INFO = "Definuje NumPy n-rozměrné pole"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, np.ndarray):
            raise TypeError(f"Hodnota '{value}' není validní numpy.ndarray.")

        # Pokud má anotace specifikován datový typ
        if hasattr(annotation, "dtype") and annotation.dtype is not None:
            if value.dtype != annotation.dtype:
                raise TypeError(
                    f"Numpy pole má nesprávný datový typ. Očekáváno: {annotation.dtype}, získáno: {value.dtype}")

        return True