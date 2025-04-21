from typing import Any, Tuple, Union

from ._exceptions import VerifyTypeError, VerifyUnexpectedError, VerifyError
from ._get_simplified_traceback import get_simplified_traceback

class ValidateNativeType:

    def __call__(
            self,
            value: Any,
            expected: Union[type, Tuple[type, ...]]
    ):

        try:
            # Ověření, zda hodnota odpovídá očekávané instanci
            if isinstance(value, expected):
                return True

            # Vyvolání výjimky s oznamem o nevalidní hodnotě
            raise VerifyValueTypeError(value, expected)

        # Propagace již existujících ošetřených výjimek
        except VerifyError:
            raise

        # Vyvolání výjimky s oznamem o nevalidní hodnotě pro expected
        except TypeError as e:
            raise VerifyExpectedTypeError(value, expected)

        # Zachycení neočekávaných výjimek
        except Exception as e:
            raise VerifyUnexpectedError()


    def _get_exp_tuple_as_string(self):
        """Vrátí tuple převedené na řetězec."""
        return ', '.join(t.__name__ for t in self._expected)

    def _get_expected_text_for_error_message(self):
        """Vrátí řetězec definující očekávané typy"""
        return (
            f"Požadované typy (instance): {self._get_exp_tuple_as_string()}"
            if isinstance(self._expected , tuple)
            else f"Požadovaný typ (instance): {self._expected .__name__}"
        )

    def _value_not_expected_error_message(self):
        what_happened = [
            f"   - Ověřovaná hodnota neodpovídá požadovaným kritériím.\n"
            f"   - Ověřovaná hodnota: {repr(self._value)}\n"
            f"   - Typ (instance) ověřované hodnoty: {type(self._value).__name__}\n"
            f"   - {self._get_expected_text_for_error_message()}\n"
        ]
        what_to_do = [
            "   - Zkontrolujte kód volající tuto funkci a hodnoty, "
            "které jsou předány a očekávány.\n"
            "   - Prohlédněte si stručný přehled návazností (výše), "
            "zda chybu neoběvíte tam."
        ]
        return what_happened, what_to_do

    def _uncorrected_expected_error_message(self):
        pass

    def _unexpected_error_message(self):
        pass

validate_native_type = ValidateNativeType()
validate_native_type("123", (int, bool))