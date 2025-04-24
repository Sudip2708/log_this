from ..._bases import IsInstanceValidatorBase
import enum


class EnumValidator(IsInstanceValidatorBase):
    """
    Validátor pro Enum

    Hint:
        Enum = Výčtový typ definující množinu pojmenovaných hodnot
    """

    VALIDATOR_KEY = "Enum"
    ANNOTATION = "enum.Enum"
    INFO = "Definuje výčtový typ"
    ORIGIN = None

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        if not isinstance(value, enum.Enum):
            raise TypeError(f"Hodnota '{value}' není validní Enum.")

        # Pokud je anotace konkrétní třída Enum, kontrolujeme příslušnost
        if annotation is not enum.Enum and issubclass(annotation, enum.Enum):
            if not isinstance(value, annotation):
                raise TypeError(
                    f"Hodnota '{value}' není instancí požadovaného Enum typu {annotation.__name__}.")

        return True