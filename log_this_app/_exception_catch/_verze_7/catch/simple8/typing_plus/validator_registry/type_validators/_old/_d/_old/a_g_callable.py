from typing import Callable, get_args
import inspect


from ._callable_alike_base import CallableAlikeBase


class CallableValidator(CallableAlikeBase):
    """
    Validátor pro zápis Callable[[ArgType1, ArgType2, ...], ReturnType]

    Validuje pouze zda je objekt volatelný (callable),
    nevaliduje typy argumentů a návratové hodnoty.

    Hint:
        Callable[[ArgType1, ArgType2, ...], ReturnType] = Volatelný objekt s definovanými
        typy argumentů a návratovou hodnotou
    """

    # Definice klíče pro registr
    VALIDATOR_TYPE = Callable

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama - kontrola zda je objekt volatelný
        if not callable(value):
            if bool_only:
                return False
            raise TypeError(
                f"Očekáván volatelný objekt, ale obdrženo {type(value).__name__}")

        # Poznámka: Nevalidujeme typy argumentů a návratovou hodnotu,
        # protože to by vyžadovalo funkci zavolat, což není žádoucí

        return True

    def validate2(self, value, annotation, depth_check, custom_types, bool_only):

        # Validace sebe sama - kontrola zda je objekt volatelný
        if not callable(value):
            if bool_only:
                return False
            raise TypeError(
                f"Očekáván volatelný objekt, ale obdrženo {type(value).__name__}")

        # Poznámka: Nevalidujeme typy argumentů a návratovou hodnotu,
        # protože to by vyžadovalo funkci zavolat, což není žádoucí

        return True

    # Validace vnitřních stavů
    def is_callable_compatible(self, value, annotation, depth_check, custom_types, bool_only) -> bool:
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
