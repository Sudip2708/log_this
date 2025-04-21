from typing import Callable, get_args
import inspect

from .._base_type_validator import BaseTypeValidator


class CallableValidator(BaseTypeValidator):
    """
    Validátor pro zápis Callable[[ArgType1, ArgType2, ...], ReturnType]

    Validuje pouze zda je objekt volatelný (callable),
    nevaliduje typy argumentů a návratové hodnoty.

    Hint:
        Callable[[ArgType1, ArgType2, ...], ReturnType] = Volatelný objekt s definovanými
        typy argumentů a návratovou hodnotou
    """

    # Definice klíče pro registr
    VALIDATOR_KEY = "callable"
    ANNOTATION = Callable
    INFO = "Definuje volatelný objekt."
    GET_ORIGIN = callable


    # Validace vnitřních stavů
    def validate(self, value, annotation, depth_check, custom_types, bool_only) -> bool:

        # Validace sebe sama (origin)
        if not callable(value):
            return False

        try:
            expected_args, _ = get_args(annotation)
            sig = inspect.signature(value)
            params = list(sig.parameters.values())

            # Ověření počtu argumentů
            if len(expected_args) != len(params):
                return False

            # (Volitelně) Ověření typů
            for expected, actual in zip(expected_args, params):
                if actual.annotation is inspect._empty:
                    continue  # typ neanotován → nelze ověřit

                if actual.annotation != expected:
                    return False

            return True

        except Exception:
            return False
