from typing import Any, Tuple, Union

from .exceptions import (
    VerifyValueTypeError,
    VerifyExpectedTypeError,
    VerifyInternalUnexpectedError,
    VerifyError
)


class ValidateNativeType:
    """
    Ověřuje, zda je zadaná hodnota instancí očekávaného typu nebo jedním z očekávaných typů.
    """

    def __call__(
            self,
            value: Any,
            expected: Union[type, Tuple[type, ...]]
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
                info="Chyba nastala při validaci hodnoty.",
                modul="Zachyceno v metodě __call__ třídy ValidateNativeType",
                original_exception=e
            ) from e


validate_native_type = ValidateNativeType()
# Příklad volání pro ilustraci (výsledek se nikde nepoužívá)
validate_native_type("123", (int, bool))