from typing import Any, Tuple, Union

from .exceptions import (
    VerifyValueHasAttributeError,
    VerifyExpectedHasAttributeError,
    VerifyUnexpectedInternalError,
    VerifyError
)


class ValidateHasAttribute:
    """
    Ověřuje, zda objekt má požadovaný atribut nebo všechny atributy.
    """

    def __call__(
        self,
        value: Any,
        expected: Union[str, Tuple[str, ...]],
        annotation: str,
        bool_only: bool = False
    ) -> bool:
        """
        Ověří, zda objekt `value` má požadovaný atribut (nebo všechny atributy).

        Args:
            value: Objekt, který se ověřuje.
            expected: Jméno atributu jako string nebo tuple atributů (např. '__aiter__', '__anext__').
            bool_only: Pokud True, vrací pouze True/False bez vyvolání výjimek.

        Returns:
            True, pokud objekt má všechny požadované atributy.

        Raises:
            VerifyValueTypeError: Pokud objekt nemá požadovaný atribut (a `bool_only` je False).
            VerifyExpectedTypeError: Pokud `expected` není string nebo tuple stringů.
            VerifyUnexpectedInternalError: Pokud dojde k neočekávané chybě.
        """

        try:

            # Ověření, zda objekt má všechny požadované atributy
            if all(hasattr(value, attr) for attr in expected):
                return True

            # Kontrola zda odpověď má být bool
            if bool_only:
                return False

            # Zjištění chybějících atributů pro lepší výpis chyby
            missing = [attr for attr in expected if not hasattr(value, attr)]
            raise VerifyValueHasAttributeError(
                value, expected, annotation, missing
            )

        except VerifyError:
            raise

        except TypeError as e:
            raise VerifyExpectedHasAttributeError(expected) from e

        except Exception as e:
            raise VerifyUnexpectedInternalError(
                info="Chyba nastala při validaci přítomnosti atributů.",
                modul="Zachyceno v metodě __call__ třídy ValidateHasAttribute.",
                original_exception=e
            ) from e


validate_has_attribute = ValidateHasAttribute()


