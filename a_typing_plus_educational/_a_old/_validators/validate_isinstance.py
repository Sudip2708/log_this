from typing import Any, Tuple, Union

from .exceptions import (
    VerifyValueTypeError,
    VerifyExpectedTypeError,
    VerifyInternalUnexpectedError,
    VerifyError
)


class ValidateIsInstance:
    """
    Ověřuje, zda je zadaná hodnota instancí očekávaného typu nebo jedním z očekávaných typů.
    """

    def __call__(
            self,
            value: Any,
            expected: Union[type, Tuple[type, ...]],
            bool_only: bool = False
    ) -> bool:
        """
        Ověří, zda je poskytnutá hodnota instancí očekávaného typu.

        Args:
            value: Hodnota k ověření. Může být libovolného typu.
            expected: Očekávaný typ nebo tuple očekávaných typů.

        Returns:
            True, pokud je `value` instancí `expected` typu (nebo jednoho z typů v `expected` tuple).

        Raises:
            VerifyValueTypeError: Pokud `value` není instancí očekávaného typu.
            VerifyExpectedTypeError: Pokud `expected` není platný typ nebo tuple typů.
            VerifyInternalUnexpectedError: Pokud během validace dojde k neočekávané vnitřní chybě.
        """

        try:
            # Ověření, zda hodnota odpovídá očekávané instanci
            if isinstance(value, expected):
                return True

            # Kontrola zda odpověď má být bool
            if bool_only:
                return False

            # Vyvolání výjimky s oznamem o nevalidní hodnotě
            raise VerifyValueTypeError(value, expected)

        # Propagace již existujících ošetřených výjimek (např. z vlastních validací)
        except VerifyError:
            raise

        # Vyvolání výjimky s oznamem o nevalidní hodnotě pro expected
        except TypeError as e:
            raise VerifyExpectedTypeError(expected) from e

        # Zachycení neočekávaných výjimek
        except Exception as e:
            raise VerifyInternalUnexpectedError(
                info = f"Chyba nastala při validaci nativního typu.",
                modul = "Zachyceno v metodě __call__ třídy ValidateIsInstance.",
                original_exception = e
            ) from e

validate_is_instance = ValidateIsInstance()

