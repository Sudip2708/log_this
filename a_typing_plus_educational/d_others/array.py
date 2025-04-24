from ..._bases import IsInstanceValidatorBase
import array


class ArrayValidator(IsInstanceValidatorBase):
    """
    Validátor pro array.array

    Hint:
        array.array = Efektivní pole s homogenním datovým typem
    """

    VALIDATOR_KEY = "array"
    ANNOTATION = "array.array"
    INFO = "Definuje objekt typu array.array"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, array.array):
            raise TypeError(
                f"Hodnota '{value}' není validní array.array objekt.")

        # Pokud anotace obsahuje informaci o typovém kódu
        if hasattr(annotation, "typecode") and annotation.typecode is not None:
            if value.typecode != annotation.typecode:
                raise TypeError(
                    f"Array má nesprávný typový kód. Očekáváno: {annotation.typecode}, získáno: {value.typecode}")

        return True