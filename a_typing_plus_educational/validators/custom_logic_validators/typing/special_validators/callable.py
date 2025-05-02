from typing import Callable

from ....._bases import BaseCustomLogicValidator
from ....._verifiers import callable_verifier

class CallableValidator(BaseCustomLogicValidator):

    # Definice klíče pro registr
    VALIDATOR_KEY = "callable"
    ANNOTATION = Callable

    IS_INSTANCE = callable
    HAS_ATTRS = "__call__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Volatelný objekt (funkce, metoda)"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je Callable, tj. může být volán jako funkce. "
            "Lze specifikovat vstupní i návratové typy."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Definice metody __call__ pro ověření volatelnosti objektu."""

        return callable_verifier(
            value
        )
